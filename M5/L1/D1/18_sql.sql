SELECT oi.order_id,
       SUM(oi.quantity * oi.unit_price) AS total
FROM org.order_items oi
GROUP BY oi.order_id
ORDER BY oi.order_id;