INSERT INTO transferencias (cli_origen_id, cli_destino_id, act_id, monto, estado_actual, referencia, nota)
VALUES (11, 12, 1, 100, 'creada', 'TRX_AUTO_0001', 'Auto confirm al insertar');

-- Debe quedar aplicada (si tus triggers aplicadores están OK)
SELECT tra_id, estado_actual
FROM transferencias
WHERE referencia = 'TRX_AUTO_0001';

-- Debe existir log CONFIRMED
SELECT *
FROM transferencias_log
WHERE tra_id = (SELECT tra_id FROM transferencias WHERE referencia='TRX_AUTO_0001')
ORDER BY log_id;

-- Ver saldos de 11 y 12
SELECT cli_id, saldo
FROM cuentas
WHERE act_id=1 AND cli_id IN (11,12)
ORDER BY cli_id;
