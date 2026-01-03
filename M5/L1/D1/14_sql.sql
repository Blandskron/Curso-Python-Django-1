INSERT INTO org.orders (client_id, status)
VALUES (1, 'PENDING')
RETURNING order_id;