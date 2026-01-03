SELECT *
FROM orders
WHERE status = 'PAID' AND order_date >= CURRENT_DATE - INTERVAL '30 days';