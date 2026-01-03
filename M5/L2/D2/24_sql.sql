SELECT c.client_id, c.name, o.order_id
FROM clients c
LEFT JOIN orders o ON o.client_id = c.client_id
ORDER BY c.client_id;