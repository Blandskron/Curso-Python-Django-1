CREATE TABLE productos (
  product_id SERIAL PRIMARY KEY,
  nombre VARCHAR(120),
  precio NUMERIC(10,2) CHECK (precio >= 0)
);