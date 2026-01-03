SELECT *
FROM payments
WHERE paid_at >= now() - INTERVAL '7 days';