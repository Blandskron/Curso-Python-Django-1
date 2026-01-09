CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    saldo NUMERIC(15,2) NOT NULL
);

CREATE TABLE transferencias (
    id SERIAL PRIMARY KEY,
    destinatario INTEGER NOT NULL,
    total NUMERIC(15,2) NOT NULL
);
