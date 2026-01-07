-- ============================================================
-- DATASET DE PRUEBA (PostgreSQL) PARA TESTEAR TODAS LAS QUERIES
-- Tablas: clients, products, orders, order_items, payments
-- Incluye datos con: NULLs, duplicados, clientes sin pedidos,
-- pedidos sin ítems, productos inactivos, fechas variadas, etc.
-- ============================================================

BEGIN;

-- Limpieza (por si ya existen)
DROP TABLE IF EXISTS payments CASCADE;
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS clients CASCADE;

-- ======================
-- 1) TABLAS
-- ======================

CREATE TABLE clients (
  client_id   INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name        VARCHAR(120) NOT NULL,
  email       VARCHAR(180) NULL,
  country     VARCHAR(80)  NOT NULL,
  created_at  TIMESTAMP    NOT NULL DEFAULT now()
);

CREATE TABLE products (
  product_id  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  sku         VARCHAR(40)  NOT NULL UNIQUE,
  name        VARCHAR(160) NOT NULL,
  category    VARCHAR(80)  NOT NULL,
  price       NUMERIC(12,2) NOT NULL CHECK (price >= 0),
  is_active   BOOLEAN      NOT NULL DEFAULT TRUE,
  created_at  TIMESTAMP    NOT NULL DEFAULT now()
);

CREATE TABLE orders (
  order_id    INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  client_id   INT NOT NULL REFERENCES clients(client_id) ON DELETE RESTRICT,
  status      VARCHAR(20) NOT NULL CHECK (status IN ('PENDING','PAID','CANCELLED','REFUNDED')),
  order_date  DATE NOT NULL
);

CREATE TABLE order_items (
  order_item_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  order_id      INT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
  product_id    INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
  quantity      INT NOT NULL CHECK (quantity > 0),
  unit_price    NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0)
);

CREATE TABLE payments (
  payment_id  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  order_id    INT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
  amount      NUMERIC(12,2) NOT NULL CHECK (amount >= 0),
  method      VARCHAR(20) NOT NULL CHECK (method IN ('CARD','TRANSFER','CASH','CRYPTO')),
  status      VARCHAR(20) NOT NULL CHECK (status IN ('PENDING','PAID','FAILED','REFUNDED')),
  paid_at     TIMESTAMP NOT NULL
);

-- Índices útiles (no obligatorios)
CREATE INDEX idx_orders_client_id     ON orders(client_id);
CREATE INDEX idx_orders_order_date    ON orders(order_date);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_payments_paid_at     ON payments(paid_at);

-- ======================
-- 2) INSERTS
-- ======================

-- CLIENTS (incluye NULL email, países duplicados, nombres con "spa")
INSERT INTO clients (name, email, country, created_at) VALUES
('Acme SpA',                  'contacto@acme.cl',          'Chile',      now() - interval '400 days'),
('Beta Ltda',                 NULL,                         'Chile',      now() - interval '200 days'),
('Gamma Corp',                'sales@gamma.com',            'USA',        now() - interval '90 days'),
('Delta SpA',                 'info@delta.cl',              'Chile',      now() - interval '35 days'),
('Epsilon SAS',               'hola@epsilon.co',            'Colombia',   now() - interval '20 days'),
('Zeta GmbH',                 'kontakt@zeta.de',            'Germany',    now() - interval '12 days'),
('Omega SpA',                 NULL,                         'Peru',       now() - interval '5 days'),
('NoOrders Inc',              'noorders@x.com',             'USA',        now() - interval '2 days');

-- PRODUCTS (incluye inactivos y rangos de precio para tier LOW/MID/HIGH)
-- Nota: product_id 10 existe para tu query #18
INSERT INTO products (sku, name, category, price, is_active, created_at) VALUES
('SKU-0001', 'Antivirus Basic',            'SOFTWARE',  7990.00,  TRUE,  now() - interval '180 days'),
('SKU-0002', 'Antivirus Pro',              'SOFTWARE', 19990.00,  TRUE,  now() - interval '170 days'),
('SKU-0003', 'Cloud Storage 1TB',          'SOFTWARE', 29990.00,  TRUE,  now() - interval '160 days'),
('SKU-0004', 'Laptop 14"',                 'HARDWARE', 549990.00, TRUE,  now() - interval '150 days'),
('SKU-0005', 'Mouse Wireless',             'HARDWARE', 14990.00,  TRUE,  now() - interval '140 days'),
('SKU-0006', 'Keyboard Mechanical',        'HARDWARE', 49990.00,  TRUE,  now() - interval '130 days'),
('SKU-0007', 'Consulting Hour',            'SERVICES',  9000.00,  TRUE,  now() - interval '120 days'),
('SKU-0008', 'Setup Service',              'SERVICES', 35000.00,  FALSE, now() - interval '110 days'),
('SKU-0009', 'Premium Support Monthly',    'SERVICES',  120000.00,TRUE,  now() - interval '100 days'),
('SKU-0010', 'ERP License Annual',         'SOFTWARE', 1250000.00,TRUE,  now() - interval '95 days'),
('SKU-0011', 'Old Discontinued License',   'SOFTWARE',  15000.00, FALSE, now() - interval '90 days'),
('SKU-0012', 'Gift Card',                  'OTHER',     10000.00, TRUE,  now() - interval '80 days');

