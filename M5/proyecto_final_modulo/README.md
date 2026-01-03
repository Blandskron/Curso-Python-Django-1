# E-commerce — Módulo 5 (Bases de Datos Relacionales)

## 1) Descripción general
Esta base de datos modela un e-commerce mínimo (MVP) con:
- **Usuarios** (clientes y administradores)
- **Categorías**
- **Productos**
- **Stock por producto**
- **Pedidos**
- **Detalle de pedidos** (productos y cantidades)

El modelo permite:
- Asociar pedidos a usuarios
- Asociar productos a categorías
- Registrar múltiples productos dentro de un pedido (order_items)
- Controlar disponibilidad de stock por producto
- Distinguir usuarios administradores mediante el campo `role`

## 2) Orden de ejecución
1. `schema.sql` — crea tablas, llaves y restricciones
2. `seed.sql` — carga datos de ejemplo
3. `queries.sql` — consultas solicitadas
4. `transaction.sql` — operación transaccional de compra

## 3) Evidencia (ejemplos de consultas)
Ejemplos que deberían devolver resultados con los datos del seed:

### Productos con su categoría
```sql
SELECT p.name, c.name
FROM products p
JOIN categories c ON c.category_id = p.category_id;
````

### Total de un pedido (pedido más reciente)

```sql
SELECT o.order_id, SUM(oi.quantity * oi.unit_price) AS total
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.order_id = (SELECT MAX(order_id) FROM orders)
GROUP BY o.order_id;
```

### Productos con stock bajo

```sql
SELECT p.name, s.quantity, s.low_stock_threshold
FROM stock s
JOIN products p ON p.product_id = s.product_id
WHERE s.quantity < s.low_stock_threshold;
