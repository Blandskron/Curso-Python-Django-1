SELECT c.client_id, c.name,
       SUM(oi.quantity * oi.unit_price) AS total_spent
FROM org.clients c
JOIN org.orders o ON o.client_id = c.client_id
JOIN org.order_items oi ON oi.order_id = o.order_id
GROUP BY c.client_id, c.name
ORDER BY total_spent DESC
LIMIT 10;