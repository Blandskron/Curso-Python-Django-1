SELECT c.client_id, c.name
FROM clients c
LEFT JOIN orders o ON o.client_id = c.client_id
WHERE o.order_id IS NULL;