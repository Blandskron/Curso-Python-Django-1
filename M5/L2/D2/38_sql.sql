SELECT AVG(t.total) AS avg_ticket
FROM (
  SELECT oi.order_id, SUM(oi.quantity * oi.unit_price) AS total
  FROM order_items oi
  GROUP BY oi.order_id
) t;