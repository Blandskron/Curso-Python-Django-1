## A) Crear y organizar la base (rol: centralizar, controlar, auditar)

### 1) Crear esquema (organización lógica)

```sql
CREATE SCHEMA IF NOT EXISTS org;
```

### 2) Crear tabla “maestra” de clientes (entidad)

```sql
CREATE TABLE org.clients (
  client_id BIGSERIAL PRIMARY KEY,
  name      VARCHAR(120) NOT NULL,
  email     VARCHAR(150) UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);
```

### 3) Crear tabla de usuarios (quién opera el sistema)

```sql
CREATE TABLE org.users (
  user_id BIGSERIAL PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  username  VARCHAR(60)  NOT NULL UNIQUE,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);
```

### 4) Crear tabla de pedidos (transaccional)

```sql
CREATE TABLE org.orders (
  order_id BIGSERIAL PRIMARY KEY,
  client_id BIGINT NOT NULL REFERENCES org.clients(client_id),
  order_date DATE NOT NULL DEFAULT CURRENT_DATE,
  status VARCHAR(20) NOT NULL DEFAULT 'PENDING'
);
```

### 5) Crear tabla de productos

```sql
CREATE TABLE org.products (
  product_id BIGSERIAL PRIMARY KEY,
  sku VARCHAR(40) NOT NULL UNIQUE,
  name VARCHAR(120) NOT NULL,
  price NUMERIC(12,2) NOT NULL CHECK (price >= 0)
);
```

### 6) Tabla de detalle (relación N a N: orders ↔ products)

```sql
CREATE TABLE org.order_items (
  order_id BIGINT NOT NULL REFERENCES org.orders(order_id) ON DELETE CASCADE,
  product_id BIGINT NOT NULL REFERENCES org.products(product_id),
  quantity INT NOT NULL CHECK (quantity > 0),
  unit_price NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),
  PRIMARY KEY (order_id, product_id)
);
```

---

## B) Objetos clave: restricciones (integridad y consistencia)

### 7) Agregar NOT NULL después

```sql
ALTER TABLE org.clients
  ALTER COLUMN name SET NOT NULL;
```

### 8) Agregar CHECK de estado permitido

```sql
ALTER TABLE org.orders
  ADD CONSTRAINT chk_orders_status
  CHECK (status IN ('PENDING','PAID','CANCELLED','SHIPPED'));
```

### 9) Agregar FK a posteriori (si faltara)

```sql
ALTER TABLE org.orders
  ADD CONSTRAINT fk_orders_client
  FOREIGN KEY (client_id) REFERENCES org.clients(client_id);
```

### 10) UNIQUE compuesto (ej: evitar duplicar SKU por proveedor)

```sql
-- ejemplo genérico (si existiera supplier_id)
-- ALTER TABLE org.products ADD CONSTRAINT uq_supplier_sku UNIQUE (supplier_id, sku);
```

---

## C) Insertar y poblar (rol: registrar operación real)

### 11) Insertar clientes

```sql
INSERT INTO org.clients (name, email)
VALUES ('Acme SpA', 'contacto@acme.cl'),
       ('Nova Ltda', 'hola@nova.cl');
```

### 12) Insertar usuarios

```sql
INSERT INTO org.users (full_name, username)
VALUES ('María Pérez', 'mperez'),
       ('Juan Soto', 'jsoto');
```

### 13) Insertar productos

```sql
INSERT INTO org.products (sku, name, price)
VALUES ('SKU-001', 'Plan Básico', 9900),
       ('SKU-002', 'Plan Pro', 19900);
```

### 14) Crear un pedido

```sql
INSERT INTO org.orders (client_id, status)
VALUES (1, 'PENDING')
RETURNING order_id;
```

### 15) Agregar ítems al pedido

```sql
INSERT INTO org.order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 1, 2, 9900),
       (1, 2, 1, 19900);
```

---

## D) Consultas esenciales (rol: información para decisiones)

### 16) Listar clientes

```sql
SELECT client_id, name, email, created_at
FROM org.clients
ORDER BY created_at DESC;
```

### 17) Pedidos con nombre de cliente (JOIN)

```sql
SELECT o.order_id, c.name AS client, o.order_date, o.status
FROM org.orders o
JOIN org.clients c ON c.client_id = o.client_id
ORDER BY o.order_id DESC;
```

### 18) Total por pedido (SUM)

```sql
SELECT oi.order_id,
       SUM(oi.quantity * oi.unit_price) AS total
FROM org.order_items oi
GROUP BY oi.order_id
ORDER BY oi.order_id;
```

