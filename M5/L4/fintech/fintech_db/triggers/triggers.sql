-- ============================
-- TRIGGERS (PostgreSQL)
-- - Saldo inicial = 10000 al crear cliente
-- - Al "confirmar" una transferencia (insert en log con ok=true y estado que aplica saldos)
--   => descuenta al origen y suma al destino automáticamente
-- ============================

-- Recomendado
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================
-- 0) SEMILLAS MÍNIMAS (COIN + estados)
-- ============================
INSERT INTO activos (codigo, nombre, decimales, activo)
VALUES ('COIN', 'Moneda interna', 2, TRUE)
ON CONFLICT (codigo) DO NOTHING;

INSERT INTO transfer_estado_catalogo (est_code, descripcion, severidad, aplica_saldos)
VALUES
  ('CREATED',     'Transferencia creada',                 'info',    FALSE),
  ('CONFIRMED',   'Transferencia confirmada (aplica)',    'info',    TRUE),
  ('BAL_INSUF',   'Saldo insuficiente',                   'error',   FALSE),
  ('ALREADY_APPL','Transferencia ya aplicada',            'warning', FALSE)
ON CONFLICT (est_code) DO NOTHING;


-- =========================================
-- 1) CLIENTE -> crear cuenta COIN con 10000
-- =========================================
CREATE OR REPLACE FUNCTION fn_clientes_crear_cuenta_inicial()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
  v_act_id SMALLINT;
BEGIN
  -- asegura activo default
  INSERT INTO activos (codigo, nombre, decimales, activo)
  VALUES ('COIN', 'Moneda interna', 2, TRUE)
  ON CONFLICT (codigo) DO NOTHING;

  SELECT act_id INTO v_act_id
  FROM activos
  WHERE codigo = 'COIN';

  -- crea cuenta con saldo inicial
  INSERT INTO cuentas (cli_id, act_id, saldo, estado)
  VALUES (NEW.cli_id, v_act_id, 10000, 'activa')
  ON CONFLICT (cli_id, act_id) DO NOTHING;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_clientes_crear_cuenta_inicial ON clientes;

CREATE TRIGGER trg_clientes_crear_cuenta_inicial
AFTER INSERT ON clientes
FOR EACH ROW
EXECUTE FUNCTION fn_clientes_crear_cuenta_inicial();


-- ======================================================
-- 2) APLICAR TRANSFERENCIA al CONFIRMAR (log ok=true)
-- Reglas:
-- - Se confirma insertando en transferencias_log: ok=true + est_code con aplica_saldos=true
-- - Bloquea cuentas origen/destino (FOR UPDATE) para atomicidad
-- - Valida saldo suficiente
-- - Evita doble aplicación (estado_actual='aplicada')
-- ======================================================
CREATE OR REPLACE FUNCTION fn_transferencias_aplicar_al_confirmar()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
  v_aplica BOOLEAN;
  v_origen BIGINT;
  v_destino BIGINT;
  v_act SMALLINT;
  v_monto NUMERIC(20,6);

  v_cta_origen BIGINT;
  v_cta_destino BIGINT;

  v_saldo_origen NUMERIC(20,6);
