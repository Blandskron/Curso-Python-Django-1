CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    saldo NUMERIC(15,2) NOT NULL CHECK (saldo >= 0)
);

CREATE TABLE transferencias (
    id SERIAL PRIMARY KEY,
    destinatario_id INTEGER NOT NULL,
    total NUMERIC(15,2) NOT NULL CHECK (total > 0),

    CONSTRAINT fk_transferencia_destinatario
        FOREIGN KEY (destinatario_id)
        REFERENCES clientes(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
