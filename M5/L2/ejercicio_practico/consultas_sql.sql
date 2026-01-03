/* ============================================================================
   Actividad M5 L2 — Consultas SQL a Tablas y Relaciones
   Archivo: consultas_sql.sql

   OBJETIVO:
   - Consultas a 1 tabla (clientes)
   - Consultas entre 2 tablas (clientes y pedidos) usando JOINs, GROUP BY,
     LEFT JOIN y subconsulta (consulta anidada).

   NOTA:
   - La actividad indica usar una estructura de BD como referencia (PostgreSQL,
     MySQL o SQLite). Asumimos el esquema mínimo:
       clientes(id, nombre, ciudad, ...)
       pedidos(id, cliente_id, total, fecha, ...)
     donde pedidos.cliente_id referencia clientes.id
   ============================================================================ */


/* ---------------------------------------------------------------------------
   (OPCIONAL) ESQUEMA DE REFERENCIA — SI NECESITAS CREARLO RÁPIDO
   Puedes comentar/borrar esta sección si ya tienes tablas creadas.
--------------------------------------------------------------------------- */

-- PostgreSQL (referencia)
-- DROP TABLE IF EXISTS pedidos;
-- DROP TABLE IF EXISTS clientes;

-- CREATE TABLE clientes (
--   id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--   nombre  VARCHAR(120) NOT NULL,
--   ciudad  VARCHAR(120) NOT NULL
-- );

-- CREATE TABLE pedidos (
--   id         INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--   cliente_id INTEGER NOT NULL,
--   total      NUMERIC(12,2) NOT NULL CHECK (total >= 0),
--   fecha      TIMESTAMP NOT NULL DEFAULT NOW(),
--   CONSTRAINT fk_pedidos_clientes
--     FOREIGN KEY (cliente_id) REFERENCES clientes(id)
--     ON UPDATE CASCADE
--     ON DELETE RESTRICT
-- );

-- Datos demo (opcional)
-- INSERT INTO clientes (nombre, ciudad) VALUES
-- ('Ana Pérez', 'Santiago'),
-- ('Luis Soto', 'Valparaíso'),
-- ('Carla Díaz', 'Santiago'),
-- ('Pedro Muñoz', 'Concepción'),
-- ('María Rojas', 'Valparaíso');
--
-- INSERT INTO pedidos (cliente_id, total) VALUES
-- (1, 60000),
-- (1, 55000),
-- (2, 15000),
-- (3, 120000);


/* ============================================================================
   1) CONSULTAS A UNA SOLA TABLA (clientes)
   Requerimientos del PDF:
   - Obtener todos los registros de clientes
   - Nombre y ciudad de clientes en "Valparaíso"
   - Cliente con id = 3
   - COUNT() total clientes
   - Ciudades distintas (DISTINCT)
   - Agrupar por ciudad y contar
============================================================================ */

/* 1.1 Obtener todos los registros de la tabla clientes */
SELECT
  *
FROM clientes;

/* 1.2 Obtener nombre y ciudad de clientes que vivan en "Valparaíso" */
SELECT
  nombre,
  ciudad
FROM clientes
WHERE ciudad = 'Valparaíso';

/* 1.3 Obtener el cliente con id = 3 */
SELECT
  *
FROM clientes
WHERE id = 3;

/* 1.4 COUNT(): contar cuántos clientes hay en total */
SELECT
  COUNT(*) AS total_clientes
FROM clientes;

/* 1.5 Obtener ciudades distintas en las que hay clientes (DISTINCT) */
SELECT DISTINCT
  ciudad
FROM clientes
ORDER BY ciudad;

/* 1.6 Agrupar clientes por ciudad y contar cuántos hay en cada una */
SELECT
  ciudad,
  COUNT(*) AS cantidad_clientes
FROM clientes
GROUP BY ciudad
ORDER BY cantidad_clientes DESC, ciudad ASC;


/* ============================================================================
   2) CONSULTAS ENTRE VARIAS TABLAS (clientes + pedidos)
   Requerimientos del PDF:
   - Obtener todos los pedidos incluyendo nombre del cliente (JOIN)
   - Pedidos hechos por clientes de "Santiago"
   - Total de pedidos por cliente (GROUP BY)
   - LEFT JOIN: todos los clientes, tengan o no pedidos
   - Subconsulta: clientes cuyo total de pedidos supera $100.000
============================================================================ */

/* 2.1 Obtener todos los pedidos, incluyendo el nombre del cliente */
SELECT
  p.id        AS pedido_id,
  p.fecha     AS pedido_fecha,
  p.total     AS pedido_total,
  c.id        AS cliente_id,
  c.nombre    AS cliente_nombre,
  c.ciudad    AS cliente_ciudad
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
ORDER BY p.id;

/* 2.2 Obtener los pedidos hechos por clientes de "Santiago" */
SELECT
  p.id        AS pedido_id,
  p.fecha     AS pedido_fecha,
  p.total     AS pedido_total,
  c.nombre    AS cliente_nombre,
  c.ciudad    AS cliente_ciudad
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
WHERE c.ciudad = 'Santiago'
ORDER BY p.id;

/* 2.3 Obtener el total de pedidos por cliente (COUNT de pedidos y SUM de total) */
SELECT
  c.id                         AS cliente_id,
  c.nombre                     AS cliente_nombre,
  COUNT(p.id)                  AS cantidad_pedidos,
  COALESCE(SUM(p.total), 0)    AS monto_total_pedidos
FROM clientes c
JOIN pedidos p ON p.cliente_id = c.id
GROUP BY c.id, c.nombre
ORDER BY monto_total_pedidos DESC;

/* 2.4 LEFT JOIN: listar TODOS los clientes y sus pedidos, incluso si no tienen */
SELECT
  c.id       AS cliente_id,
  c.nombre   AS cliente_nombre,
  c.ciudad   AS cliente_ciudad,
  p.id       AS pedido_id,
  p.fecha    AS pedido_fecha,
  p.total    AS pedido_total
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
ORDER BY c.id, p.id;

/* 2.5 Consulta anidada: clientes cuyo total de pedidos supera $100.000
   - Subconsulta calcula el SUM(total) por cliente
   - Consulta externa filtra los que superan 100000
*/
SELECT
  t.cliente_id,
  t.cliente_nombre,
  t.total_pedidos
FROM (
  SELECT
    c.id                      AS cliente_id,
    c.nombre                  AS cliente_nombre,
    COALESCE(SUM(p.total), 0) AS total_pedidos
  FROM clientes c
  LEFT JOIN pedidos p ON p.cliente_id = c.id
  GROUP BY c.id, c.nombre
) AS t
WHERE t.total_pedidos > 100000
ORDER BY t.total_pedidos DESC;
