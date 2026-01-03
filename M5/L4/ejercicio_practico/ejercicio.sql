/* ============================================================================
   1) CREACIÓN DE TABLAS (DDL)
============================================================================ */

/*
  ¿Qué es una clave primaria (PRIMARY KEY) y por qué se usa en id?
  - Una PK es una columna (o conjunto de columnas) que identifica de forma ÚNICA cada fila.
  - Se usa típicamente en una columna "id" porque:
      1) es simple de referenciar desde otras tablas (FK),
      2) evita duplicados,
      3) permite relaciones claras (JOIN),
      4) mejora el diseño y la integridad de los datos.
*/

/*
  ¿Qué significa NOT NULL?
  - NOT NULL indica que la columna NO puede quedar vacía (no acepta NULL).
  - Se usa en campos obligatorios, por ejemplo el nombre de un departamento o empleado.
*/

/*
  ¿Qué relación existe entre empleados y departamentos?
  - Relación 1 a N (uno a muchos):
      Un departamento puede tener muchos empleados.
      Un empleado pertenece a un departamento (o puede estar sin depto si se permite NULL).
  - Se implementa con una FK en empleados: empleados.departamento_id -> departamentos.id
*/


/* (Recomendado) Borrar si existen para ejecutar el script varias veces */
DROP TABLE IF EXISTS empleados;
DROP TABLE IF EXISTS departamentos;

/* Tabla: departamentos */
CREATE TABLE departamentos (
  id SERIAL PRIMARY KEY,          -- PK: identifica unívocamente cada departamento
  nombre VARCHAR(100) NOT NULL     -- NOT NULL: el nombre es obligatorio
);

/* Tabla: empleados */
CREATE TABLE empleados (
  id SERIAL PRIMARY KEY,              -- PK: identifica unívocamente cada empleado
  nombre VARCHAR(100) NOT NULL,        -- NOT NULL: el nombre es obligatorio
  correo VARCHAR(100),                -- por ahora permite NULL (luego lo cambiaremos)
  departamento_id INTEGER,            -- FK: referencia al departamento
  CONSTRAINT fk_empleados_departamento
    FOREIGN KEY (departamento_id)
    REFERENCES departamentos(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

/*
  Nota de integridad referencial:
  - ON DELETE RESTRICT evita eliminar un departamento si todavía hay empleados asociados.
  - Esto “protege” la consistencia: no quedan empleados apuntando a un depto inexistente.
*/


/* ============================================================================
   2) MODIFICAR TABLAS EXISTENTES (ALTER TABLE)
============================================================================ */

/* 2.1 Agregar nuevas columnas según el enunciado */
ALTER TABLE empleados
ADD COLUMN fecha_ingreso DATE;

ALTER TABLE departamentos
ADD COLUMN ubicacion VARCHAR(100);

/* 2.2 Modificar campo correo para que NO permita nulos (SET NOT NULL)
   IMPORTANTE:
   - Esto FALLA si ya existen registros con correo = NULL.
   - Solución: antes, actualizar los NULL a un valor por defecto o eliminar/corregir.
*/

/* (opcional) Si ya tienes datos con NULL, primero normaliza:
   UPDATE empleados SET correo = 'sin-correo@empresa.cl' WHERE correo IS NULL;
*/

ALTER TABLE empleados
ALTER COLUMN correo SET NOT NULL;

/* 2.3 Intentar modificar una clave primaria y documentar qué ocurre
   En general:
   - No puedes “quitar” o cambiar una PK si existen dependencias (FK) o si viola unicidad.
   - Además, una PK requiere que la columna sea UNIQUE y NOT NULL.
   - La BD normalmente impedirá la operación o pedirá eliminar restricciones primero.

   Aquí haremos un intento controlado:
   - Intentaremos eliminar la PK (constraint) del campo id.
   - En PostgreSQL, el nombre típico de la constraint es empleados_pkey (puede variar).
   - Si el nombre no coincide, usa:
       \\d empleados
     para ver el nombre real de la PK.
*/

/* Intento (puede fallar si el nombre de constraint es distinto) */
-- ALTER TABLE empleados DROP CONSTRAINT empleados_pkey;

 /*
   ¿Qué ocurre?
   - Si el nombre de la PK no coincide, dará error: "constraint ... does not exist".
   - Si coincide, PostgreSQL sí permite quitarla, pero:
       1) el id ya no será PK (pierdes integridad/identificación única),
       2) si otra tabla dependiera de esa PK por FK, NO te dejará eliminarla.
   - En un sistema real NO se recomienda quitar PK de tablas maestras.
 */

 /* Intento alternativo: cambiar tipo de la PK (también suele fallar si hay dependencias) */
-- ALTER TABLE empleados ALTER COLUMN id TYPE VARCHAR(20);

 /*
   ¿Qué ocurre?
   - Puede fallar por dependencia de secuencia/identity, o por constraints.
   - Si hay FK desde otras tablas hacia empleados.id, también fallará por dependencias.
 */


/* ============================================================================
   3) ELIMINAR Y TRUNCAR TABLAS
============================================================================ */

/* 3.1 Sentencia para eliminar la tabla empleados (considerando su relación con departamentos)
   Relación: empleados -> departamentos (empleados tiene FK hacia departamentos)
   - Esto NO impide borrar empleados.
   - Puedes eliminar empleados sin problemas, porque la FK está en empleados.
*/
DROP TABLE empleados;

/*
  Nota:
  - Si la relación hubiera sido al revés (departamentos referenciando empleados),
    ahí sí habría que eliminar primero la tabla “hija” o usar CASCADE.
*/

/* (Opcional) Si quieres recrear empleados para seguir probando, vuelve a crearla aquí:
CREATE TABLE empleados (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL,
  departamento_id INTEGER,
  fecha_ingreso DATE,
  CONSTRAINT fk_empleados_departamento
    FOREIGN KEY (departamento_id)
    REFERENCES departamentos(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);
*/

/* 3.2 Crear tabla temporal de prueba + insertar 2 registros + TRUNCATE */
DROP TABLE IF EXISTS temp_prueba;

CREATE TABLE temp_prueba (
  id SERIAL PRIMARY KEY,
  valor VARCHAR(50) NOT NULL
);

INSERT INTO temp_prueba (valor)
VALUES ('registro 1'), ('registro 2');

/* Verificar inserción */
SELECT * FROM temp_prueba;

/* Ejecutar TRUNCATE (borra TODOS los registros rápidamente) */
TRUNCATE TABLE temp_prueba;

/* Verificar que quedó vacía */
SELECT * FROM temp_prueba;

/* 3.3 Diferencia entre DELETE y TRUNCATE (comentarios)

  DELETE:
  - Borra filas una por una (puede tener WHERE).
  - Puede disparar triggers por fila.
  - Registra más detalle en logs (más lento en grandes volúmenes).
  - Se puede revertir con ROLLBACK si está dentro de una transacción.

  TRUNCATE:
  - Vacía toda la tabla (no admite WHERE).
  - Es más rápido, especialmente con muchas filas.
  - En muchos motores resetea contadores/identities (dependiendo del motor).
  - Suele tener restricciones con FK (no puedes truncar si hay referencias activas).
  - En PostgreSQL es transaccional (se puede ROLLBACK si estás en una transacción),
    pero en otros motores puede comportarse distinto.
*/
