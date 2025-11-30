Actividad N° 3 – Generando un Diagrama de Clases
Módulo: Programación Avanzada en Python

Descripción general
--------------------

El diagrama de clases modela un sistema educacional básico en el que
participan alumnos, profesores, administrativos, carreras, asignaturas
y cursos, además de elementos de apoyo como matrículas, evaluaciones,
notas, salas, horarios y periodos académicos.

Clases principales
------------------

- Persona (abstracta): clase base para Alumno, Profesor y Administrativo.
- Alumno: representa a los estudiantes, con número de matrícula, estado, etc.
- Profesor: modela a los docentes, con título y departamento.
- Administrativo: usuarios encargados de generar matrículas.
- Carrera: conjunto de asignaturas asociadas a un plan de estudios.
- Asignatura: unidad de aprendizaje, a partir de la cual se crean cursos.
- Curso: sección concreta de una asignatura impartida en un periodo
  académico, con un profesor, sala y horario.
- PeriodoAcademico: representa año, semestre y fechas de inicio/fin.
- Matricula: vincula a un alumno con un curso dentro de un periodo.
- Evaluacion: controles, pruebas o trabajos asociados a un curso.
- Nota: calificación obtenida por un alumno en una evaluación.
- Sala y Horario: permiten asignar espacio físico y bloque horario a un curso.

Relaciones y herencia
---------------------

- Herencia:
  * Persona es superclase de Alumno, Profesor y Administrativo.
- Asociaciones:
  * Carrera se asocia con muchos Alumno.
  * Profesor dicta muchos Curso.
  * Curso se relaciona con una Asignatura, un Horario, una Sala,
    un PeriodoAcademico y muchas Evaluacion.
  * Alumno y Curso se relacionan mediante Matricula.
  * Evaluacion y Alumno se relacionan mediante Nota.
- Agregación:
  * Carrera agrega múltiples Asignatura.
- Composición:
  * Asignatura compone múltiples Curso (el curso no tiene sentido
    sin asignatura en este modelo).

Visibilidad, atributos y métodos
---------------------------------

- Se usa:
  * `+` para métodos y atributos públicos.
  * `-` para atributos privados.
  * `#` para atributos protegidos (en la clase base Persona).
- Cada clase define:
  * Atributos que representan su estado (por ejemplo, código de
    carrera, nombre de asignatura, valor de nota).
  * Métodos que describen comportamientos típicos (inscribir alumno
    en curso, crear evaluación, calcular promedio, etc.).

Cómo se hizo el diagrama
-------------------------

El diagrama fue diseñado siguiendo los conceptos indicados en la
actividad:

- Definición de clases con atributos y métodos.
- Uso de visibilidad en notación UML.
- Inclusión de relaciones, agregación, composición y herencia
  para modelar adecuadamente el dominio de un sistema educacional.

La captura del diagrama (archivo PNG/JPG) se generó a partir de
la especificación del modelo en una herramienta de modelado
(PlantUML, StarUML o Lucidchart), y se incluye junto a este README.
