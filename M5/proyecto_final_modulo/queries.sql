/* ============================================================================
   queries.sql — Consultas típicas de e-commerce
============================================================================ */

-- 1) Listar todos los productos junto a su categoría
SELECT
  p.product_id,
  p.name AS producto,
  c.name AS categoria,
  p.price,
  p.active
FROM products p
JOIN categories c ON c.category_id = p.category_id
ORDER BY c.name, p.name;

-- 2) Buscar productos por nombre (ejemplo: contiene 'sql')
-- Cambia el término según lo que te pidan
SELECT
  p.product_id,
  p.name,
  p.price
FROM products p
WHERE LOWER(p.name) LIKE '%sql%'
ORDER BY p.name;

-- 3) Filtrar productos por categoría (ejemplo: Tecnología)
SELECT
  p.product_id,
  p.name,
  p.price
FROM products p
JOIN categories c ON c.category_id = p.category_id
WHERE c.name = 'Tecnología'
ORDER BY p.name;

-- 4) Mostrar los productos asociados a un pedido (ejemplo: pedido más reciente)
SELECT
  oi.order_id,
  p.name AS producto,
  oi.quantity,
  oi.unit_price,
  (oi.quantity * oi.unit_price) AS subtotal
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
WHERE oi.order_id = (SELECT MAX(order_id) FROM orders)
ORDER BY p.name;

-- 5) Calcular el total de un pedido (ejemplo: pedido más reciente)
SELECT
  o.order_id,
  u.email AS cliente,
  SUM(oi.quantity * oi.unit_price) AS total_pedido
FROM orders o
JOIN users u ON u.user_id = o.user_id
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.order_id = (SELECT MAX(order_id) FROM orders)
GROUP BY o.order_id, u.email;

-- 6) Identificar productos con stock bajo (quantity < low_stock_threshold)
SELECT
  p.product_id,
  p.name AS producto,
  s.quantity,
  s.low_stock_threshold
FROM stock s
JOIN products p ON p.product_id = s.product_id
WHERE s.quantity < s.low_stock_threshold
ORDER BY (s.low_stock_threshold - s.quantity) DESC, p.name;
