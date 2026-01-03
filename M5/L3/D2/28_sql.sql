DELETE FROM payments
WHERE payment_id = 55;

UPDATE orders
SET status = 'PENDING'
WHERE order_id = 10;