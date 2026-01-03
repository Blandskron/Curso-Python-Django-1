CREATE TABLE pedidos (
  order_id SERIAL PRIMARY KEY,
  client_id INT NOT NULL,
  fecha DATE,
  FOREIGN KEY (client_id)
    REFERENCES clientes(client_id)
    ON DELETE CASCADE
);