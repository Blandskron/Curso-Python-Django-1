## 1) Rol de una Base de Datos Relacional en una empresa

Una **base de datos relacional** es el sistema donde una empresa **guarda, organiza, relaciona y protege** información crítica (clientes, productos, ventas, pagos, inventario, etc.) usando **tablas** conectadas entre sí.

Su rol principal es:
- **Centralizar datos**: una “fuente única” (evita Excel duplicados).
- **Asegurar integridad**: reglas que evitan datos inválidos (ej.: venta sin cliente).
- **Soportar procesos**: ventas, pagos, stock, soporte, auditoría.
- **Permitir consultas y reportes**: responder preguntas con SQL.
- **Seguridad y control**: permisos, roles, trazabilidad.

### 3 ejemplos concretos (con SQL)
A continuación, 3 escenarios típicos donde una base relacional es clave:

#### Ejemplo 1: Ventas / Facturación (clientes + pedidos)
**Pregunta de negocio:** ¿Cuánto vendimos este mes y cuáles son los productos top?

```sql
-- Total vendido este mes
SELECT
  DATE_TRUNC('month', NOW()) AS mes,
  SUM(oi.cantidad * oi.precio_unitario) AS total_vendido
FROM ordenes o
JOIN orden_items oi ON oi.orden_id = o.orden_id
WHERE o.fecha >= DATE_TRUNC('month', NOW())
  AND o.estado = 'PAGADA';
````

```sql
-- Top 5 productos por ingresos
SELECT
  p.producto_id,
  p.nombre,
  SUM(oi.cantidad) AS unidades,
  SUM(oi.cantidad * oi.precio_unitario) AS ingresos
FROM orden_items oi
JOIN productos p ON p.producto_id = oi.producto_id
JOIN ordenes o ON o.orden_id = oi.orden_id
WHERE o.estado = 'PAGADA'
GROUP BY p.producto_id, p.nombre
ORDER BY ingresos DESC
LIMIT 5;
```

#### Ejemplo 2: Autenticación / Roles / Permisos

**Pregunta de negocio:** ¿Qué usuarios tienen rol “ADMIN” y cuándo fue su último login?

```sql
SELECT
  u.user_id,
  u.email,
  r.nombre AS rol,
  MAX(l.fecha_login) AS ultimo_login
FROM usuarios u
JOIN usuarios_roles ur ON ur.user_id = u.user_id
JOIN roles r ON r.rol_id = ur.rol_id
LEFT JOIN logins l ON l.user_id = u.user_id
WHERE r.nombre = 'ADMIN'
GROUP BY u.user_id, u.email, r.nombre
ORDER BY ultimo_login DESC NULLS LAST;
```

#### Ejemplo 3: Inventario / Logística

**Pregunta de negocio:** ¿Qué productos están bajo stock mínimo?

```sql
SELECT
  p.producto_id,
  p.nombre,
  i.stock_actual,
  i.stock_minimo
FROM inventario i
JOIN productos p ON p.producto_id = i.producto_id
WHERE i.stock_actual < i.stock_minimo
ORDER BY (i.stock_minimo - i.stock_actual) DESC;
```

---

## 2) ¿Qué es un RDBMS y qué lo diferencia?

Un **RDBMS** (Relational Database Management System) es el software que permite:

* **Crear** bases de datos y tablas
* **Aplicar reglas** (integridad)
* **Guardar y consultar** datos con SQL
* **Administrar usuarios, permisos, backups, rendimiento**

### 3 características que lo diferencian de “guardar datos” en archivos (CSV/JSON/Excel)

1. **Relaciones y JOINs**

* Permite conectar tablas por claves.

```sql
SELECT o.orden_id, c.nombre, o.fecha
FROM ordenes o
JOIN clientes c ON c.cliente_id = o.cliente_id;
```

2. **Restricciones de integridad (PK/FK/UNIQUE/CHECK)**

* Evita que entren datos incorrectos.

```sql
ALTER TABLE clientes
ADD CONSTRAINT uq_clientes_email UNIQUE (email);
```

3. **Transacciones (ACID)**

* Operaciones “todo o nada” (muy importante en pagos).

```sql
BEGIN;

UPDATE cuentas
SET saldo = saldo - 50000
WHERE cuenta_id = 10;

UPDATE cuentas
SET saldo = saldo + 50000
WHERE cuenta_id = 25;

