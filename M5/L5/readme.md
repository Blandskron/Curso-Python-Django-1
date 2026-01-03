# A) Modelo conceptual ER → “expresado” en SQL (entidades, identificadores, relaciones)

## Entidades fuertes (Strong entities)

### 1) Entidad: students (PK = student_id)

```sql
CREATE TABLE students (
  student_id BIGSERIAL PRIMARY KEY,
  full_name  VARCHAR(120) NOT NULL,
  email      VARCHAR(150) UNIQUE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);
```

### 2) Entidad: courses (PK = course_id)

```sql
CREATE TABLE courses (
  course_id BIGSERIAL PRIMARY KEY,
  code      VARCHAR(30) UNIQUE NOT NULL,
  title     VARCHAR(160) NOT NULL,
  level     VARCHAR(20) NOT NULL CHECK (level IN ('BEGINNER','INTERMEDIATE','ADVANCED')),
  is_active BOOLEAN NOT NULL DEFAULT TRUE
);
```

## Relación 1 a N (Course 1—N Module)

### 3) Entidad: modules (FK -> courses)

```sql
CREATE TABLE modules (
  module_id BIGSERIAL PRIMARY KEY,
  course_id BIGINT NOT NULL REFERENCES courses(course_id) ON DELETE CASCADE,
  title     VARCHAR(160) NOT NULL,
  position  INT NOT NULL CHECK (position > 0),
  UNIQUE (course_id, position)
);
```

## Relación N a N (Student N—N Course) con tabla asociativa (Enrollment)

### 4) Tabla asociativa: enrollments (PK compuesta)

```sql
CREATE TABLE enrollments (
  student_id BIGINT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
  course_id  BIGINT NOT NULL REFERENCES courses(course_id) ON DELETE RESTRICT,
  enrolled_at TIMESTAMP NOT NULL DEFAULT now(),
  status     VARCHAR(20) NOT NULL CHECK (status IN ('ACTIVE','COMPLETED','DROPPED')),
  final_grade NUMERIC(5,2) CHECK (final_grade BETWEEN 1 AND 7),
  PRIMARY KEY (student_id, course_id)
);
```

## Entidad débil (Weak entity): student_addresses

Dependiente de `students` (su PK incluye la PK del padre)

### 5) Entidad débil: student_addresses (PK = student_id, address_no)

```sql
CREATE TABLE student_addresses (
  student_id BIGINT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE,
  address_no SMALLINT NOT NULL CHECK (address_no > 0),
  street     VARCHAR(160) NOT NULL,
  city       VARCHAR(80) NOT NULL,
  country    CHAR(2) NOT NULL,
  PRIMARY KEY (student_id, address_no)
);
```

---

# B) Tipos de relaciones (1–1, 1–N, N–N) en SQL

## 1–1 (ej: cada curso tiene 1 “course_profile” opcional)

### 6) Tabla 1–1 usando PK=FK

```sql
CREATE TABLE course_profiles (
  course_id BIGINT PRIMARY KEY REFERENCES courses(course_id) ON DELETE CASCADE,
  description TEXT,
  language VARCHAR(10) NOT NULL DEFAULT 'es'
);
```

## 1–N ya visto (courses -> modules) ✅

## N–N ya visto (students <-> courses via enrollments) ✅

---

# C) Reglas de transformación (ER → Relacional) “en forma SQL”

### 7) Regla: entidad fuerte → tabla con PK

```sql
-- students(student_id PK), courses(course_id PK)
```

### 8) Regla: 1–N → FK en el lado N

```sql
-- modules.course_id FK -> courses.course_id
```

### 9) Regla: N–N → tabla puente con PK compuesta + FKs

```sql
-- enrollments(student_id, course_id) PK + FKs
```

### 10) Regla: entidad débil → PK compuesta que incluye PK del dueño

```sql
-- student_addresses PK(student_id, address_no)
```

*(Las “reglas” se ven materializadas en las definiciones anteriores.)*

