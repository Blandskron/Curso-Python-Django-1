-- suponiendo tabla product_stock(product_id PK, stock INT)
INSERT INTO product_stock (product_id, stock)
VALUES (10, 5)
ON CONFLICT (product_id)
DO UPDATE SET stock = product_stock.stock + EXCLUDED.stock;