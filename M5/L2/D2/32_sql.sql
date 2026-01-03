SELECT c.client_id, c.name
FROM clients c
WHERE (
  SELECT COUNT(*)
  FROM orders o
  WHERE o.client_id = c.client_id
) > 5;