-- ============================
-- 10 TRANSFERENCIAS DE PRUEBA (SERIE 3)
-- (si ya tienes el trigger AFTER INSERT que autoconfirma,
--  entonces se aplicarán automáticamente al insertarse)
-- ============================

INSERT INTO transferencias (
  cli_origen_id,
  cli_destino_id,
  act_id,
  monto,
  estado_actual,
  referencia,
  nota
) VALUES
-- 21
(1,  3,  1,  210,  'creada', 'TRX_0021', 'Pago prueba 21'),
-- 22
(2,  4,  1,  990,  'creada', 'TRX_0022', 'Pago prueba 22'),
-- 23
(3,  5,  1,  125,  'creada', 'TRX_0023', 'Pago prueba 23'),
-- 24
(4,  6,  1,  700,  'creada', 'TRX_0024', 'Pago prueba 24'),
-- 25
(5,  7,  1,  450,  'creada', 'TRX_0025', 'Pago prueba 25'),
-- 26
(6,  8,  1,  333,  'creada', 'TRX_0026', 'Pago prueba 26'),
-- 27
(7,  9,  1,  875,  'creada', 'TRX_0027', 'Pago prueba 27'),
-- 28
(8, 10,  1,  160,  'creada', 'TRX_0028', 'Pago prueba 28'),
-- 29
(9, 11,  1,  540,  'creada', 'TRX_0029', 'Pago prueba 29'),
-- 30
(10,12,  1,  260,  'creada', 'TRX_0030', 'Pago prueba 30');

-- ============================
-- VALIDACIÓN (transferencias)
-- ============================

SELECT tra_id, cli_origen_id, cli_destino_id, monto, estado_actual
FROM transferencias
WHERE referencia BETWEEN 'TRX_0021' AND 'TRX_0030'
ORDER BY tra_id;

-- ============================
-- VALIDACIÓN (log + saldos)
-- ============================

-- Log de estas transferencias
SELECT l.log_id, l.tra_id, l.ok, l.est_code, l.error_code, l.error_msg, l.created_at
FROM transferencias_log l
JOIN transferencias t ON t.tra_id = l.tra_id
WHERE t.referencia BETWEEN 'TRX_0021' AND 'TRX_0030'
ORDER BY l.log_id;

-- Saldos involucrados (clientes 1..12)
SELECT c.cli_id, cl.nombre, c.saldo, c.updated_at
FROM cuentas c
JOIN clientes cl ON cl.cli_id = c.cli_id
WHERE c.act_id = 1 AND c.cli_id BETWEEN 1 AND 12
ORDER BY c.cli_id;
