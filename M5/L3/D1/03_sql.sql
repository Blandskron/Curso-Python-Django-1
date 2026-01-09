--- Insert UNITARIO DE DATOS
INSERT INTO clients (name, email, country)
VALUES ('Nova Ltda', 'hola@nova.cl', 'CL');

-- Insert MASIVO DE DATOS
INSERT INTO products (sku, name, category, price, is_active)
VALUES
  ('SKU-100', 'Plan Básico', 'SOFTWARE', 9900, TRUE),
  ('SKU-200', 'Plan Pro',   'SOFTWARE', 19900, TRUE),
  ('SKU-300', 'Plan Elite', 'SOFTWARE', 29900, FALSE),
  ('SKU-400', 'Servicio de Consultoría', 'SERVICES', 49900, TRUE),
  ('SKU-500', 'Soporte Premium', 'SERVICES', 79900, TRUE),
  ('SKU-600', 'Capacitación Avanzada', 'SERVICES', 99900, FALSE);