COMMIT;
-- Si algo falla antes del COMMIT, se hace ROLLBACK y no queda inconsistente.
```

### 3 RDBMS comunes y contextos típicos

* **PostgreSQL**: aplicaciones web, microservicios, reporting, alta integridad y extensiones.
* **MySQL/MariaDB**: web tradicional, CMS, e-commerce, gran adopción.
* **SQL Server**: entornos corporativos, integración Microsoft, BI empresarial.

---

## 3) Herramientas para consultar una BD (GUI y CLI)

### GUI (gráficas)

* **DBeaver** (multibase: Postgres/MySQL/SQL Server/SQLite)
* **pgAdmin** (PostgreSQL) / **MySQL Workbench** (MySQL)

### CLI (línea de comandos)

* **psql** (PostgreSQL)
* **mysql** (MySQL/MariaDB)
* **sqlite3** (SQLite)

---

## 4) Objetos dentro de una base de datos (con ejemplos SQL reales)

> En esta sección se explica **Tabla, Vista, Índice, PK y FK** con ejemplos directos en SQL.

### 4.1 Tablas (TABLE)

Una **tabla** guarda datos en filas/columnas.

Ejemplo: clientes, productos, órdenes, items.

```sql
CREATE TABLE clientes (
  cliente_id   BIGSERIAL PRIMARY KEY,
  nombre       VARCHAR(120) NOT NULL,
  email        VARCHAR(160) NOT NULL UNIQUE,
  creado_en    TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE productos (
  producto_id  BIGSERIAL PRIMARY KEY,
  nombre       VARCHAR(140) NOT NULL,
  precio       NUMERIC(12,2) NOT NULL CHECK (precio >= 0),
  activo       BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE ordenes (
  orden_id     BIGSERIAL PRIMARY KEY,
  cliente_id   BIGINT NOT NULL,
  fecha        TIMESTAMP NOT NULL DEFAULT NOW(),
  estado       VARCHAR(20) NOT NULL CHECK (estado IN ('PENDIENTE','PAGADA','CANCELADA')),
  CONSTRAINT fk_ordenes_cliente
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE orden_items (
  orden_item_id   BIGSERIAL PRIMARY KEY,
  orden_id        BIGINT NOT NULL,
  producto_id     BIGINT NOT NULL,
  cantidad        INT NOT NULL CHECK (cantidad > 0),
  precio_unitario NUMERIC(12,2) NOT NULL CHECK (precio_unitario >= 0),

  CONSTRAINT fk_items_orden
    FOREIGN KEY (orden_id) REFERENCES ordenes(orden_id)
    ON DELETE CASCADE,

  CONSTRAINT fk_items_producto
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
    ON DELETE RESTRICT
);
```

#### Insert de ejemplo (DML)

```sql
INSERT INTO clientes (nombre, email)
VALUES ('Ana Pérez', 'ana@correo.com'),
       ('Luis Soto', 'luis@correo.com');

INSERT INTO productos (nombre, precio)
VALUES ('Curso Python', 49990),
       ('Curso SQL', 39990);
```

---

### 4.2 Llave primaria (PRIMARY KEY)

La **PK** identifica **únicamente** cada registro. En los ejemplos:

* `clientes.cliente_id`
* `productos.producto_id`
* `ordenes.orden_id`
* `orden_items.orden_item_id`

Ejemplo de PK compuesta (cuando corresponde):

```sql
CREATE TABLE usuarios_roles (
  user_id BIGINT NOT NULL,
  rol_id  BIGINT NOT NULL,
  PRIMARY KEY (user_id, rol_id)
);
```

---

### 4.3 Llave foránea (FOREIGN KEY)

La **FK** asegura integridad referencial: no puedes crear una orden para un cliente que no existe.

Ejemplo (ya incluido arriba):

```sql
ALTER TABLE ordenes
ADD CONSTRAINT fk_ordenes_cliente
FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id);
```

---

### 4.4 Vistas (VIEW)

Una **vista** es una consulta guardada que se comporta como una “tabla virtual”.
Sirve para:

* Simplificar consultas repetidas
* Entregar información lista para reportes
* Restringir columnas sensibles (seguridad)

Ejemplo: vista con “total por orden”

```sql
CREATE VIEW vw_orden_resumen AS
SELECT
  o.orden_id,
  o.fecha,
  o.estado,
  c.nombre AS cliente,
  c.email,
  SUM(oi.cantidad * oi.precio_unitario) AS total
FROM ordenes o
JOIN clientes c ON c.cliente_id = o.cliente_id
JOIN orden_items oi ON oi.orden_id = o.orden_id
GROUP BY o.orden_id, o.fecha, o.estado, c.nombre, c.email;
```

Uso:

```sql
SELECT * FROM vw_orden_resumen
WHERE estado = 'PAGADA'
ORDER BY fecha DESC;
```

---

### 4.5 Índices (INDEX)

Un **índice** acelera búsquedas y filtros (WHERE), joins y ordenamientos (ORDER BY).
Se recomienda indexar:

* Claves foráneas
* Campos usados frecuentemente en filtros/búsqueda

Ejemplos:

```sql
-- Buscar clientes por email rápido (aunque UNIQUE ya suele crear índice implícito)
CREATE INDEX idx_clientes_email ON clientes(email);

-- Acelera JOIN y filtros por cliente en ordenes
CREATE INDEX idx_ordenes_cliente_id ON ordenes(cliente_id);

-- Acelera consultas por estado y fecha (reportes)
CREATE INDEX idx_ordenes_estado_fecha ON ordenes(estado, fecha);
```

---

## 5) Consultas típicas que demuestran el modelo relacional

### JOIN entre tablas

```sql
SELECT
  o.orden_id,
  o.fecha,
  c.nombre AS cliente,
  SUM(oi.cantidad * oi.precio_unitario) AS total
FROM ordenes o
JOIN clientes c ON c.cliente_id = o.cliente_id
JOIN orden_items oi ON oi.orden_id = o.orden_id
GROUP BY o.orden_id, o.fecha, c.nombre
ORDER BY o.fecha DESC;
```

### Control de integridad: ejemplo de error esperado

Si intentas insertar una orden con `cliente_id` inexistente, la FK lo impide:

```sql
INSERT INTO ordenes (cliente_id, estado)
VALUES (999999, 'PAGADA');  -- debería fallar por FK si ese cliente no existe
```

---

## 6) (Opcional) Ejemplo de transacción real (pago + orden)

Caso: registrar pago y marcar orden como pagada. Si falla el pago, no se actualiza la orden.

```sql
BEGIN;

INSERT INTO pagos (orden_id, monto, fecha)
VALUES (101, 89980, NOW());

UPDATE ordenes
SET estado = 'PAGADA'
WHERE orden_id = 101;

COMMIT;
```

---

## Conclusión

* Una BD relacional **centraliza** y **protege** la información del negocio.
* Un RDBMS aporta **modelo relacional**, **integridad**, **SQL** y **transacciones**.
* Objetos clave:

  * **Tablas** guardan datos
  * **PK/FK** conectan y aseguran integridad
  * **Vistas** simplifican reportes
  * **Índices** mejoran rendimiento
