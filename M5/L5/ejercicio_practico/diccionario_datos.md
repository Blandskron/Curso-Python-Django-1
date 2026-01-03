# Diccionario de Datos — Universidad (Estudiantes, Cursos, Matrículas)

## Tabla: estudiantes

| Campo  | Tipo de Dato   | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|-------|-----------------|---------------|----------------|---------------|--------------|
| rut   | VARCHAR(10)     | No            | Sí             | No            | Identificador único del estudiante (RUT) |
| nombre| VARCHAR(120)    | No            | No             | No            | Nombre completo del estudiante |
| correo| VARCHAR(160)    | No            | No             | No            | Correo del estudiante (UNIQUE: no se repite) |

---

## Tabla: cursos

| Campo               | Tipo de Dato   | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|--------------------|-----------------|---------------|----------------|---------------|--------------|
| codigo             | VARCHAR(20)     | No            | Sí             | No            | Identificador único del curso |
| nombre             | VARCHAR(120)    | No            | No             | No            | Nombre del curso |
| docente_responsable| VARCHAR(120)    | No            | No             | No            | Docente principal responsable |

---

## Tabla: matriculas

> Tabla asociativa que resuelve la relación **N:M** entre estudiantes y cursos, y guarda datos propios (fecha y año).  
> PK compuesta: (estudiante_rut, curso_codigo, anio)

| Campo          | Tipo de Dato | Permite Nulos | Clave Primaria | Clave Foránea | Observaciones |
|---------------|--------------|---------------|----------------|---------------|--------------|
| estudiante_rut| VARCHAR(10)  | No            | Sí (compuesta) | Sí            | FK → estudiantes(rut) |
| curso_codigo  | VARCHAR(20)  | No            | Sí (compuesta) | Sí            | FK → cursos(codigo) |
| fecha_matricula| DATE        | No            | No             | No            | Fecha en que se inscribió |
| anio          | SMALLINT     | No            | Sí (compuesta) | No            | Año de inscripción (CHECK 1900–2100) |

---

# Reflexión

## 1) ¿Cuál fue la mayor dificultad al transformar el modelo conceptual al relacional?
La mayor dificultad fue decidir **cómo representar correctamente la relación N:M** entre estudiantes y cursos. En el modelo E-R se entiende fácil (“muchos a muchos”), pero al pasarlo a relacional se debe crear una **tabla intermedia (matriculas)** con **claves foráneas** a ambas tablas.  
Además, fue importante definir una **clave primaria adecuada**: se usó PK compuesta (estudiante_rut, curso_codigo, anio) para permitir que un estudiante pueda inscribirse al mismo curso en distintos años sin duplicar mal los datos.

## 2) ¿Qué ventajas tiene normalizar una base de datos? ¿Y cuándo conviene desnormalizarla?
**Ventajas de normalizar:**
- Reduce duplicidad (evita repetir datos del estudiante o del curso en cada matrícula).
- Mejora consistencia e integridad (cambias el correo del estudiante en un solo lugar).
- Facilita mantenimiento y escalabilidad.

**Cuándo conviene desnormalizar:**
- Cuando se necesita mayor rendimiento para reportes muy frecuentes (por ejemplo, dashboards) y los JOIN afectan mucho la performance.
- Cuando se crean tablas de resumen/materializadas (por ejemplo, total de matrículas por curso/año) para acelerar consultas, asumiendo un costo adicional de mantenimiento.
