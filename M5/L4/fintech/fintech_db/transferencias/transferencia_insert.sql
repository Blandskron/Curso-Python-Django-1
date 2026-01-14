-- ============================
-- 10 TRANSFERENCIAS DE PRUEBA
-- (solo se insertan, NO aplican saldo aún)
-- Para aplicar saldo debes CONFIRMARLAS después
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
-- 1
(1,  2,  1,  500,  'creada', 'TRX_0001', 'Pago prueba 1'),
-- 2
(2,  3,  1, 1200,  'creada', 'TRX_0002', 'Pago prueba 2'),
-- 3
(3,  4,  1,  300,  'creada', 'TRX_0003', 'Pago prueba 3'),
-- 4
(4,  5,  1, 2500,  'creada', 'TRX_0004', 'Pago prueba 4'),
-- 5
(5,  6,  1,  750,  'creada', 'TRX_0005', 'Pago prueba 5'),
-- 6
(6,  7,  1,  900,  'creada', 'TRX_0006', 'Pago prueba 6'),
-- 7
(7,  8,  1, 1500,  'creada', 'TRX_0007', 'Pago prueba 7'),
-- 8
(8,  9,  1,  200,  'creada', 'TRX_0008', 'Pago prueba 8'),
-- 9
(9, 10,  1, 1800,  'creada', 'TRX_0009', 'Pago prueba 9'),
-- 10
(10,11, 1,  400,  'creada', 'TRX_0010', 'Pago prueba 10');

-- ============================
-- VALIDACIÓN
-- ============================

SELECT tra_id, cli_origen_id, cli_destino_id, monto, estado_actual
FROM transferencias
ORDER BY tra_id;