-- ORDERS
-- Objetivos:
-- - status variados (PENDING/PAID/CANCELLED/REFUNDED)
-- - order_date dentro de 2025 para BETWEEN (query #10)
-- - varios pedidos PAID en últimos 30 días para query #8
-- - al menos un pedido SIN items para NOT EXISTS (query #34)
-- - un cliente con >5 pedidos para query #32 (usamos client_id=1)
INSERT INTO orders (client_id, status, order_date) VALUES
-- Cliente 1 (Acme SpA) -> 6 pedidos (cumple >5)
(1, 'PAID',      CURRENT_DATE - 5),
(1, 'PAID',      CURRENT_DATE - 12),
(1, 'PENDING',   CURRENT_DATE - 40),
(1, 'CANCELLED', DATE '2025-06-15'),
(1, 'PAID',      DATE '2025-03-20'),
(1, 'REFUNDED',  DATE '2025-11-05'),

-- Cliente 2 (Beta Ltda)
(2, 'PAID',      CURRENT_DATE - 2),
(2, 'CANCELLED', CURRENT_DATE - 25),
(2, 'PENDING',   DATE '2025-01-10'),

-- Cliente 3 (Gamma Corp)
(3, 'PAID',      DATE '2025-12-20'),
(3, 'PAID',      DATE '2025-02-02'),

-- Cliente 4 (Delta SpA)
(4, 'PENDING',   CURRENT_DATE - 1),

-- Cliente 5 (Epsilon SAS) -> pedido sin ítems (para NOT EXISTS)
(5, 'PAID',      CURRENT_DATE - 3),

-- Cliente 6 (Zeta GmbH)
(6, 'CANCELLED', DATE '2025-07-07'),

-- Cliente 7 (Omega SpA)
(7, 'PAID',      DATE '2024-12-31');

-- ORDER_ITEMS
-- Reglas:
-- - varios productos SOFTWARE para query #27
-- - totales grandes para HAVING > 1.000.000 (query #39)
-- - algunos pedidos con ítems, y dejamos 1 pedido sin ítems (el de client_id=5)
-- NOTA: order_id se asigna en orden, así que quedan:
-- 1..14 en el mismo orden de los inserts de orders
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
-- Order 1 (PAID, reciente) - cliente 1
(1, 2, 1, 19990.00),
(1, 5, 2, 14990.00),

-- Order 2 (PAID, reciente) - cliente 1
(2, 3, 1, 29990.00),
(2, 7, 3, 9000.00),

-- Order 3 (PENDING) - cliente 1
(3, 1, 2, 7990.00),

-- Order 4 (CANCELLED 2025) - cliente 1
(4, 5, 1, 14990.00),
(4, 6, 1, 49990.00),

-- Order 5 (PAID 2025) - cliente 1 (metemos alto total para HAVING)
(5, 10, 1, 1250000.00),  -- ERP Annual
(5, 9,  2, 120000.00),   -- Premium Support

-- Order 6 (REFUNDED 2025) - cliente 1
(6, 2, 2, 19990.00),

-- Order 7 (PAID, reciente) - cliente 2
(7, 4, 1, 549990.00),
(7, 5, 1, 14990.00),

-- Order 8 (CANCELLED, reciente) - cliente 2
(8, 3, 1, 29990.00),

-- Order 9 (PENDING 2025) - cliente 2
(9, 12, 5, 10000.00),

-- Order 10 (PAID 2025) - cliente 3
(10, 2, 1, 19990.00),
(10, 3, 2, 29990.00),

-- Order 11 (PAID 2025) - cliente 3
(11, 6, 1, 49990.00),

-- Order 12 (PENDING, reciente) - cliente 4
(12, 7, 2, 9000.00),

-- Order 13 (PAID, reciente) - cliente 5
-- (SIN ITEMS a propósito para query #34)

-- Order 14 (CANCELLED 2025) - cliente 6
(14, 1, 1, 7990.00);

-- PAYMENTS
-- Reglas:
-- - paid_at en últimos 7 días para query #15
-- - métodos/estados variados
-- - pagos asociados a pedidos (JOIN query #30)
INSERT INTO payments (order_id, amount, method, status, paid_at) VALUES
(1,  49970.00, 'CARD',     'PAID',     now() - interval '4 days'),
(2,  56990.00, 'TRANSFER', 'PAID',     now() - interval '10 days'), -- fuera de 7 días
(5, 1490000.00,'TRANSFER', 'PAID',     now() - interval '2 days'),
(6,  39980.00, 'CARD',     'REFUNDED', now() - interval '1 days'),
(7, 564980.00, 'CARD',     'PAID',     now() - interval '6 days'),
(8,  29990.00, 'CARD',     'FAILED',   now() - interval '3 days'),
(10, 79970.00, 'CASH',     'PAID',     DATE '2025-12-21'::timestamp),
(13, 10000.00, 'CRYPTO',   'PENDING',  now() - interval '12 hours');

COMMIT;

-- ============================================================
-- QUICK CHECKS (opcionales)
-- SELECT COUNT(*) FROM clients;
-- SELECT COUNT(*) FROM products;
-- SELECT COUNT(*) FROM orders;
-- SELECT COUNT(*) FROM order_items;
-- SELECT COUNT(*) FROM payments;
-- ============================================================
