/* ============================================================================
   transaction.sql — Operación transaccional: registrar compra
   Motor recomendado: PostgreSQL
   Flujo:
   1) Crear pedido
   2) Agregar items
   3) Descontar stock
   4) Confirmar (COMMIT) o deshacer (ROLLBACK) si no hay stock
============================================================================ */

BEGIN;

-- Parámetros del ejemplo (ajusta):
-- Cliente: diego@shop.cl
-- Compra: 1 teclado mecánico + 2 SQL desde cero
-- Nota: Usamos CTEs para capturar el order_id creado.

-- 1) Crear pedido
WITH new_order AS (
  INSERT INTO orders (user_id, status)
  VALUES ((SELECT user_id FROM users WHERE email='diego@shop.cl'), 'CREATED')
  RETURNING order_id
),
items AS (
  -- 2) Definir items a comprar (producto, cantidad)
  SELECT
    (SELECT order_id FROM new_order) AS order_id,
    p.product_id,
    v.qty AS quantity,
    p.price AS unit_price
  FROM (VALUES
    ('Teclado mecánico', 1),
    ('SQL desde cero', 2)
  ) AS v(product_name, qty)
  JOIN products p ON p.name = v.product_name
),
lock_stock AS (
  -- 3) Bloquear stock de esos productos para evitar condiciones de carrera
  SELECT s.*
  FROM stock s
  JOIN items i ON i.product_id = s.product_id
  FOR UPDATE
),
check_stock AS (
  -- 4) Validar stock suficiente (si falla, abortamos manualmente con RAISE)
  SELECT
    COUNT(*) AS insufficient_count
  FROM lock_stock s
  JOIN items i ON i.product_id = s.product_id
  WHERE s.quantity < i.quantity
)
-- Insertar items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT order_id, product_id, quantity, unit_price
FROM items;

-- Validación: si hay falta de stock, hacemos ROLLBACK lanzando error
DO $$
DECLARE insufficient INT;
BEGIN
  SELECT
    COUNT(*)
  INTO insufficient
  FROM stock s
  JOIN order_items oi ON oi.product_id = s.product_id
  WHERE oi.order_id = (SELECT MAX(order_id) FROM orders)
    AND s.quantity < oi.quantity;

  IF insufficient > 0 THEN
    RAISE EXCEPTION 'Stock insuficiente para uno o más productos. Se revierte la compra.';
  END IF;
END $$;

-- 5) Descontar stock según items del pedido recién creado
UPDATE stock s
SET quantity = s.quantity - oi.quantity,
    updated_at = NOW()
FROM order_items oi
WHERE oi.order_id = (SELECT MAX(order_id) FROM orders)
  AND oi.product_id = s.product_id;

-- (Opcional) marcar pedido como PAID al finalizar compra
UPDATE orders
SET status = 'PAID'
WHERE order_id = (SELECT MAX(order_id) FROM orders);

COMMIT;

-- Verificación rápida:
-- SELECT * FROM orders ORDER BY order_id DESC LIMIT 1;
-- SELECT * FROM order_items WHERE order_id = (SELECT MAX(order_id) FROM orders);
-- SELECT p.name, s.quantity FROM stock s JOIN products p ON p.product_id = s.product_id ORDER BY p.name;
