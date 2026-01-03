BEGIN;

INSERT INTO orders (client_id, order_date, status)
VALUES (1, CURRENT_DATE, 'PENDING')
RETURNING order_id;

-- Supón que devuelve 300 (en tu app lo capturas)
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (300, 1, 1, 9900),
       (300, 2, 1, 19900);

COMMIT;