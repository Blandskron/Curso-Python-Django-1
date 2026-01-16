/* ============================================================================
   schema.sql — E-commerce (Módulo 5)
   Motor recomendado: PostgreSQL (pero es estándar y fácil de adaptar)
   Requisitos: usuarios, productos, categorías, pedidos, detalle, stock_productos
   + roles (admin vs customer) + integridad (PK/FK/constraints)
============================================================================ */

-- Limpieza ordenada (hijos -> padres)
DROP TABLE IF EXISTS detalle_pedido;
DROP TABLE IF EXISTS stock_productos;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS usuarios;

-- =========================
-- usuarios
-- =========================
CREATE TABLE usuarios (
  usuario_id    BIGSERIAL PRIMARY KEY,
  nombre       VARCHAR(120) NOT NULL,
  correo      VARCHAR(180) NOT NULL UNIQUE,
  rol       VARCHAR(20)  NOT NULL CHECK (rol IN ('CUSTOMER', 'ADMIN')),
  fecha_creacion TIMESTAMP    NOT NULL DEFAULT NOW()
);

-- =========================
-- CATEGORIaS
-- =========================
CREATE TABLE categorias (
  categoria_id BIGSERIAL PRIMARY KEY,
  nombre        VARCHAR(120) NOT NULL UNIQUE,
  descripcion VARCHAR(255)
);

-- =========================
-- PRODUCToS
-- =========================
CREATE TABLE productos (
  producto_id  BIGSERIAL PRIMARY KEY,
  categoria_id BIGINT NOT NULL,
  nombre        VARCHAR(160) NOT NULL,
  descripcion TEXT,
  precio       NUMERIC(12,2) NOT NULL CHECK (precio >= 0),
  activo      BOOLEAN NOT NULL DEFAULT TRUE,
  fecha_creacion  TIMESTAMP NOT NULL DEFAULT NOW(),

  CONSTRAINT fk_productos_categoria
    FOREIGN KEY (categoria_id)
    REFERENCES categorias(categoria_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Evitar duplicados evidentes dentro de la misma categoría (opcional pero útil)
CREATE UNIQUE INDEX uq_productos_categoria_nombre ON productos(categoria_id, nombre);

-- =========================
-- STOCK_productos (1:1 con product)
-- =========================
CREATE TABLE stock_productos (
  producto_id          BIGINT PRIMARY KEY,
  cantidad            INT NOT NULL CHECK (cantidad >= 0),
  stock_minimo_productos INT NOT NULL DEFAULT 5 CHECK (stock_minimo_productos >= 0),
  fecha_creacion          TIMESTAMP NOT NULL DEFAULT NOW(),

  CONSTRAINT fk_stock_productos_productos
    FOREIGN KEY (producto_id)
    REFERENCES productos(producto_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

-- =========================
-- pedidos
-- =========================
CREATE TABLE pedidos (
  pedido_id   BIGSERIAL PRIMARY KEY,
  usuario_id    BIGINT NOT NULL,
  estado     VARCHAR(20) NOT NULL CHECK (estado IN ('CREATED', 'PAID', 'CANCELLED')),
  fecha_creacion TIMESTAMP NOT NULL DEFAULT NOW(),

  CONSTRAINT fk_pedidos_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(usuario_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- =========================
-- detalle_pedido
-- =========================
CREATE TABLE detalle_pedido (
  detalle_pedido_id BIGSERIAL PRIMARY KEY,
  pedido_id      BIGINT NOT NULL,
  producto_id    BIGINT NOT NULL,
  cantidad      INT NOT NULL CHECK (cantidad > 0),
  precio_unitario    NUMERIC(12,2) NOT NULL CHECK (precio_unitario >= 0),

  CONSTRAINT fk_detalle_pedido
    FOREIGN KEY (pedido_id)
    REFERENCES pedidos(pedido_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  CONSTRAINT fk_detalle_productos
    FOREIGN KEY (producto_id)
    REFERENCES productos(producto_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Un producto no debería repetirse dentro del mismo pedido (sumas por cantidad)
CREATE UNIQUE INDEX uq_detalle_pedido_pedidos_productos ON detalle_pedido(pedido_id, producto_id);

-- Índices típicos
CREATE INDEX idx_productos_categoria ON productos(categoria_id);
CREATE INDEX idx_pedidos_usuario ON pedidos(usuario_id);
CREATE INDEX idx_detalle_pedidos ON detalle_pedido(pedido_id);
CREATE INDEX idx_detalle_productos ON detalle_pedido(producto_id);
