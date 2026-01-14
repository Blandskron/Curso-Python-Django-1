-- =========================================================
-- TRIGGER: al actualizar estado_actual -> 'validando'
-- crea automáticamente el log CONFIRMED (ok=true)
-- y eso activa el trigger existente que mueve saldos
-- =========================================================

CREATE OR REPLACE FUNCTION fn_transferencias_autoconfirmar_por_estado()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  -- Solo cuando pasa a 'validando' (evento de confirmación)
  IF (TG_OP = 'UPDATE')
     AND (NEW.estado_actual = 'validando')
     AND (OLD.estado_actual IS DISTINCT FROM NEW.estado_actual)
  THEN
    -- evita duplicar confirmaciones
    IF NOT EXISTS (
      SELECT 1
      FROM transferencias_log
      WHERE tra_id = NEW.tra_id
        AND ok = TRUE
        AND est_code = 'CONFIRMED'
    ) THEN
      INSERT INTO transferencias_log (tra_id, ok, est_code)
      VALUES (NEW.tra_id, TRUE, 'CONFIRMED');
    END IF;
  END IF;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_transferencias_autoconfirmar_por_estado ON transferencias;

CREATE TRIGGER trg_transferencias_autoconfirmar_por_estado
AFTER UPDATE OF estado_actual ON transferencias
FOR EACH ROW
EXECUTE FUNCTION fn_transferencias_autoconfirmar_por_estado();
