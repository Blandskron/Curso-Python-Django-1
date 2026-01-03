-- Si sku es UNIQUE, esto fallará si ya existe
INSERT INTO products (sku, name, category, price, is_active)
VALUES ('SKU-100', 'Duplicado', 'SOFTWARE', 9990, TRUE);