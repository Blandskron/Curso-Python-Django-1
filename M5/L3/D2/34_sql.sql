BEGIN;

UPDATE products
SET price = -1
WHERE product_id = 1; -- viola CHECK (price >= 0)

ROLLBACK;