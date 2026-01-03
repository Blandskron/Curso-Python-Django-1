/* ============================================================================
   seed.sql — Datos de ejemplo (E-commerce)
============================================================================ */

-- =========================
-- CATEGORIES (>=3)
-- =========================
INSERT INTO categories (name, description) VALUES
('Tecnología', 'Dispositivos y accesorios'),
('Hogar', 'Productos para el hogar'),
('Libros', 'Lecturas y formación');

-- =========================
-- USERS (>=5, incluye 1 ADMIN)
-- =========================
INSERT INTO users (name, email, role) VALUES
('Ana Pérez',   'ana@shop.cl',   'CUSTOMER'),
('Luis Soto',   'luis@shop.cl',  'CUSTOMER'),
('Paula Rojas', 'paula@shop.cl', 'CUSTOMER'),
('Diego Mella', 'diego@shop.cl', 'CUSTOMER'),
('Admin',       'admin@shop.cl', 'ADMIN');

-- =========================
-- PRODUCTS (>=10) asociados a categorías
-- =========================
-- Tecnología (4)
INSERT INTO products (category_id, name, description, price) VALUES
((SELECT category_id FROM categories WHERE name='Tecnología'), 'Mouse inalámbrico', 'Mouse 2.4G', 12990),
((SELECT category_id FROM categories WHERE name='Tecnología'), 'Teclado mecánico', 'Switches táctiles', 45990),
((SELECT category_id FROM categories WHERE name='Tecnología'), 'Audífonos Bluetooth', 'Cancelación de ruido', 39990),
((SELECT category_id FROM categories WHERE name='Tecnología'), 'Webcam HD', '1080p', 24990);

-- Hogar (3)
INSERT INTO products (category_id, name, description, price) VALUES
((SELECT category_id FROM categories WHERE name='Hogar'), 'Hervidor eléctrico', '1.7L', 17990),
((SELECT category_id FROM categories WHERE name='Hogar'), 'Lámpara escritorio', 'LED regulable', 14990),
((SELECT category_id FROM categories WHERE name='Hogar'), 'Set organizadores', 'Cajas apilables', 9990);

-- Libros (3)
INSERT INTO products (category_id, name, description, price) VALUES
((SELECT category_id FROM categories WHERE name='Libros'), 'SQL desde cero', 'Guía práctica', 19990),
((SELECT category_id FROM categories WHERE name='Libros'), 'PostgreSQL avanzado', 'Optimización y diseño', 24990),
((SELECT category_id FROM categories WHERE name='Libros'), 'Diseño de bases de datos', 'Modelo ER y normalización', 22990);

-- =========================
-- STOCK (para cada producto)
-- =========================
INSERT INTO stock (product_id, quantity, low_stock_threshold)
SELECT product_id,
       CASE
         WHEN name IN ('Teclado mecánico', 'PostgreSQL avanzado') THEN 4  -- bajo stock intencional
         WHEN name IN ('Webcam HD', 'Set organizadores') THEN 6
         ELSE 12
       END AS quantity,
       5 AS low_stock_threshold
FROM products;

-- =========================
-- ORDERS (>=3) + ITEMS
-- =========================

-- Pedido 1 (Ana) - CREATED
INSERT INTO orders (user_id, status)
VALUES ((SELECT user_id FROM users WHERE email='ana@shop.cl'), 'CREATED');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
((SELECT MAX(order_id) FROM orders), (SELECT product_id FROM products WHERE name='Mouse inalámbrico'), 1, (SELECT price FROM products WHERE name='Mouse inalámbrico')),
((SELECT MAX(order_id) FROM orders), (SELECT product_id FROM products WHERE name='SQL desde cero'), 1, (SELECT price FROM products WHERE name='SQL desde cero'));

-- Pedido 2 (Luis) - PAID
INSERT INTO orders (user_id, status)
VALUES ((SELECT user_id FROM users WHERE email='luis@shop.cl'), 'PAID');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
((SELECT MAX(order_id) FROM orders), (SELECT product_id FROM products WHERE name='Teclado mecánico'), 1, (SELECT price FROM products WHERE name='Teclado mecánico')),
((SELECT MAX(order_id) FROM orders), (SELECT product_id FROM products WHERE name='Lámpara escritorio'), 2, (SELECT price FROM products WHERE name='Lámpara escritorio'));

-- Pedido 3 (Paula) - CREATED
INSERT INTO orders (user_id, status)
VALUES ((SELECT user_id FROM users WHERE email='paula@shop.cl'), 'CREATED');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
((SELECT MAX(order_id) FROM orders), (SELECT product_id FROM products WHERE name='Audífonos Bluetooth'), 1, (SELECT price FROM products WHERE name='Audífonos Bluetooth')),
((SELECT MAX(order_id) FROM orders), (SELECT product_id FROM products WHERE name='Hervidor eléctrico'), 1, (SELECT price FROM products WHERE name='Hervidor eléctrico')),
((SELECT MAX(order_id) FROM orders), (SELECT product_id FROM products WHERE name='Set organizadores'), 3, (SELECT price FROM products WHERE name='Set organizadores'));
