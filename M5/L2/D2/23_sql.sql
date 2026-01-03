SELECT o.order_id, o.order_date, o.status, c.name AS client
FROM orders o
JOIN clients c ON c.client_id = o.client_id;