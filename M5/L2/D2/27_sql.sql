SELECT o.order_id, p.category, SUM(oi.quantity) AS units
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p     ON p.product_id = oi.product_id
WHERE p.category = 'SOFTWARE'
GROUP BY o.order_id, p.category;