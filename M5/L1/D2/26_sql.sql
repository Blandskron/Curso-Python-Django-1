CREATE OR REPLACE VIEW org.v_orders_with_total AS
SELECT o.order_id, o.client_id, o.order_date, o.status,
       COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total
FROM org.orders o
LEFT JOIN org.order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id, o.client_id, o.order_date, o.status;