BEGIN
  -- Solo actuamos cuando el log viene "ok=true"
  IF NEW.ok IS DISTINCT FROM TRUE THEN
    RETURN NEW;
  END IF;

  -- Debe ser un estado que aplica saldos
  SELECT aplica_saldos INTO v_aplica
  FROM transfer_estado_catalogo
  WHERE est_code = NEW.est_code;

  IF COALESCE(v_aplica, FALSE) = FALSE THEN
    RETURN NEW;
  END IF;

  -- Trae datos de la transferencia
  SELECT t.cli_origen_id, t.cli_destino_id, t.act_id, t.monto
    INTO v_origen, v_destino, v_act, v_monto
  FROM transferencias t
  WHERE t.tra_id = NEW.tra_id;

  -- Evita doble aplicación
  IF EXISTS (
    SELECT 1 FROM transferencias
    WHERE tra_id = NEW.tra_id AND estado_actual = 'aplicada'
  ) THEN
    -- deja evidencia (ok=false => no re-dispara aplicación)
    INSERT INTO transferencias_log (tra_id, ok, est_code, error_code, error_msg, detalle)
    VALUES (NEW.tra_id, FALSE, 'ALREADY_APPL', 'ALREADY_APPLIED', 'Transferencia ya aplicada', NULL);
    RETURN NEW;
  END IF;

  -- Asegura que existan cuentas (COIN u otro activo)
  INSERT INTO cuentas (cli_id, act_id, saldo, estado)
  VALUES (v_origen, v_act, 0, 'activa')
  ON CONFLICT (cli_id, act_id) DO NOTHING;

  INSERT INTO cuentas (cli_id, act_id, saldo, estado)
  VALUES (v_destino, v_act, 0, 'activa')
  ON CONFLICT (cli_id, act_id) DO NOTHING;

  -- Lock filas de cuentas en orden estable para evitar deadlocks
  IF v_origen < v_destino THEN
    SELECT cta_id, saldo INTO v_cta_origen, v_saldo_origen
    FROM cuentas
    WHERE cli_id = v_origen AND act_id = v_act
    FOR UPDATE;

    SELECT cta_id INTO v_cta_destino
    FROM cuentas
    WHERE cli_id = v_destino AND act_id = v_act
    FOR UPDATE;
  ELSE
    SELECT cta_id INTO v_cta_destino
    FROM cuentas
    WHERE cli_id = v_destino AND act_id = v_act
    FOR UPDATE;

    SELECT cta_id, saldo INTO v_cta_origen, v_saldo_origen
    FROM cuentas
    WHERE cli_id = v_origen AND act_id = v_act
    FOR UPDATE;
  END IF;

  -- Validación saldo
  IF v_saldo_origen < v_monto THEN
    UPDATE transferencias
    SET estado_actual = 'fallida',
        updated_at = now()
    WHERE tra_id = NEW.tra_id;

    INSERT INTO transferencias_log (tra_id, ok, est_code, error_code, error_msg, detalle)
    VALUES (
      NEW.tra_id,
      FALSE,
      'BAL_INSUF',
      'INSUFFICIENT_FUNDS',
      'Saldo insuficiente para aplicar transferencia',
      jsonb_build_object('saldo_origen', v_saldo_origen, 'monto', v_monto)
    );

    RETURN NEW;
  END IF;

  -- Aplica débitos/créditos
  UPDATE cuentas
  SET saldo = saldo - v_monto,
      updated_at = now()
  WHERE cta_id = v_cta_origen;

  UPDATE cuentas
  SET saldo = saldo + v_monto,
      updated_at = now()
  WHERE cta_id = v_cta_destino;

  -- Marca transferencia como aplicada
  UPDATE transferencias
  SET estado_actual = 'aplicada',
      updated_at = now()
  WHERE tra_id = NEW.tra_id;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_transferencias_aplicar_al_confirmar ON transferencias_log;

CREATE TRIGGER trg_transferencias_aplicar_al_confirmar
AFTER INSERT ON transferencias_log
FOR EACH ROW
EXECUTE FUNCTION fn_transferencias_aplicar_al_confirmar();


-- =========================================
-- 3) OPCIONAL: “confirmar” fácil (vía función)
--    (esto NO es trigger, pero te deja 1 llamada simple)
--    SELECT confirmar_transferencia(tra_id);
-- =========================================
CREATE OR REPLACE FUNCTION confirmar_transferencia(p_tra_id BIGINT)
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
  INSERT INTO transferencias_log (tra_id, ok, est_code, error_code, error_msg, detalle)
  VALUES (p_tra_id, TRUE, 'CONFIRMED', NULL, NULL, NULL);
END;
$$;
