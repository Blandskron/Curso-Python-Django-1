BEGIN;
UPDATE orders SET status = 'CANCELLED' WHERE order_id = 10;
ROLLBACK;