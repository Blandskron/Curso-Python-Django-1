BEGIN;

UPDATE org.products SET price = -10 WHERE product_id = 1; -- violará CHECK (price >= 0)

ROLLBACK;