-- ============================
-- INSERT DE 20 CLIENTES
-- Al insertarse:
-- - Se dispara el trigger
-- - Se crea automáticamente su cuenta
-- - Saldo inicial = 10000
-- ============================

INSERT INTO clientes (nombre, email, estado) VALUES
('Cliente 01', 'cliente01@fintech.local', 'activo'),
('Cliente 02', 'cliente02@fintech.local', 'activo'),
('Cliente 03', 'cliente03@fintech.local', 'activo'),
('Cliente 04', 'cliente04@fintech.local', 'activo'),
('Cliente 05', 'cliente05@fintech.local', 'activo'),
('Cliente 06', 'cliente06@fintech.local', 'activo'),
('Cliente 07', 'cliente07@fintech.local', 'activo'),
('Cliente 08', 'cliente08@fintech.local', 'activo'),
('Cliente 09', 'cliente09@fintech.local', 'activo'),
('Cliente 10', 'cliente10@fintech.local', 'activo'),
('Cliente 11', 'cliente11@fintech.local', 'activo'),
('Cliente 12', 'cliente12@fintech.local', 'activo'),
('Cliente 13', 'cliente13@fintech.local', 'activo'),
('Cliente 14', 'cliente14@fintech.local', 'activo'),
('Cliente 15', 'cliente15@fintech.local', 'activo'),
('Cliente 16', 'cliente16@fintech.local', 'activo'),
('Cliente 17', 'cliente17@fintech.local', 'activo'),
('Cliente 18', 'cliente18@fintech.local', 'activo'),
('Cliente 19', 'cliente19@fintech.local', 'activo'),
('Cliente 20', 'cliente20@fintech.local', 'activo');

-- ============================
-- VALIDACIÓN RÁPIDA
-- ============================

-- Ver clientes
SELECT cli_id, nombre, email FROM clientes ORDER BY cli_id;

-- Ver cuentas creadas automáticamente (todas con saldo 10000)
SELECT c.cli_id, cl.nombre, a.codigo AS activo, c.saldo
FROM cuentas c
JOIN clientes cl ON cl.cli_id = c.cli_id
JOIN activos a ON a.act_id = c.act_id
ORDER BY c.cli_id;
