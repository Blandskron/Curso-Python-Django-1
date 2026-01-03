SELECT c.client_id, c.name,
       MIN(o.order_date) AS first_order,
       MAX(o.order_date) AS last_order
FROM clients c
JOIN orders o ON o.client_id = c.client_id
GROUP BY c.client_id, c.name;