BEGIN;
UPDATE orders SET status = 'SHIPPED' WHERE order_id = 10;
COMMIT;