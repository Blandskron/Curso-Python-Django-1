BEGIN;

-- supón que method tiene CHECK y esto falla
INSERT INTO payments (order_id, paid_at, amount, method, status)
VALUES (10, now(), 29800, 'INVALID_METHOD', 'APPROVED');

UPDATE orders SET status = 'PAID' WHERE order_id = 10;

ROLLBACK;