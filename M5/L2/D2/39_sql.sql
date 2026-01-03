SELECT c.client_id, c.name,
       SUM(oi.quantity * oi.unit_price) AS total_spent
FROM clients c
JOIN orders o ON o.client_id = c.client_id
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.client_id, c.name
HAVING SUM(oi.quantity * oi.unit_price) > 1000000
ORDER BY total_spent DESC;