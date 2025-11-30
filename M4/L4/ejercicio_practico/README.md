poo_sistema_educacional
=======================

Actividad N° 4 – Implementación de un Modelo POO
Módulo: Programación Avanzada en Python

Descripción general
--------------------

Este proyecto implementa en Python el modelo POO de un sistema
educacional, a partir del diagrama de clases definido en la actividad
anterior (M4_L3 – Generando un Diagrama de Clases).

Se incluyen:

- Clases de personas (Persona, Alumno, Profesor, Administrativo).
- Clases académicas (Carrera, Asignatura, Curso, PeriodoAcademico).
- Clases de apoyo (Horario, Sala, Matricula, Evaluacion, Nota).

Estructura del proyecto
-----------------------

- personas.py
  Contiene:

  - Persona (clase abstracta base).
  - Alumno (subclase de Persona).
  - Profesor (subclase de Persona).
  - Administrativo (subclase de Persona).
- academia.py
  Contiene:

  - Carrera
  - Asignatura
  - PeriodoAcademico
  - Horario
  - Sala
  - Curso
  - Matricula
  - Evaluacion
  - Nota
- main.py
  Script de demostración donde se crean objetos, se relacionan
  entre sí y se muestran ejemplos de polimorfismo, interacción
  entre objetos y “sobrecarga” de métodos.
- README.txt
  Este archivo explicativo.

Conceptos de POO implementados
------------------------------

1) Clases, atributos y métodos

   - Cada entidad relevante del dominio está modelada como clase.
   - Se usan atributos para representar el estado (por ejemplo,
     nombre, código, créditos, etc.).
   - Se definen métodos para modelar comportamientos (inscribir
     alumnos, calcular promedios, verificar fechas, etc.).
2) Encapsulamiento

   - En la clase Persona se usan atributos con prefijo "_" para indicar
     que son internos (_rut, _nombre, _email).
   - En Curso se mantiene internamente la estructura de alumnos,
     evaluaciones y notas, ocultando la implementación al exterior.
3) Herencia

   - Persona es una clase abstracta.
   - Alumno, Profesor y Administrativo heredan de Persona e
     implementan su propio comportamiento en el método mostrar_rol().
4) Polimorfismo

   - En main.py se crea una lista de objetos Persona que contiene
     instancias de Alumno, Profesor y Administrativo.
   - Al recorrer la lista y llamar a mostrar_rol(), cada objeto
     responde según su implementación específica.
5) Sobrecarga de métodos (simulada)

   - Curso.calcular_promedio(alumno=None):
     * Si se llama con un Alumno, devuelve el promedio individual.
     * Si se llama sin parámetro, devuelve el promedio general del curso.
   - Matricula.calcular_arancel(descuento=0.0):
     * Sin descuento, retorna el arancel base.
     * Con descuento (0 < descuento <= 1), aplica porcentaje.
6) Interacción entre objetos

   - En main.py se demuestra:
     * Creación de carreras, asignaturas, periodos, horarios y salas.
     * Creación de un Curso a partir de una Asignatura.
     * Inscripción de Alumnos en el Curso.
     * Generación de Matrículas para cada Alumno.
     * Creación de Evaluaciones y registro de Notas.
     * Cálculo de promedios individuales y del curso.

Cómo ejecutar
--------------

1. Abrir una terminal en la carpeta `poo_sistema_educacional`.
2. Ejecutar:

   python main.py
3. Se mostrará en consola:

   - La demostración de polimorfismo con Persona.mostrar_rol().
   - El resultado de la inscripción a curso.
   - Los aranceles (con y sin descuento).
   - Los promedios finales de los alumnos y el promedio del curso.