---

# D) Normalización (hasta 3FN) con ejemplos SQL

## 1) Ejemplo malo (NO normalizado): todo mezclado en una sola tabla

### 11) Tabla desnormalizada (anti-ejemplo)

```sql
CREATE TABLE raw_enrollments_bad (
  student_email VARCHAR(150),
  student_name  VARCHAR(120),
  course_code   VARCHAR(30),
  course_title  VARCHAR(160),
  module_titles TEXT, -- "Intro|SQL Básico|JOINs"
  status        VARCHAR(20),
  final_grade   NUMERIC(5,2)
);
```

### 12) Problema típico: duplicación e inconsistencias (mismo curso repetido)

```sql
INSERT INTO raw_enrollments_bad
(student_email, student_name, course_code, course_title, module_titles, status, final_grade)
VALUES
('a@correo.com','Ana','SQL-01','SQL desde cero','Intro|SELECT|JOIN','ACTIVE',NULL),
('b@correo.com','Beto','SQL-01','SQL Basico','Intro|SELECT|JOIN','ACTIVE',NULL); -- título inconsistente
```

---

## 1FN (valores atómicos, sin listas en una columna)

### 13) “Separar” módulos: crear tabla raw_modules_1nf

```sql
CREATE TABLE raw_modules_1nf (
  course_code VARCHAR(30),
  module_title VARCHAR(160)
);
```

### 14) Insertar módulos como filas (ya no “lista”)

```sql
INSERT INTO raw_modules_1nf (course_code, module_title)
VALUES ('SQL-01','Intro'), ('SQL-01','SELECT'), ('SQL-01','JOIN');
```

---

## 2FN (si PK compuesta, nada debe depender solo de una parte)

En `enrollments(student_id, course_id)` los atributos `status, final_grade` dependen del par completo ✅
Pero **course_title** depende solo de `course_id` (o `course_code`) → debe vivir en `courses`.
**student_name/email** dependen solo de `student_id` → deben vivir en `students`.

*(Eso ya queda resuelto separando `students`, `courses`, y dejando `enrollments` solo con atributos de la relación.)*

### 15) Ejemplo correcto 2FN: enrollments solo con datos de inscripción

```sql
-- enrollments ya cumple: status, enrolled_at, final_grade dependen de (student_id, course_id)
```

---

## 3FN (sin dependencias transitivas: atributos no-clave no dependen de otros no-clave)

Ejemplo clásico: `city -> country` o `course_code -> course_title` (depende del curso, no de inscripción).
Solución: tabla `cities` o referencias separadas si aplica.

### 16) Tabla lookup (catálogo) para países (evita inconsistencias)

```sql
CREATE TABLE countries (
  country_code CHAR(2) PRIMARY KEY,
  country_name VARCHAR(80) NOT NULL
);
```

### 17) Ajustar direcciones para referenciar catálogo (3FN)

```sql
ALTER TABLE student_addresses
ADD CONSTRAINT fk_addr_country
FOREIGN KEY (country) REFERENCES countries(country_code);
```

---

# E) Restricciones y “reglas del modelo” (parte del diseño)

### 18) Evitar módulos duplicados por curso y posición (ya puesto, pero ejemplo explícito)

```sql
-- UNIQUE(course_id, position) en modules
```

### 19) Evitar doble inscripción (PK compuesta lo garantiza)

```sql
-- PRIMARY KEY(student_id, course_id) en enrollments
```

### 20) CHECK para estados

```sql
ALTER TABLE enrollments
ADD CONSTRAINT chk_enroll_status
CHECK (status IN ('ACTIVE','COMPLETED','DROPPED'));
```

### 21) CHECK para notas (escala chilena 1–7)

```sql
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (final_grade IS NULL OR final_grade BETWEEN 1 AND 7);
```

---

# F) Diccionario de datos (documentación del modelo) en SQL

## 1) Comentarios en tablas/columnas (muy usado como diccionario “in-db”)

