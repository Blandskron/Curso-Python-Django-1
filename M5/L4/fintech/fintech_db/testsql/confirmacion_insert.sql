-- 1) Confirmar transferencias (esto dispara el trigger y mueve saldos)
INSERT INTO transferencias_log (tra_id, ok, est_code)
VALUES
(1, TRUE, 'CONFIRMED'),
(3, TRUE, 'CONFIRMED'),
(4, TRUE, 'CONFIRMED'),
(5, TRUE, 'CONFIRMED'),
(6, TRUE, 'CONFIRMED'),
(7, TRUE, 'CONFIRMED'),
(8, TRUE, 'CONFIRMED');

-- 2) Ver log generado (incluye fallas si hubo saldo insuficiente, etc.)
SELECT log_id, tra_id, ok, est_code, error_code, error_msg, created_at
FROM transferencias_log
ORDER BY log_id;

-- 3) Ver transferencias ya aplicadas (estado_actual debería pasar a 'aplicada')
SELECT tra_id, cli_origen_id, cli_destino_id, monto, estado_actual, updated_at
FROM transferencias
WHERE tra_id IN (1,3,4,5,6,7,8)
ORDER BY tra_id;

-- 4) Ver saldos afectados (clientes 1..8)
SELECT c.cli_id, cl.nombre, c.saldo, c.updated_at
FROM cuentas c
JOIN clientes cl ON cl.cli_id = c.cli_id
WHERE c.act_id = 1 AND c.cli_id BETWEEN 1 AND 8
ORDER BY c.cli_id;
