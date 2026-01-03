/* ============================================================================
   schema.sql — E-commerce (Módulo 5)
   Motor recomendado: PostgreSQL (pero es estándar y fácil de adaptar)
   Requisitos: usuarios, productos, categorías, pedidos, detalle, stock
   + roles (admin vs customer) + integridad (PK/FK/constraints)
============================================================================ */

-- Limpieza ordenada (hijos -> padres)
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

-- =========================
-- USERS
-- =========================
CREATE TABLE users (
  user_id    BIGSERIAL PRIMARY KEY,
  name       VARCHAR(120) NOT NULL,
  email      VARCHAR(180) NOT NULL UNIQUE,
  role       VARCHAR(20)  NOT NULL CHECK (role IN ('CUSTOMER', 'ADMIN')),
  created_at TIMESTAMP    NOT NULL DEFAULT NOW()
);

-- =========================
-- CATEGORIES
-- =========================
CREATE TABLE categories (
  category_id BIGSERIAL PRIMARY KEY,
  name        VARCHAR(120) NOT NULL UNIQUE,
  description VARCHAR(255)
);

-- =========================
-- PRODUCTS
-- =========================
CREATE TABLE products (
  product_id  BIGSERIAL PRIMARY KEY,
  category_id BIGINT NOT NULL,
  name        VARCHAR(160) NOT NULL,
  description TEXT,
  price       NUMERIC(12,2) NOT NULL CHECK (price >= 0),
  active      BOOLEAN NOT NULL DEFAULT TRUE,
  created_at  TIMESTAMP NOT NULL DEFAULT NOW(),

  CONSTRAINT fk_products_category
    FOREIGN KEY (category_id)
    REFERENCES categories(category_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Evitar duplicados evidentes dentro de la misma categoría (opcional pero útil)
CREATE UNIQUE INDEX uq_products_category_name ON products(category_id, name);

-- =========================
-- STOCK (1:1 con product)
-- =========================
CREATE TABLE stock (
  product_id          BIGINT PRIMARY KEY,
  quantity            INT NOT NULL CHECK (quantity >= 0),
  low_stock_threshold INT NOT NULL DEFAULT 5 CHECK (low_stock_threshold >= 0),
  updated_at          TIMESTAMP NOT NULL DEFAULT NOW(),

  CONSTRAINT fk_stock_product
    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

-- =========================
-- ORDERS
-- =========================
CREATE TABLE orders (
  order_id   BIGSERIAL PRIMARY KEY,
  user_id    BIGINT NOT NULL,
  status     VARCHAR(20) NOT NULL CHECK (status IN ('CREATED', 'PAID', 'CANCELLED')),
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),

  CONSTRAINT fk_orders_user
    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- =========================
-- ORDER_ITEMS
-- =========================
CREATE TABLE order_items (
  order_item_id BIGSERIAL PRIMARY KEY,
  order_id      BIGINT NOT NULL,
  product_id    BIGINT NOT NULL,
  quantity      INT NOT NULL CHECK (quantity > 0),
  unit_price    NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),

  CONSTRAINT fk_items_order
    FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  CONSTRAINT fk_items_product
    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Un producto no debería repetirse dentro del mismo pedido (sumas por quantity)
CREATE UNIQUE INDEX uq_order_items_order_product ON order_items(order_id, product_id);

-- Índices típicos
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_items_order ON order_items(order_id);
CREATE INDEX idx_items_product ON order_items(product_id);
