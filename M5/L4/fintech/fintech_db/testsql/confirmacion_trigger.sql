-- =====================================================
-- 1) VERIFICAR que el trigger aplicador EXISTE
-- =====================================================
SELECT trigger_name, event_object_table, action_timing, event_manipulation, action_statement
FROM information_schema.triggers
WHERE event_object_table IN ('transferencias_log','transferencias')
ORDER BY event_object_table, trigger_name;

-- =====================================================
-- 2) VERIFICAR que CONFIRMED aplica_saldos = true
-- =====================================================
SELECT est_code, aplica_saldos
FROM transfer_estado_catalogo
WHERE est_code = 'CONFIRMED';

-- =====================================================
-- 3) FIX: re-crear el trigger aplicador (si faltaba)
-- (usa la función que ya te di antes: fn_transferencias_aplicar_al_confirmar)
-- =====================================================
DROP TRIGGER IF EXISTS trg_transferencias_aplicar_al_confirmar ON transferencias_log;

CREATE TRIGGER trg_transferencias_aplicar_al_confirmar
AFTER INSERT ON transferencias_log
FOR EACH ROW
EXECUTE FUNCTION fn_transferencias_aplicar_al_confirmar();

-- =====================================================
-- 4) RE-INTENTO: forzar aplicación para una transferencia de prueba
-- (cambia 12 por el tra_id real del test)
-- =====================================================
INSERT INTO transferencias_log (tra_id, ok, est_code)
VALUES (12, TRUE, 'CONFIRMED');

-- =====================================================
-- 5) VALIDAR:
-- - transferencia queda 'aplicada'
-- - saldos cambian
-- =====================================================
SELECT tra_id, cli_origen_id, cli_destino_id, monto, estado_actual, updated_at
FROM transferencias
WHERE tra_id = 12;

SELECT c.cli_id, c.saldo, c.updated_at
FROM cuentas c
WHERE c.act_id = 1
  AND c.cli_id IN (
    SELECT cli_origen_id FROM transferencias WHERE tra_id = 12
    UNION
    SELECT cli_destino_id FROM transferencias WHERE tra_id = 12
  )
ORDER BY c.cli_id;

SELECT log_id, tra_id, ok, est_code, error_code, error_msg, created_at
FROM transferencias_log
WHERE tra_id = 12
ORDER BY log_id;
