## 2.1 Elementos fundamentales (SELECT, FROM, WHERE, ORDER BY, LIMIT)

### 1) SELECT básico

```sql
SELECT * FROM clients;
```

### 2) Selección de columnas (proyección)

```sql
SELECT client_id, name, email
FROM clients;
```

### 3) Alias de columnas

```sql
SELECT name AS client_name, email AS contact_email
FROM clients;
```

### 4) ORDER BY asc/desc

```sql
SELECT client_id, name, created_at
FROM clients
ORDER BY created_at DESC;
```

### 5) LIMIT / OFFSET (paginación)

```sql
SELECT client_id, name
FROM clients
ORDER BY client_id
LIMIT 10 OFFSET 20;
```

### 6) DISTINCT (evitar duplicados)

```sql
SELECT DISTINCT country
FROM clients
ORDER BY country;
```

---

## 2.2 Condiciones de selección (WHERE, AND/OR, IN, BETWEEN, LIKE, NULL)

### 7) WHERE simple

```sql
SELECT *
FROM products
WHERE is_active = TRUE;
```

### 8) AND / OR

```sql
SELECT *
FROM orders
WHERE status = 'PAID' AND order_date >= CURRENT_DATE - INTERVAL '30 days';
```

### 9) IN (lista de valores)

```sql
SELECT order_id, status
FROM orders
WHERE status IN ('PENDING', 'CANCELLED');
```

### 10) BETWEEN (rango)

```sql
SELECT order_id, order_date
FROM orders
WHERE order_date BETWEEN DATE '2025-01-01' AND DATE '2025-12-31';
```

### 11) LIKE / ILIKE (búsqueda por texto)

```sql
SELECT client_id, name
FROM clients
WHERE name ILIKE '%spa%';
```

### 12) IS NULL / IS NOT NULL

```sql
SELECT client_id, name
FROM clients
WHERE email IS NULL;
```

### 13) Comparaciones numéricas

```sql
SELECT product_id, name, price
FROM products
WHERE price >= 10000 AND price < 50000;
```

### 14) NOT (negación)

```sql
SELECT *
FROM orders
WHERE NOT status = 'CANCELLED';
```

### 15) Condición con fecha “últimos 7 días”

```sql
SELECT *
FROM payments
WHERE paid_at >= now() - INTERVAL '7 days';
```

### 16) CASE (clasificar resultados)

```sql
SELECT product_id, name, price,
       CASE
         WHEN price < 10000 THEN 'LOW'
         WHEN price < 30000 THEN 'MID'
         ELSE 'HIGH'
       END AS price_tier
FROM products;
```

---

## Consultas usando llave primaria (PK)

### 17) Buscar por PK (cliente)

```sql
SELECT *
FROM clients
WHERE client_id = 1;
```

### 18) Buscar por PK (producto)

```sql
SELECT sku, name, price
FROM products
WHERE product_id = 10;
```

---

## Funciones en consultas (texto, fechas, numéricas)

### 19) Funciones de texto (UPPER / LENGTH)

```sql
SELECT client_id, UPPER(name) AS name_upper, LENGTH(name) AS name_len
FROM clients;
```

### 20) COALESCE (reemplazar NULL)

```sql
SELECT client_id, name, COALESCE(email, 'SIN EMAIL') AS email
FROM clients;
```

### 21) Redondeo y cálculo (ROUND)

```sql
SELECT product_id, name, ROUND(price * 1.19, 2) AS price_with_vat
FROM products;
```

### 22) Extraer año/mes (EXTRACT)

```sql
SELECT order_id, order_date,
       EXTRACT(YEAR FROM order_date) AS year,
       EXTRACT(MONTH FROM order_date) AS month
FROM orders;
```

---

## 2.3 Consultas a varias tablas (JOIN + integridad referencial)

### 23) INNER JOIN: pedidos con cliente

```sql
SELECT o.order_id, o.order_date, o.status, c.name AS client
FROM orders o
JOIN clients c ON c.client_id = o.client_id;
```

### 24) LEFT JOIN: clientes aunque no tengan pedidos

```sql
SELECT c.client_id, c.name, o.order_id
FROM clients c
LEFT JOIN orders o ON o.client_id = c.client_id
ORDER BY c.client_id;
```

### 25) JOIN de 3 tablas: pedido + cliente + total

```sql
SELECT o.order_id, c.name AS client,
       SUM(oi.quantity * oi.unit_price) AS total
FROM orders o
JOIN clients c ON c.client_id = o.client_id
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id, c.name
ORDER BY total DESC;
```

