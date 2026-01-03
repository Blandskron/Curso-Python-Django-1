UPDATE order_items oi
SET unit_price = p.price
FROM products p
WHERE p.product_id = oi.product_id
  AND oi.order_id = 10;