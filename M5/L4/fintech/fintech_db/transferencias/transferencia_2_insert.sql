-- ============================
-- 10 TRANSFERENCIAS DE PRUEBA (SERIE 2)
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
-- 11
(11, 12, 1,  650,  'creada', 'TRX_0011', 'Pago prueba 11'),
-- 12
(12, 13, 1,  980,  'creada', 'TRX_0012', 'Pago prueba 12'),
-- 13
(13, 14, 1,  420,  'creada', 'TRX_0013', 'Pago prueba 13'),
-- 14
(14, 15, 1, 3100,  'creada', 'TRX_0014', 'Pago prueba 14'),
-- 15
(15, 16, 1,  275,  'creada', 'TRX_0015', 'Pago prueba 15'),
-- 16
(16, 17, 1, 1400,  'creada', 'TRX_0016', 'Pago prueba 16'),
-- 17
(17, 18, 1,  860,  'creada', 'TRX_0017', 'Pago prueba 17'),
-- 18
(18, 19, 1,  510,  'creada', 'TRX_0018', 'Pago prueba 18'),
-- 19
(19, 20, 1, 1950,  'creada', 'TRX_0019', 'Pago prueba 19'),
-- 20
(20,  1, 1,  330,  'creada', 'TRX_0020', 'Pago prueba 20');

-- ============================
-- VALIDACIÓN
-- ============================

SELECT tra_id, cli_origen_id, cli_destino_id, monto, estado_actual
FROM transferencias
WHERE referencia BETWEEN 'TRX_0011' AND 'TRX_0020'
ORDER BY tra_id;
