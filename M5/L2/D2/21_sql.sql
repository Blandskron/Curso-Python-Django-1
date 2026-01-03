SELECT product_id, name, ROUND(price * 1.19, 2) AS price_with_vat
FROM products;