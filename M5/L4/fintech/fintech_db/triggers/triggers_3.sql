-- =========================================================
-- TRIGGER: auto-confirmar al INSERT de transferencias
-- - Si llega en estado 'creada' (o NULL), inserta log CONFIRMED
-- - Eso dispara el trigger existente en transferencias_log
--   (fn_transferencias_aplicar_al_confirmar) y mueve saldos
-- =========================================================

CREATE OR REPLACE FUNCTION fn_transferencias_autoconfirmar_al_insert()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
  -- Si por algún motivo viene null, lo tratamos como 'creada'
  IF NEW.estado_actual IS NULL THEN
    NEW.estado_actual := 'creada';
  END IF;

  -- Auto-confirmar SOLO cuando está 'creada'
  IF NEW.estado_actual = 'creada' THEN
    -- Evita duplicar por si reinsertas/repites lógica
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

DROP TRIGGER IF EXISTS trg_transferencias_autoconfirmar_al_insert ON transferencias;

CREATE TRIGGER trg_transferencias_autoconfirmar_al_insert
AFTER INSERT ON transferencias
FOR EACH ROW
EXECUTE FUNCTION fn_transferencias_autoconfirmar_al_insert();
