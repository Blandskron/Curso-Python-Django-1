SELECT product_id, name, price,
       CASE
         WHEN price < 10000 THEN 'LOW'
         WHEN price < 30000 THEN 'MID'
         ELSE 'HIGH'
       END AS price_tier
FROM products;