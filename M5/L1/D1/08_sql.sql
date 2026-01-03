ALTER TABLE org.orders
  ADD CONSTRAINT chk_orders_status
  CHECK (status IN ('PENDING','PAID','CANCELLED','SHIPPED'));