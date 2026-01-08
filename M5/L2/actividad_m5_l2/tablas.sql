CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50)
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER,
    fecha DATE,
    total NUMERIC,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);