### 19) Top clientes por gasto

```sql
SELECT c.client_id, c.name,
       SUM(oi.quantity * oi.unit_price) AS total_spent
FROM org.clients c
JOIN org.orders o ON o.client_id = c.client_id
JOIN org.order_items oi ON oi.order_id = o.order_id
GROUP BY c.client_id, c.name
ORDER BY total_spent DESC
LIMIT 10;
```

### 20) Filtrar por rango de fechas

```sql
SELECT *
FROM org.orders
WHERE order_date BETWEEN DATE '2025-01-01' AND DATE '2025-12-31';
```

---

## E) Actualización y eliminación (operación controlada)

### 21) Actualizar estado de pedido

```sql
UPDATE org.orders
SET status = 'PAID'
WHERE order_id = 1;
```

### 22) Actualizar precio de producto

```sql
UPDATE org.products
SET price = price * 1.05
WHERE sku = 'SKU-002';
```

### 23) Eliminar cliente (si el modelo lo permite)

*(mejor: “soft delete”, pero ejemplo real de DELETE)*

```sql
DELETE FROM org.clients
WHERE client_id = 2;
```

---

## F) Transacciones (característica RDBMS: ACID)

### 24) Transacción completa: crear pedido + items

```sql
BEGIN;

INSERT INTO org.orders (client_id, status)
VALUES (1, 'PENDING');

INSERT INTO org.order_items (order_id, product_id, quantity, unit_price)
VALUES (currval(pg_get_serial_sequence('org.orders','order_id')), 1, 1, 9900);

COMMIT;
```

### 25) Rollback si algo falla

```sql
BEGIN;

UPDATE org.products SET price = -10 WHERE product_id = 1; -- violará CHECK (price >= 0)

ROLLBACK;
```

---

## G) Vistas (objeto: simplificar consultas para usuarios/BI)

### 26) Vista: pedidos con total

```sql
CREATE OR REPLACE VIEW org.v_orders_with_total AS
SELECT o.order_id, o.client_id, o.order_date, o.status,
       COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total
FROM org.orders o
LEFT JOIN org.order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id, o.client_id, o.order_date, o.status;
```

### 27) Consultar la vista

```sql
SELECT *
FROM org.v_orders_with_total
ORDER BY order_id DESC;
```

---

## H) Índices (característica: rendimiento y escalabilidad)

### 28) Índice por FK (consultas por cliente)

```sql
CREATE INDEX IF NOT EXISTS idx_orders_client_id
ON org.orders(client_id);
```

### 29) Índice por fecha (reportería)

```sql
CREATE INDEX IF NOT EXISTS idx_orders_order_date
ON org.orders(order_date);
```

---

## I) Funciones y triggers (objetos: reglas automáticas)

### 30) Tabla de auditoría

```sql
CREATE TABLE org.audit_log (
  audit_id BIGSERIAL PRIMARY KEY,
  table_name TEXT NOT NULL,
  action TEXT NOT NULL,
  record_id BIGINT,
  changed_at TIMESTAMP NOT NULL DEFAULT now()
);
```

### 31) Función trigger para auditar cambios en orders

```sql
CREATE OR REPLACE FUNCTION org.fn_audit_orders()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO org.audit_log(table_name, action, record_id)
  VALUES ('orders', TG_OP, COALESCE(NEW.order_id, OLD.order_id));
  RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql;
```

### 32) Trigger

```sql
CREATE TRIGGER trg_audit_orders
AFTER INSERT OR UPDATE OR DELETE ON org.orders
FOR EACH ROW EXECUTE FUNCTION org.fn_audit_orders();
```

---

## J) Roles y permisos (rol: seguridad y control de acceso)

### 33) Crear rol de solo lectura (reportería)

```sql
CREATE ROLE reporter NOINHERIT LOGIN PASSWORD 'cambia_esta_clave';
```

### 34) Conceder permisos de lectura

```sql
GRANT USAGE ON SCHEMA org TO reporter;
GRANT SELECT ON ALL TABLES IN SCHEMA org TO reporter;
ALTER DEFAULT PRIVILEGES IN SCHEMA org GRANT SELECT ON TABLES TO reporter;
```

---

## K) Herramientas para consultar objetos (metadatos del RDBMS)

### 35) Listar tablas del esquema (catálogo/INFORMATION_SCHEMA)

```sql
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'org'
ORDER BY table_name;
```