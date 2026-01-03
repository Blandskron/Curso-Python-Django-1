CREATE TABLE org.order_items (
  order_id BIGINT NOT NULL REFERENCES org.orders(order_id) ON DELETE CASCADE,
  product_id BIGINT NOT NULL REFERENCES org.products(product_id),
  quantity INT NOT NULL CHECK (quantity > 0),
  unit_price NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),
  PRIMARY KEY (order_id, product_id)
);