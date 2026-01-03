SELECT c.client_id, c.name, o.order_id
FROM clients c
FULL OUTER JOIN orders o ON o.client_id = c.client_id;