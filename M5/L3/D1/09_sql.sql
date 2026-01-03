DELETE FROM payments
WHERE paid_at < now() - INTERVAL '2 years';