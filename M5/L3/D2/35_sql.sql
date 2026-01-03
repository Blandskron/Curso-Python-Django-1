BEGIN;

UPDATE products SET price = price * 1.05 WHERE category = 'SOFTWARE';

SAVEPOINT sp_before_delete;

DELETE FROM orders WHERE order_id = 999; -- quizá no querías borrar esto

ROLLBACK TO SAVEPOINT sp_before_delete;

COMMIT;