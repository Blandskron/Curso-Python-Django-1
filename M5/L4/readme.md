# 4. Lenguaje de Definición de Datos (DDL)

## 4.1 Sintaxis básica DDL

*(Definir estructuras, no manipular datos)*

### 1) Crear una base de datos

```sql
CREATE DATABASE empresa_db;
```

### 2) Eliminar una base de datos

```sql
DROP DATABASE empresa_db;
```

### 3) Crear un esquema (organización lógica)

```sql
CREATE SCHEMA IF NOT EXISTS ventas;
```

### 4) Eliminar un esquema con todo su contenido

```sql
DROP SCHEMA ventas CASCADE;
```

---

## 4.2 Creación de tablas (modelo relacional completo)

### 5) Crear tabla simple (campos + tipos)

```sql
CREATE TABLE clientes (
  client_id INT,
  nombre VARCHAR(100),
  email VARCHAR(150)
);
```

### 6) Crear tabla con PRIMARY KEY

```sql
CREATE TABLE clientes (
  client_id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(150)
);
```

### 7) Crear tabla con NOT NULL

```sql
CREATE TABLE usuarios (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password_hash TEXT NOT NULL
);
```

### 8) UNIQUE constraint

```sql
CREATE TABLE productos (
  product_id SERIAL PRIMARY KEY,
  sku VARCHAR(40) UNIQUE,
  nombre VARCHAR(120) NOT NULL
);
```

### 9) CHECK constraint

```sql
CREATE TABLE productos (
  product_id SERIAL PRIMARY KEY,
  nombre VARCHAR(120),
  precio NUMERIC(10,2) CHECK (precio >= 0)
);
```

### 10) DEFAULT

```sql
CREATE TABLE auditoria (
  audit_id SERIAL PRIMARY KEY,
  accion VARCHAR(50),
  fecha TIMESTAMP DEFAULT now()
);
```

---

## Creación con llaves foráneas (integridad referencial)

### 11) Tabla padre

```sql
CREATE TABLE clientes (
  client_id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL
);
```

### 12) Tabla hija con FOREIGN KEY

```sql
CREATE TABLE pedidos (
  order_id SERIAL PRIMARY KEY,
  client_id INT NOT NULL,
  fecha DATE NOT NULL,
  FOREIGN KEY (client_id) REFERENCES clientes(client_id)
);
```

### 13) FOREIGN KEY con ON DELETE CASCADE

```sql
CREATE TABLE pedidos (
  order_id SERIAL PRIMARY KEY,
  client_id INT NOT NULL,
  fecha DATE,
  FOREIGN KEY (client_id)
    REFERENCES clientes(client_id)
    ON DELETE CASCADE
);
```

### 14) FOREIGN KEY con ON DELETE RESTRICT

```sql
FOREIGN KEY (client_id)
REFERENCES clientes(client_id)
ON DELETE RESTRICT;
```

### 15) Modelo N a N (tabla intermedia)

```sql
CREATE TABLE pedido_items (
  order_id INT,
  product_id INT,
  cantidad INT NOT NULL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES pedidos(order_id),
  FOREIGN KEY (product_id) REFERENCES productos(product_id)
);
```

---

## Tipos de datos comunes (reconocimiento del modelo)

### 16) Tipos numéricos

```sql
INTEGER, BIGINT, SERIAL, NUMERIC(10,2)
```

### 17) Tipos texto

```sql
CHAR(10), VARCHAR(100), TEXT
```

### 18) Tipos fecha/hora

```sql
DATE, TIME, TIMESTAMP
```

### 19) Booleanos

```sql
BOOLEAN
```

### 20) JSON / JSONB (PostgreSQL)

```sql
CREATE TABLE eventos (
  event_id SERIAL PRIMARY KEY,
  metadata JSONB
);
```

---

## 4.3 Modificación de tablas (ALTER TABLE)

### 21) Agregar columna

```sql
ALTER TABLE clientes
ADD COLUMN email VARCHAR(150);
```

### 22) Eliminar columna

```sql
ALTER TABLE clientes
DROP COLUMN email;
```

### 23) Cambiar tipo de dato

