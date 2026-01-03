INSERT INTO orders (client_id, status)
VALUES (1, 'PENDING');

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (currval(pg_get_serial_sequence('orders','order_id')), 1, 1, 9900);