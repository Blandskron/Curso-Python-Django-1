UPDATE orders
SET status = CASE
  WHEN status = 'PENDING' THEN 'CANCELLED'
  ELSE status
END
WHERE order_date < CURRENT_DATE - INTERVAL '90 days';