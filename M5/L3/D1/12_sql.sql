INSERT INTO orders (client_id, order_date, status)
SELECT client_id, CURRENT_DATE, 'PENDING'
FROM clients
WHERE country = 'CL';