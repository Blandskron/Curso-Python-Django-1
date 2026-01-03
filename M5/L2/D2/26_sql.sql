SELECT o.order_id, c.name AS client, p.name AS product,
       oi.quantity, oi.unit_price
FROM orders o
JOIN clients c      ON c.client_id = o.client_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p     ON p.product_id = oi.product_id
ORDER BY o.order_id, p.name;