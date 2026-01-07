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

INSERT INTO clients (name, email, country, created_at) VALUES
('Acme SpA',                  'contacto@acme.cl',          'Chile',      now() - interval '400 days'),
('Beta Ltda',                 NULL,                         'Chile',      now() - interval '200 days'),
('Gamma Corp',                'sales@gamma.com',            'USA',        now() - interval '90 days'),
('Delta SpA',                 'info@delta.cl',              'Chile',      now() - interval '35 days'),
('Epsilon SAS',               'hola@epsilon.co',            'Colombia',   now() - interval '20 days'),
('Zeta GmbH',                 'kontakt@zeta.de',            'Germany',    now() - interval '12 days'),
('Omega SpA',                 NULL,                         'Peru',       now() - interval '5 days'),
('NoOrders Inc',              'noorders@x.com',             'USA',        now() - interval '2 days');

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

INSERT INTO orders (client_id, status, order_date) VALUES
(1, 'PAID',      CURRENT_DATE - 5),
(1, 'PAID',      CURRENT_DATE - 12),
(1, 'PENDING',   CURRENT_DATE - 40),
(1, 'CANCELLED', DATE '2025-06-15'),
(1, 'PAID',      DATE '2025-03-20'),
(1, 'REFUNDED',  DATE '2025-11-05'),
(2, 'PAID',      CURRENT_DATE - 2),
(2, 'CANCELLED', CURRENT_DATE - 25),
(2, 'PENDING',   DATE '2025-01-10'),
(3, 'PAID',      DATE '2025-12-20'),
(3, 'PAID',      DATE '2025-02-02'),
(4, 'PENDING',   CURRENT_DATE - 1),
(5, 'PAID',      CURRENT_DATE - 3),
(6, 'CANCELLED', DATE '2025-07-07'),
(7, 'PAID',      DATE '2024-12-31');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 2, 1, 19990.00),
(1, 5, 2, 14990.00),
(2, 3, 1, 29990.00),
(2, 7, 3, 9000.00),
(3, 1, 2, 7990.00),
(4, 5, 1, 14990.00),
(4, 6, 1, 49990.00),
(5, 10, 1, 1250000.00),
(5, 9,  2, 120000.00),
(6, 2, 2, 19990.00),
(7, 4, 1, 549990.00),
(7, 5, 1, 14990.00),
(8, 3, 1, 29990.00),
(9, 12, 5, 10000.00),
(10, 2, 1, 19990.00),
(10, 3, 2, 29990.00),
(11, 6, 1, 49990.00),
(12, 7, 2, 9000.00),
(14, 1, 1, 7990.00);

INSERT INTO payments (order_id, amount, method, status, paid_at) VALUES
(1,  49970.00, 'CARD',     'PAID',     now() - interval '4 days'),
(2,  56990.00, 'TRANSFER', 'PAID',     now() - interval '10 days'),
(5, 1490000.00,'TRANSFER', 'PAID',     now() - interval '2 days'),
(6,  39980.00, 'CARD',     'REFUNDED', now() - interval '1 days'),
(7, 564980.00, 'CARD',     'PAID',     now() - interval '6 days'),
(8,  29990.00, 'CARD',     'FAILED',   now() - interval '3 days'),
(10, 79970.00, 'CASH',     'PAID',     DATE '2025-12-21'::timestamp),
(13, 10000.00, 'CRYPTO',   'PENDING',  now() - interval '12 hours');
