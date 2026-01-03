BEGIN;

SELECT *
FROM orders
WHERE order_id = 10
FOR UPDATE;

UPDATE orders
SET status = 'PAID'
WHERE order_id = 10;

COMMIT;