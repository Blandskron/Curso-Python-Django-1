SELECT order_id, status
FROM orders
WHERE status IN ('PENDING', 'CANCELLED');