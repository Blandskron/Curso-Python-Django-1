-- ejemplo: cart_items(user_id, product_id, quantity)
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT 200, p.product_id, ci.quantity, p.price
FROM cart_items ci
JOIN products p ON p.product_id = ci.product_id
WHERE ci.user_id = 7;