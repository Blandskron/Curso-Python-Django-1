-- Si desactivas autocommit (depende de la herramienta):
BEGIN;
UPDATE products SET price = price * 1.02 WHERE category = 'SOFTWARE';
-- si sales sin COMMIT, no queda persistido.
ROLLBACK;