-- crea una transferencia nueva
INSERT INTO transferencias (cli_origen_id, cli_destino_id, act_id, monto, estado_actual, referencia)
VALUES (1, 2, 1, 111, 'creada', 'TRX_TEST_AUTO');

-- mira su id
SELECT tra_id, estado_actual FROM transferencias WHERE referencia='TRX_TEST_AUTO';

-- confirma con UPDATE (sin insertar log)
UPDATE transferencias
SET estado_actual='validando'
WHERE referencia='TRX_TEST_AUTO';

-- valida estado y log
SELECT tra_id, estado_actual FROM transferencias WHERE referencia='TRX_TEST_AUTO';
SELECT * FROM transferencias_log WHERE tra_id = (SELECT tra_id FROM transferencias WHERE referencia='TRX_TEST_AUTO');