### 22) Comentario de tabla

```sql
COMMENT ON TABLE students IS 'Almacena estudiantes. Entidad fuerte del sistema de cursos.';
```

### 23) Comentarios de columnas

```sql
COMMENT ON COLUMN students.email IS 'Correo único del estudiante (login/contacto).';
COMMENT ON COLUMN enrollments.final_grade IS 'Nota final (1 a 7) si el curso está completado.';
```

### 24) Comentario de relación

```sql
COMMENT ON TABLE enrollments IS 'Tabla puente N-N entre students y courses (inscripciones).';
```

## 2) Consultas a metadatos (INFORMATION_SCHEMA) para generar diccionario

### 25) Diccionario: columnas + tipos + nulidad

```sql
SELECT table_name, column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_schema = 'public'
ORDER BY table_name, ordinal_position;
```

### 26) Diccionario: PKs

```sql
SELECT tc.table_name, kcu.column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
WHERE tc.constraint_type = 'PRIMARY KEY'
  AND tc.table_schema = 'public'
ORDER BY tc.table_name, kcu.ordinal_position;
```

### 27) Diccionario: FKs (integridad referencial)

```sql
SELECT
  tc.table_name AS fk_table,
  kcu.column_name AS fk_column,
  ccu.table_name AS referenced_table,
  ccu.column_name AS referenced_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_schema = 'public'
ORDER BY fk_table, fk_column;
```

### 28) Diccionario: constraints CHECK

```sql
SELECT conrelid::regclass AS table_name, conname AS constraint_name, pg_get_constraintdef(oid) AS definition
FROM pg_constraint
WHERE contype = 'c'
ORDER BY table_name, constraint_name;
```

### 29) Diccionario: índices

```sql
SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;
```

### 30) Diccionario: comentarios (tablas/columnas)

```sql
SELECT
  c.relname AS table_name,
  a.attname AS column_name,
  d.description
FROM pg_class c
JOIN pg_attribute a ON a.attrelid = c.oid
LEFT JOIN pg_description d ON d.objoid = c.oid AND d.objsubid = a.attnum
WHERE c.relkind = 'r' AND a.attnum > 0
ORDER BY table_name, a.attnum;
```

---

# G) “Modelo relacional resuelve el problema” (DDL final + ejemplo de uso mínimo)

### 31) Insertar países (catálogo)

```sql
INSERT INTO countries (country_code, country_name)
VALUES ('CL','Chile'), ('AR','Argentina');
```

### 32) Insertar estudiantes

```sql
INSERT INTO students (full_name, email)
VALUES ('Ana Pérez','ana@mail.com'),
       ('Beto Soto','beto@mail.com');
```

### 33) Insertar direcciones (entidad débil)

```sql
INSERT INTO student_addresses (student_id, address_no, street, city, country)
VALUES (1, 1, 'Av. Siempre Viva 123', 'Santiago', 'CL');
```

### 34) Insertar cursos

```sql
INSERT INTO courses (code, title, level)
VALUES ('SQL-01','SQL desde cero','BEGINNER');
```

### 35) Insertar módulos (1–N)

```sql
INSERT INTO modules (course_id, title, position)
VALUES (1, 'Introducción', 1),
       (1, 'SELECT y WHERE', 2),
       (1, 'JOINs', 3);
```

### 36) Inscribir estudiante (N–N)

```sql
INSERT INTO enrollments (student_id, course_id, status)
VALUES (1, 1, 'ACTIVE');
```

---

# H) Normalización vs desnormalización (para discutir en clase con SQL)

### 37) Vista desnormalizada (para reporting, sin romper 3FN físicamente)

```sql
CREATE OR REPLACE VIEW v_student_course_status AS
SELECT s.student_id, s.full_name, s.email,
       c.course_id, c.code, c.title,
       e.status, e.enrolled_at, e.final_grade
FROM students s
JOIN enrollments e ON e.student_id = s.student_id
JOIN courses c ON c.course_id = e.course_id;
```

