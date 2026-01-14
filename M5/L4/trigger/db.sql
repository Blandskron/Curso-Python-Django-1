-- =========================
-- TABLAS
-- =========================

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    saldo NUMERIC(10,2) NOT NULL DEFAULT 0,
    creado_en TIMESTAMP DEFAULT NOW()
);

CREATE TABLE transferencias (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    monto NUMERIC(10,2) NOT NULL,
    creado_en TIMESTAMP DEFAULT NOW()
);

CREATE TABLE auditoria (
    id SERIAL PRIMARY KEY,
    tabla TEXT,
    operacion TEXT,
    fecha TIMESTAMP DEFAULT NOW()
);

-- =========================
-- FUNCIONES DE TRIGGER
-- =========================

-- Validar monto positivo
CREATE OR REPLACE FUNCTION validar_monto()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.monto <= 0 THEN
        RAISE EXCEPTION 'El monto debe ser mayor a 0';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Verificar saldo suficiente
CREATE OR REPLACE FUNCTION verificar_saldo()
RETURNS TRIGGER AS $$
DECLARE
    saldo_actual NUMERIC;
BEGIN
    SELECT saldo INTO saldo_actual
    FROM clientes
    WHERE id = NEW.cliente_id;

    IF saldo_actual < NEW.monto THEN
        RAISE EXCEPTION 'Saldo insuficiente';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Descontar saldo
CREATE OR REPLACE FUNCTION descontar_saldo()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE clientes
    SET saldo = saldo - NEW.monto
    WHERE id = NEW.cliente_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Auditoría automática
CREATE OR REPLACE FUNCTION log_transferencias()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO auditoria (tabla, operacion)
    VALUES ('transferencias', TG_OP);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- =========================
-- TRIGGERS
-- =========================

CREATE TRIGGER trg_validar_monto
BEFORE INSERT ON transferencias
FOR EACH ROW
EXECUTE FUNCTION validar_monto();

CREATE TRIGGER trg_verificar_saldo
BEFORE INSERT ON transferencias
FOR EACH ROW
EXECUTE FUNCTION verificar_saldo();

CREATE TRIGGER trg_descontar_saldo
AFTER INSERT ON transferencias
FOR EACH ROW
EXECUTE FUNCTION descontar_saldo();

CREATE TRIGGER trg_log_transferencias
AFTER INSERT OR UPDATE OR DELETE ON transferencias
FOR EACH ROW
EXECUTE FUNCTION log_transferencias();

INSERT INTO clientes (nombre, saldo)
VALUES ('Juan', 1000);

INSERT INTO transferencias (cliente_id, monto)
VALUES (1, 200);
