/* ============================================================================
   Actividad M5 L3 — Manipulación de Datos y Transacciones en SQL
   Archivo: actividad_m5_l3/manipulacion_datos.sql

   Tablas usadas (misma estructura que Actividad anterior):
   - clientes(id, nombre, ciudad, ...)
   - pedidos(id, cliente_id, total, fecha, ...)
   Donde pedidos.cliente_id es FK a clientes.id con RESTRICT (o equivalente).

   Importante:
   - IDs autogenerados con DEFAULT/SERIAL/IDENTITY (no los asignamos manualmente).
   - Si tu BD usa nombres distintos de columnas, ajusta los nombres.
============================================================================ */


/* ----------------------------------------------------------------------------
  1) INSERCIÓN DE DATOS (INSERT)
  Requisitos:
  - Insertar al menos 3 nuevos clientes
  - Insertar al menos 5 pedidos asociados a esos clientes
  - Usar DEFAULT o secuencia para autogenerar IDs
---------------------------------------------------------------------------- */

/* 1.1 Insertar 3 nuevos clientes (IDs autogenerados) */
INSERT INTO clientes (nombre, ciudad)
VALUES
  ('Camila Torres', 'Santiago'),
  ('Diego Fuentes', 'Valparaíso'),
  ('Fernanda López', 'Concepción');

/* (Opcional) Verificar clientes insertados */
SELECT * FROM clientes ORDER BY id DESC LIMIT 10;

/*
  1.2 Insertar al menos 5 pedidos asociados.
  Nota: Para asociarlos necesitamos los IDs reales.
  Si ya existen datos, estos IDs podrían no ser 1..n.
  Solución segura: obtener IDs por email/nombre (o revisar con SELECT).

  Como el esquema mínimo del curso usa nombre+ciudad, aquí usamos el nombre.
  (En una BD real, usarías un identificador único como email).
*/

/* Obtener IDs de los clientes recién insertados */
SELECT id, nombre, ciudad
FROM clientes
WHERE nombre IN ('Camila Torres', 'Diego Fuentes', 'Fernanda López')
ORDER BY id;

/*
  Asumiremos que el SELECT anterior devuelve algo como:
  Camila Torres   -> id = (X)
  Diego Fuentes   -> id = (Y)
  Fernanda López  -> id = (Z)

  Para que el archivo funcione sin “adivinar” IDs,
  insertamos pedidos con subconsultas que obtienen el id por nombre.
*/

/* Insertar 5 pedidos usando subconsulta para cliente_id */
INSERT INTO pedidos (cliente_id, total, fecha)
VALUES
  ((SELECT id FROM clientes WHERE nombre = 'Camila Torres'),  60000, DEFAULT),
  ((SELECT id FROM clientes WHERE nombre = 'Camila Torres'),  25000, DEFAULT),
  ((SELECT id FROM clientes WHERE nombre = 'Diego Fuentes'),  15000, DEFAULT),
  ((SELECT id FROM clientes WHERE nombre = 'Fernanda López'), 80000, DEFAULT),
  ((SELECT id FROM clientes WHERE nombre = 'Fernanda López'), 45000, DEFAULT);

/* (Opcional) Verificar pedidos insertados */
SELECT * FROM pedidos ORDER BY id DESC LIMIT 10;


/* ----------------------------------------------------------------------------
  2) ACTUALIZACIÓN DE DATOS (UPDATE)
  Requisitos:
  - Cambiar ciudad del cliente con id = 2 a "Viña del Mar"
  - Modificar el total de un pedido existente
---------------------------------------------------------------------------- */

/* 2.1 Cambiar ciudad del cliente id=2 a "Viña del Mar" */
UPDATE clientes
SET ciudad = 'Viña del Mar'
WHERE id = 2;

/* Verificar cambio */
SELECT * FROM clientes WHERE id = 2;

/*
  2.2 Modificar el total de un pedido existente
  Nota: como no sabemos qué IDs existen en tu BD, elige un id real.
  Aquí mostramos una forma segura: tomar el pedido más reciente y modificarlo.
*/

/* Ver el pedido más reciente (para identificar un id existente) */
SELECT id, cliente_id, total, fecha
FROM pedidos
ORDER BY id DESC
LIMIT 1;

/* Actualizar el total del pedido más reciente (+10.000) */
UPDATE pedidos
SET total = total + 10000
WHERE id = (
  SELECT id FROM pedidos ORDER BY id DESC LIMIT 1
);

/* Verificar actualización */
SELECT id, cliente_id, total, fecha
FROM pedidos
ORDER BY id DESC
LIMIT 1;


/* ----------------------------------------------------------------------------
  3) ELIMINACIÓN DE DATOS (DELETE)
  Requisitos:
  - Eliminar un pedido por su id
  - Intentar eliminar un cliente que tiene pedidos asociados y documentar resultado
---------------------------------------------------------------------------- */

/* 3.1 Eliminar un pedido por su id
   Elegimos eliminar el pedido más reciente (id conocido por subconsulta).
*/
DELETE FROM pedidos
WHERE id = (
  SELECT id FROM pedidos ORDER BY id DESC LIMIT 1
);

/* Verificar que se eliminó (debería no aparecer) */
SELECT id, cliente_id, total, fecha
FROM pedidos
ORDER BY id DESC
LIMIT 5;

/*
  3.2 Intentar eliminar un cliente que tiene pedidos asociados
  Esto debe FALLAR si existe integridad referencial con RESTRICT/NO ACTION.
  Elegimos un cliente que sabemos que tiene pedidos: 'Camila Torres' (insertamos 2).
*/

/* Confirmar que tiene pedidos */
SELECT
  c.id AS cliente_id,
  c.nombre,
  COUNT(p.id) AS cantidad_pedidos
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
WHERE c.nombre = 'Camila Torres'
GROUP BY c.id, c.nombre;

/*
  Intento de eliminación (esperado: ERROR por FK).
  Resultado esperado típico:
  - PostgreSQL: "update or delete on table 'clientes' violates foreign key constraint ..."
  - MySQL: "Cannot delete or update a parent row: a foreign key constraint fails ..."
  - SQLite: falla si PRAGMA foreign_keys = ON.
*/
DELETE FROM clientes
WHERE id = (SELECT id FROM clientes WHERE nombre = 'Camila Torres');

/* Si quieres comprobar el estado final: */
SELECT * FROM clientes WHERE nombre = 'Camila Torres';
SELECT * FROM pedidos WHERE cliente_id = (SELECT id FROM clientes WHERE nombre = 'Camila Torres');
