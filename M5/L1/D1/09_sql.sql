ALTER TABLE org.orders
  ADD CONSTRAINT fk_orders_client
  FOREIGN KEY (client_id) REFERENCES org.clients(client_id);