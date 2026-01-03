SELECT p.payment_id, p.amount, p.method, p.status, o.order_id, o.status AS order_status
FROM payments p
JOIN orders o ON o.order_id = p.order_id
ORDER BY p.paid_at DESC;