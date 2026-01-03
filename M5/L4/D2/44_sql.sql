CREATE TABLE pedido_items (
  order_id INT,
  product_id INT,
  cantidad INT NOT NULL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES pedidos(order_id),
  FOREIGN KEY (product_id) REFERENCES productos(product_id)
);