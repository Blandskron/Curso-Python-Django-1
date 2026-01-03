CREATE TABLE clientes (
  client_id SERIAL PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL,
  email VARCHAR(150) UNIQUE,
  creado_en TIMESTAMP DEFAULT now()
);