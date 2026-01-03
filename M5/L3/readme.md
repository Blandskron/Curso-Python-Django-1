## 3.1 Sintaxis básica DML (INSERT / UPDATE / DELETE)

### 1) INSERT básico

```sql
INSERT INTO clients (name, email, country)
VALUES ('Acme SpA', 'contacto@acme.cl', 'CL');
```

### 2) INSERT con DEFAULT (omites created_at si tiene default)

```sql
INSERT INTO clients (name, email, country)
VALUES ('Nova Ltda', 'hola@nova.cl', 'CL');
```

### 3) INSERT múltiples filas

```sql
INSERT INTO products (sku, name, category, price, is_active)
VALUES
  ('SKU-100', 'Plan Básico', 'SOFTWARE', 9900, TRUE),
  ('SKU-200', 'Plan Pro',   'SOFTWARE', 19900, TRUE);
```

### 4) UPDATE básico

```sql
UPDATE clients
SET country = 'AR'
WHERE client_id = 1;
```

### 5) DELETE básico (cuidado en producción)

```sql
DELETE FROM clients
WHERE client_id = 2;
```

---

## 3.2 DML con condiciones (ingreso, actualización, borrado)

### 6) UPDATE con varias columnas

```sql
UPDATE products
SET price = 14990,
    is_active = TRUE
WHERE sku = 'SKU-100';
```

### 7) UPDATE con cálculo (subir 5%)

```sql
UPDATE products
SET price = price * 1.05
WHERE category = 'SOFTWARE';
```

### 8) UPDATE usando CASE (cambiar estados)

```sql
UPDATE orders
SET status = CASE
  WHEN status = 'PENDING' THEN 'CANCELLED'
  ELSE status
END
WHERE order_date < CURRENT_DATE - INTERVAL '90 days';
```

### 9) DELETE con condición por fecha

```sql
DELETE FROM payments
WHERE paid_at < now() - INTERVAL '2 years';
```

### 10) Soft delete (recomendado): marcar inactivo

```sql
UPDATE products
SET is_active = FALSE
WHERE product_id = 10;
```

### 11) INSERT evitando duplicado con ON CONFLICT (UPSERT)

```sql
INSERT INTO clients (email, name, country)
VALUES ('contacto@acme.cl', 'Acme SpA', 'CL')
ON CONFLICT (email)
DO UPDATE SET name = EXCLUDED.name,
              country = EXCLUDED.country;
```

### 12) INSERT…SELECT (poblar desde otra consulta)

```sql
INSERT INTO orders (client_id, order_date, status)
SELECT client_id, CURRENT_DATE, 'PENDING'
FROM clients
WHERE country = 'CL';
```

---

## Secuencias / identificadores (PostgreSQL)

### 13) Obtener el ID generado con RETURNING

```sql
INSERT INTO orders (client_id, status)
VALUES (1, 'PENDING')
RETURNING order_id;
```

### 14) Insertar ítems usando el order_id devuelto (ejemplo conceptual)

```sql
-- Suponiendo que ya obtuviste order_id = 101
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (101, 1, 2, 9900);
```

### 15) Usar currval() con la secuencia (solo en la misma sesión)

```sql
INSERT INTO orders (client_id, status)
VALUES (1, 'PENDING');

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (currval(pg_get_serial_sequence('orders','order_id')), 1, 1, 9900);
```

### 16) Setear un valor de secuencia (por migración / ajuste)

```sql
SELECT setval('orders_order_id_seq', 5000, TRUE);
```

---

## Restricciones y errores típicos (CHECK/UNIQUE/FK)

### 17) UPDATE que respeta CHECK (precio no negativo)

```sql
UPDATE products
SET price = 0
WHERE sku = 'SKU-100';
```

### 18) Ejemplo de violación UNIQUE (provocaría error)

```sql
-- Si sku es UNIQUE, esto fallará si ya existe
INSERT INTO products (sku, name, category, price, is_active)
VALUES ('SKU-100', 'Duplicado', 'SOFTWARE', 9990, TRUE);
```

---

## 3.3 DML con integridad referencial (tablas relacionadas)

### 19) Insertar pedido válido (cliente existente)

```sql
INSERT INTO orders (client_id, order_date, status)
VALUES (1, CURRENT_DATE, 'PENDING');
```

### 20) Insertar ítems válidos (order y product existentes)

```sql
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 2, 1, 19900);
```

### 21) Intentar insertar pedido con client_id inexistente (fallará por FK)

```sql
INSERT INTO orders (client_id, order_date, status)
VALUES (999999, CURRENT_DATE, 'PENDING');
```

### 22) Borrar un pedido y sus ítems (si FK tiene ON DELETE CASCADE)

```sql
DELETE FROM orders
WHERE order_id = 1;
```

### 23) Borrar primero hijos y luego padre (si NO hay CASCADE)

```sql
DELETE FROM order_items
WHERE order_id = 1;

DELETE FROM orders
WHERE order_id = 1;
```

### 24) Actualizar clave foránea: mover pedido a otro cliente

```sql
UPDATE orders
SET client_id = 2
WHERE order_id = 10;
```

### 25) Evitar borrar un cliente con pedidos: soft delete del cliente

```sql
-- suponiendo columna is_active
UPDATE clients
SET is_active = FALSE
WHERE client_id = 1;
```

### 26) Actualizar precios de order_items desde products (consistencia)

```sql
UPDATE order_items oi
SET unit_price = p.price
FROM products p
WHERE p.product_id = oi.product_id
  AND oi.order_id = 10;
```

