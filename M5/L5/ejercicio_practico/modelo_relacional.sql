/* ============================================================================
   Actividad M5 L5 — Modelo Relacional (Universidad)
   Archivo: actividad_m5_l5/modelo_relacional.sql

   Escenario (según guía):
   - Estudiantes: RUT, nombre, correo
   - Cursos: código, nombre, docente responsable
   - Relación N:M mediante matrícula
   - Matrícula registra fecha y año de inscripción
============================================================================ */

-- Limpieza (para re-ejecutar)
DROP TABLE IF EXISTS matriculas;
DROP TABLE IF EXISTS cursos;
DROP TABLE IF EXISTS estudiantes;

-- 1) Tabla: estudiantes
CREATE TABLE estudiantes (
  rut      VARCHAR(10)  PRIMARY KEY,          -- Identificador único del estudiante
  nombre   VARCHAR(120) NOT NULL,
  correo   VARCHAR(160) NOT NULL UNIQUE       -- Un correo no se repite
);

-- 2) Tabla: cursos
CREATE TABLE cursos (
  codigo              VARCHAR(20)  PRIMARY KEY,  -- Identificador único del curso
  nombre              VARCHAR(120) NOT NULL,
  docente_responsable VARCHAR(120) NOT NULL
);

-- 3) Tabla: matriculas (relación asociativa N:M)
-- PK compuesta: permite que el mismo estudiante se inscriba al mismo curso en distintos años.
CREATE TABLE matriculas (
  estudiante_rut VARCHAR(10) NOT NULL,
  curso_codigo   VARCHAR(20) NOT NULL,
  fecha_matricula DATE       NOT NULL,
  anio           SMALLINT    NOT NULL CHECK (anio >= 1900 AND anio <= 2100),

  CONSTRAINT pk_matriculas PRIMARY KEY (estudiante_rut, curso_codigo, anio),

  CONSTRAINT fk_matriculas_estudiante
    FOREIGN KEY (estudiante_rut)
    REFERENCES estudiantes(rut)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_matriculas_curso
    FOREIGN KEY (curso_codigo)
    REFERENCES cursos(codigo)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- (Opcional recomendado) Índices para acelerar consultas
CREATE INDEX idx_matriculas_estudiante ON matriculas(estudiante_rut);
CREATE INDEX idx_matriculas_curso ON matriculas(curso_codigo);

-- (Opcional) Datos de prueba mínimos
INSERT INTO estudiantes (rut, nombre, correo) VALUES
('12.345.678-9', 'Ana Pérez',  'ana@universidad.cl'),
('9.876.543-2',  'Luis Soto',  'luis@universidad.cl');

INSERT INTO cursos (codigo, nombre, docente_responsable) VALUES
('INF101', 'Introducción a Bases de Datos', 'Dra. Martínez'),
('MAT100', 'Álgebra I', 'Prof. Rojas');

INSERT INTO matriculas (estudiante_rut, curso_codigo, fecha_matricula, anio) VALUES
('12.345.678-9', 'INF101', '2026-03-10', 2026),
('12.345.678-9', 'MAT100', '2026-03-12', 2026),
('9.876.543-2',  'INF101', '2026-03-11', 2026);