### 38) Consultar la vista (report)

```sql
SELECT * FROM v_student_course_status
ORDER BY enrolled_at DESC;
```

---

# I) Extra: Validación de “baja complejidad” con cardinalidades y reglas

### 39) Asegurar “un perfil por curso” (1–1 ya garantizado por PK=FK)

```sql
-- course_profiles.course_id es PK y FK: no puede haber 2 perfiles para 1 curso.
```

### 40) Evitar módulos con misma posición por curso (ya garantizado)

```sql
-- UNIQUE(course_id, position)
```

### 41) Cambiar modelo: permitir “borrar curso si borro módulos y perfiles” (CASCADE)

```sql
ALTER TABLE modules
DROP CONSTRAINT modules_course_id_fkey;

ALTER TABLE modules
ADD CONSTRAINT modules_course_id_fkey
FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE;
```

---

# J) “Reglas de transformación” explicadas con más SQL (ejemplos alternativos)

### 42) N–N alternativa con ID artificial (surrogate key) + UNIQUE

```sql
CREATE TABLE enrollments_surrogate (
  enrollment_id BIGSERIAL PRIMARY KEY,
  student_id BIGINT NOT NULL REFERENCES students(student_id),
  course_id  BIGINT NOT NULL REFERENCES courses(course_id),
  status VARCHAR(20) NOT NULL,
  UNIQUE (student_id, course_id)
);
```

### 43) Entidad débil alternativa: 1 dirección “principal” (1–1)

```sql
CREATE TABLE student_primary_address (
  student_id BIGINT PRIMARY KEY REFERENCES students(student_id) ON DELETE CASCADE,
  street VARCHAR(160) NOT NULL,
  city VARCHAR(80) NOT NULL,
  country CHAR(2) NOT NULL REFERENCES countries(country_code)
);
```

---

# K) Diccionario de datos “formato tabla” (consulta lista para exportar)

### 44) Diccionario: tabla, columna, tipo, null, default

```sql
SELECT
  table_name,
  column_name,
  data_type,
  is_nullable,
  column_default
FROM information_schema.columns
WHERE table_schema = 'public'
ORDER BY table_name, ordinal_position;
```

### 45) Diccionario: constraints por tabla

```sql
SELECT
  tc.table_name,
  tc.constraint_type,
  tc.constraint_name
FROM information_schema.table_constraints tc
WHERE tc.table_schema = 'public'
ORDER BY tc.table_name, tc.constraint_type;
```

### 46) Diccionario: columnas por constraint (PK/UK/FK)

```sql
SELECT
  tc.table_name,
  tc.constraint_name,
  tc.constraint_type,
  kcu.column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
WHERE tc.table_schema = 'public'
ORDER BY tc.table_name, tc.constraint_name, kcu.ordinal_position;
```

---

# L) “Chequeo de normalización” con consultas (para detectar duplicados/inconsistencias)

### 47) Detectar emails duplicados (si no existiera UNIQUE)

```sql
SELECT email, COUNT(*)
FROM students
GROUP BY email
HAVING COUNT(*) > 1;
```

### 48) Detectar cursos duplicados por code (si no existiera UNIQUE)

```sql
SELECT code, COUNT(*)
FROM courses
GROUP BY code
HAVING COUNT(*) > 1;
```

---

# M) Limpieza del modelo (para práctica)

### 49) Eliminar todo el modelo en orden seguro

```sql
DROP VIEW IF EXISTS v_student_course_status;
DROP TABLE IF EXISTS enrollments_surrogate;
DROP TABLE IF EXISTS course_profiles;
DROP TABLE IF EXISTS student_primary_address;
DROP TABLE IF EXISTS student_addresses;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS countries;
```

### 50) Truncar (si quieres vaciar datos sin borrar estructura)

```sql
TRUNCATE TABLE enrollments, modules, courses, student_addresses, students RESTART IDENTITY CASCADE;
```