### 26) JOIN de 4 tablas: pedido detallado con productos

```sql
SELECT o.order_id, c.name AS client, p.name AS product,
       oi.quantity, oi.unit_price
FROM orders o
JOIN clients c      ON c.client_id = o.client_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p     ON p.product_id = oi.product_id
ORDER BY o.order_id, p.name;
```

### 27) Condición sobre tabla unida (filtrar por categoría)

```sql
SELECT o.order_id, p.category, SUM(oi.quantity) AS units
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p     ON p.product_id = oi.product_id
WHERE p.category = 'SOFTWARE'
GROUP BY o.order_id, p.category;
```

### 28) RIGHT/FULL OUTER (PostgreSQL soporta FULL)

```sql
SELECT c.client_id, c.name, o.order_id
FROM clients c
FULL OUTER JOIN orders o ON o.client_id = c.client_id;
```

### 29) “Antijoin”: clientes sin pedidos (LEFT + IS NULL)

```sql
SELECT c.client_id, c.name
FROM clients c
LEFT JOIN orders o ON o.client_id = c.client_id
WHERE o.order_id IS NULL;
```

### 30) Ver pagos asociados a pedidos (JOIN)

```sql
SELECT p.payment_id, p.amount, p.method, p.status, o.order_id, o.status AS order_status
FROM payments p
JOIN orders o ON o.order_id = p.order_id
ORDER BY p.paid_at DESC;
```

---

## Querys anidadas (subconsultas)

### 31) Subconsulta en WHERE: productos vendidos al menos una vez

```sql
SELECT *
FROM products p
WHERE p.product_id IN (
  SELECT DISTINCT oi.product_id
  FROM order_items oi
);
```

### 32) Subconsulta correlacionada: clientes con más de 5 pedidos

```sql
SELECT c.client_id, c.name
FROM clients c
WHERE (
  SELECT COUNT(*)
  FROM orders o
  WHERE o.client_id = c.client_id
) > 5;
```

### 33) EXISTS: pedidos que tienen al menos 1 ítem

```sql
SELECT o.order_id, o.order_date
FROM orders o
WHERE EXISTS (
  SELECT 1
  FROM order_items oi
  WHERE oi.order_id = o.order_id
);
```

### 34) NOT EXISTS: pedidos “vacíos” (sin ítems)

```sql
SELECT o.order_id
FROM orders o
WHERE NOT EXISTS (
  SELECT 1
  FROM order_items oi
  WHERE oi.order_id = o.order_id
);
```

### 35) Subconsulta como tabla (derived table)

```sql
SELECT t.client_id, t.total_spent
FROM (
  SELECT o.client_id,
         SUM(oi.quantity * oi.unit_price) AS total_spent
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.order_id
  GROUP BY o.client_id
) t
ORDER BY t.total_spent DESC;
```

---

## 2.4 Agrupaciones (GROUP BY, HAVING, COUNT/SUM/AVG/MIN/MAX)

### 36) COUNT: cantidad de pedidos por estado

```sql
SELECT status, COUNT(*) AS orders_count
FROM orders
GROUP BY status
ORDER BY orders_count DESC;
```

### 37) SUM: ventas por mes

```sql
SELECT DATE_TRUNC('month', o.order_date) AS month,
       SUM(oi.quantity * oi.unit_price) AS revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY month
ORDER BY month;
```

### 38) AVG: ticket promedio por pedido

```sql
SELECT AVG(t.total) AS avg_ticket
FROM (
  SELECT oi.order_id, SUM(oi.quantity * oi.unit_price) AS total
  FROM order_items oi
  GROUP BY oi.order_id
) t;
```

### 39) HAVING: clientes con gasto total > 1.000.000

```sql
SELECT c.client_id, c.name,
       SUM(oi.quantity * oi.unit_price) AS total_spent
FROM clients c
JOIN orders o ON o.client_id = c.client_id
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.client_id, c.name
HAVING SUM(oi.quantity * oi.unit_price) > 1000000
ORDER BY total_spent DESC;
```

### 40) MIN/MAX: primera y última compra por cliente

```sql
SELECT c.client_id, c.name,
       MIN(o.order_date) AS first_order,
       MAX(o.order_date) AS last_order
FROM clients c
JOIN orders o ON o.client_id = c.client_id
GROUP BY c.client_id, c.name;
```