### 27) Insertar pago y marcar pedido como PAID

```sql
INSERT INTO payments (order_id, paid_at, amount, method, status)
VALUES (10, now(), 29800, 'CARD', 'APPROVED');

UPDATE orders
SET status = 'PAID'
WHERE order_id = 10;
```

### 28) Borrar pago y “revertir” estado (regla de negocio)

```sql
DELETE FROM payments
WHERE payment_id = 55;

UPDATE orders
SET status = 'PENDING'
WHERE order_id = 10;
```

---

## DML basado en resultados (subqueries)

### 29) Actualizar productos no vendidos → inactivos

```sql
UPDATE products p
SET is_active = FALSE
WHERE NOT EXISTS (
  SELECT 1
  FROM order_items oi
  WHERE oi.product_id = p.product_id
);
```

### 30) Borrar pedidos “vacíos” (sin ítems)

```sql
DELETE FROM orders o
WHERE NOT EXISTS (
  SELECT 1
  FROM order_items oi
  WHERE oi.order_id = o.order_id
);
```

### 31) Insertar order_items desde un “carrito” temporal (INSERT…SELECT)

```sql
-- ejemplo: cart_items(user_id, product_id, quantity)
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT 200, p.product_id, ci.quantity, p.price
FROM cart_items ci
JOIN products p ON p.product_id = ci.product_id
WHERE ci.user_id = 7;
```

### 32) Update con subconsulta (poner país según email)

```sql
UPDATE clients
SET country = 'CL'
WHERE email ILIKE '%.cl';
```

---

## 3.4 Transaccionalidad (ACID, COMMIT, ROLLBACK, autocommit)

### 33) Transacción: crear pedido + items + commit (atomicidad)

```sql
BEGIN;

INSERT INTO orders (client_id, order_date, status)
VALUES (1, CURRENT_DATE, 'PENDING')
RETURNING order_id;

-- Supón que devuelve 300 (en tu app lo capturas)
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (300, 1, 1, 9900),
       (300, 2, 1, 19900);

COMMIT;
```

### 34) Transacción con error → ROLLBACK (consistencia)

```sql
BEGIN;

UPDATE products
SET price = -1
WHERE product_id = 1; -- viola CHECK (price >= 0)

ROLLBACK;
```

### 35) SAVEPOINT (revertir parte sin perder todo)

```sql
BEGIN;

UPDATE products SET price = price * 1.05 WHERE category = 'SOFTWARE';

SAVEPOINT sp_before_delete;

DELETE FROM orders WHERE order_id = 999; -- quizá no querías borrar esto

ROLLBACK TO SAVEPOINT sp_before_delete;

COMMIT;
```

### 36) “Confirmación” explícita

```sql
BEGIN;
UPDATE orders SET status = 'SHIPPED' WHERE order_id = 10;
COMMIT;
```

### 37) “Vuelta atrás” explícita

```sql
BEGIN;
UPDATE orders SET status = 'CANCELLED' WHERE order_id = 10;
ROLLBACK;
```

### 38) Bloqueo/aislamiento (idea básica con SELECT FOR UPDATE)

```sql
BEGIN;

SELECT *
FROM orders
WHERE order_id = 10
FOR UPDATE;

UPDATE orders
SET status = 'PAID'
WHERE order_id = 10;

COMMIT;
```

### 39) Ejemplo de consistencia: pago + estado del pedido (todo o nada)

```sql
BEGIN;

INSERT INTO payments (order_id, paid_at, amount, method, status)
VALUES (10, now(), 29800, 'TRANSFER', 'APPROVED');

UPDATE orders
SET status = 'PAID'
WHERE order_id = 10;

COMMIT;
```

### 40) Si falla el INSERT pago, no se marca PAID (rollback)

```sql
BEGIN;

-- supón que method tiene CHECK y esto falla
INSERT INTO payments (order_id, paid_at, amount, method, status)
VALUES (10, now(), 29800, 'INVALID_METHOD', 'APPROVED');

UPDATE orders SET status = 'PAID' WHERE order_id = 10;

ROLLBACK;
```

---

## “Modo autocommit” (cómo se ve en práctica)

### 41) Autocommit ON (cada sentencia se confirma sola)

```sql
-- En muchos clientes SQL, autocommit viene ON por defecto:
UPDATE products SET price = price * 1.02 WHERE category = 'SOFTWARE';
-- Se guarda inmediatamente (si no estás dentro de BEGIN/COMMIT).
```

### 42) Autocommit OFF (necesitas COMMIT)

```sql
-- Si desactivas autocommit (depende de la herramienta):
BEGIN;
UPDATE products SET price = price * 1.02 WHERE category = 'SOFTWARE';
-- si sales sin COMMIT, no queda persistido.
ROLLBACK;
```

---

## Extra: DML “profesional” (buenas prácticas)

### 43) UPDATE con verificación de filas afectadas (RETURNING)

```sql
UPDATE clients
SET email = 'nuevo@acme.cl'
WHERE client_id = 1
RETURNING client_id, name, email;
```

### 44) DELETE con RETURNING (auditar lo que borraste)

```sql
DELETE FROM payments
WHERE status = 'FAILED'
RETURNING payment_id, order_id, amount;
```

### 45) UPSERT con incremento (ej: “stock”)

```sql
-- suponiendo tabla product_stock(product_id PK, stock INT)
INSERT INTO product_stock (product_id, stock)
VALUES (10, 5)
ON CONFLICT (product_id)
DO UPDATE SET stock = product_stock.stock + EXCLUDED.stock;
```