```sql
ALTER TABLE clientes
ALTER COLUMN nombre TYPE VARCHAR(200);
```

### 24) Agregar NOT NULL

```sql
ALTER TABLE clientes
ALTER COLUMN nombre SET NOT NULL;
```

### 25) Quitar NOT NULL

```sql
ALTER TABLE clientes
ALTER COLUMN nombre DROP NOT NULL;
```

### 26) Agregar PRIMARY KEY

```sql
ALTER TABLE clientes
ADD CONSTRAINT pk_clientes PRIMARY KEY (client_id);
```

### 27) Eliminar PRIMARY KEY

```sql
ALTER TABLE clientes
DROP CONSTRAINT pk_clientes;
```

### 28) Agregar FOREIGN KEY

```sql
ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (client_id) REFERENCES clientes(client_id);
```

### 29) Eliminar FOREIGN KEY

```sql
ALTER TABLE pedidos
DROP CONSTRAINT fk_pedidos_clientes;
```

### 30) Agregar UNIQUE

```sql
ALTER TABLE usuarios
ADD CONSTRAINT uq_username UNIQUE (username);
```

---

## Modificación avanzada

### 31) Renombrar columna

```sql
ALTER TABLE clientes
RENAME COLUMN nombre TO nombre_completo;
```

### 32) Renombrar tabla

```sql
ALTER TABLE clientes
RENAME TO clientes_empresa;
```

### 33) Agregar CHECK

```sql
ALTER TABLE productos
ADD CONSTRAINT chk_precio CHECK (precio > 0);
```

### 34) Eliminar CHECK

```sql
ALTER TABLE productos
DROP CONSTRAINT chk_precio;
```

---

## Eliminación y truncado

### 35) Eliminar tabla

```sql
DROP TABLE clientes;
```

### 36) Eliminar tabla si existe

```sql
DROP TABLE IF EXISTS clientes;
```

### 37) Eliminar tabla con dependencias

```sql
DROP TABLE clientes CASCADE;
```

### 38) Truncar tabla (rápido, sin WHERE)

```sql
TRUNCATE TABLE pedidos;
```

### 39) Truncate con reinicio de IDs

```sql
TRUNCATE TABLE pedidos RESTART IDENTITY;
```

### 40) Truncate con dependencias

```sql
TRUNCATE TABLE clientes CASCADE;
```

---

## Modelo completo (ejemplo real de negocio)

### 41) Tabla clientes

```sql
CREATE TABLE clientes (
  client_id SERIAL PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL,
  email VARCHAR(150) UNIQUE,
  creado_en TIMESTAMP DEFAULT now()
);
```

### 42) Tabla productos

```sql
CREATE TABLE productos (
  product_id SERIAL PRIMARY KEY,
  nombre VARCHAR(120),
  precio NUMERIC(10,2) CHECK (precio >= 0)
);
```

### 43) Tabla pedidos

```sql
CREATE TABLE pedidos (
  order_id SERIAL PRIMARY KEY,
  client_id INT NOT NULL,
  fecha DATE NOT NULL,
  FOREIGN KEY (client_id) REFERENCES clientes(client_id)
);
```

### 44) Tabla detalle

```sql
CREATE TABLE pedido_items (
  order_id INT,
  product_id INT,
  cantidad INT NOT NULL,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES pedidos(order_id),
  FOREIGN KEY (product_id) REFERENCES productos(product_id)
);
```

---

## Buenas prácticas DDL

### 45) Crear índices explícitos

```sql
CREATE INDEX idx_pedidos_client_id ON pedidos(client_id);
```

### 46) Índice UNIQUE

```sql
CREATE UNIQUE INDEX idx_productos_sku ON productos(sku);
```

### 47) Comentarios en tablas

```sql
COMMENT ON TABLE clientes IS 'Tabla de clientes del sistema';
```

### 48) Comentarios en columnas

```sql
COMMENT ON COLUMN clientes.email IS 'Correo único del cliente';
```

---

## Control del modelo

### 49) Ver estructura de tabla (metadatos)

```sql
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'clientes';
```

### 50) Ver claves foráneas definidas

```sql
SELECT constraint_name, table_name
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';
```