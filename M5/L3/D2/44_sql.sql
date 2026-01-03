DELETE FROM payments
WHERE status = 'FAILED'
RETURNING payment_id, order_id, amount;