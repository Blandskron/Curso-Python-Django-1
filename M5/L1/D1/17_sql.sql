SELECT o.order_id, c.name AS client, o.order_date, o.status
FROM org.orders o
JOIN org.clients c ON c.client_id = o.client_id
ORDER BY o.order_id DESC;