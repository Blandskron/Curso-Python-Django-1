-- En muchos clientes SQL, autocommit viene ON por defecto:
UPDATE products SET price = price * 1.02 WHERE category = 'SOFTWARE';
-- Se guarda inmediatamente (si no estás dentro de BEGIN/COMMIT).