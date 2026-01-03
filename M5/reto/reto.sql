/* ============================================================================
   Reto SQL — Pacientes COVID
   Archivo: reto_resuelto.sql

   Tabla base entregada por el enunciado
============================================================================ */

DROP TABLE IF EXISTS pacientes_covid;

CREATE TABLE pacientes_covid
(
    rut VARCHAR(12) NOT NULL,
    nombre VARCHAR(50),
    edad INTEGER,
    dias_enfermo INTEGER,
    fase INTEGER,
    hospital VARCHAR(255),
    PRIMARY KEY (rut)
);

INSERT INTO pacientes_covid (rut, nombre, edad, dias_enfermo, fase, hospital) VALUES
('10-1', 'Pedro',    25, 10, 1, 'JJAguirre'),
('12-2', 'Mario',    33, 15, 2, 'JJAguirre'),
('13-3', 'Diego',    45, 22, 3, 'SanJose'),
('14-4', 'Paula',    28, 18, 3, 'SanJose'),
('15-5', 'Mariela',  32, 21, 3, 'Salvador'),
('16-K', 'Patricia', 37,  2, 1, 'SanJuan'),
('17-7', 'Camila',   23, 12, 2, 'SanJuan'),
('18-8', 'Javiera',  31, 15, 2, 'SanJuan');

-- Verificación
SELECT * FROM pacientes_covid;


/* ============================================================================
   CONSULTAS SOLICITADAS EN EL RETO
============================================================================ */


/* 1) Listar todos los pacientes en fase 2 o 3 */
SELECT
    *
FROM pacientes_covid
WHERE fase IN (2, 3);


/* 2) Mostrar el promedio de edad de los pacientes en fase 1 */
SELECT
    AVG(edad) AS promedio_edad_fase_1
FROM pacientes_covid
WHERE fase = 1;


/* 3) Mostrar la mayor cantidad de días enfermo que lleva un paciente en fase 3 */
SELECT
    MAX(dias_enfermo) AS max_dias_enfermo_fase_3
FROM pacientes_covid
WHERE fase = 3;


/* 4) Mostrar el promedio de días enfermo de los pacientes en fase 2 */
SELECT
    AVG(dias_enfermo) AS promedio_dias_enfermo_fase_2
FROM pacientes_covid
WHERE fase = 2;


/* 5) Mostrar los pacientes con edades entre 25 y 39 que estén en fase 1 o 3 */
SELECT
    *
FROM pacientes_covid
WHERE edad BETWEEN 25 AND 39
  AND fase IN (1, 3);


/* 6) Mostrar todos los pacientes con rut terminado en número
      que estén en un hospital que empiece con 'S' */
SELECT
    *
FROM pacientes_covid
WHERE rut ~ '[0-9]$'          -- termina en número (PostgreSQL)
  AND hospital LIKE 'S%';


/* 7) Mostrar el promedio de edad de pacientes mujeres
      (asumimos mujeres por nombre según datos entregados) */
SELECT
    AVG(edad) AS promedio_edad_mujeres
FROM pacientes_covid
WHERE nombre IN ('Paula', 'Mariela', 'Patricia', 'Camila', 'Javiera');


/* 8) Mostrar la cantidad total de pacientes que están en fase 1 o 3 */
SELECT
    COUNT(*) AS total_pacientes_fase_1_o_3
FROM pacientes_covid
WHERE fase IN (1, 3);
