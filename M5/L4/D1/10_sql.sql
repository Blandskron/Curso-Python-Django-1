CREATE TABLE auditoria (
  audit_id SERIAL PRIMARY KEY,
  accion VARCHAR(50),
  fecha TIMESTAMP DEFAULT now()
);