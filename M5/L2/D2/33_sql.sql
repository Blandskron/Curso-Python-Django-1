SELECT o.order_id, o.order_date
FROM orders o
WHERE EXISTS (
  SELECT 1
  FROM order_items oi
  WHERE oi.order_id = o.order_id
);