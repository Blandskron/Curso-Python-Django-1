SELECT o.order_id, c.name AS client,
       SUM(oi.quantity * oi.unit_price) AS total
FROM orders o
JOIN clients c ON c.client_id = o.client_id
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id, c.name
ORDER BY total DESC;