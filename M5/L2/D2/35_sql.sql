SELECT t.client_id, t.total_spent
FROM (
  SELECT o.client_id,
         SUM(oi.quantity * oi.unit_price) AS total_spent
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.order_id
  GROUP BY o.client_id
) t
ORDER BY t.total_spent DESC;