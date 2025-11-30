## 1. Modelo propuesto: Sistema educacional

### 1.1 Clases principales

**Persona (abstracta)**

* Atributos (`-` = privado, `+` = público, `#` = protegido):
  * `#rut: str`
  * `#nombre: str`
  * `#email: str`
* Métodos:
  * `+login(usuario: str, clave: str): bool`
  * `+logout(): None`

**Alumno** (hereda de `Persona`)

* Atributos:
  * `-numero_matricula: str`
  * `-fecha_ingreso: date`
  * `-estado: str`  (ej: "regular", "suspendido")
* Métodos:
  * `+inscribirse_curso(curso: Curso): None`
  * `+consultar_notas(): list[Nota]`

**Profesor** (hereda de `Persona`)

* Atributos:
  * `-titulo: str`
  * `-departamento: str`
* Métodos:
  * `+asignar_nota(evaluacion: Evaluacion, alumno: Alumno, puntaje: float): None`
  * `+crear_evaluacion(curso: Curso, nombre: str, ponderacion: float): Evaluacion`

**Administrativo** (hereda de `Persona`)

* Atributos:
  * `-cargo: str`
* Métodos:
  * `+generar_matricula(alumno: Alumno, curso: Curso): Matricula`

---

**Carrera**

* Atributos:
  * `+codigo: str`
  * `+nombre: str`
  * `+duracion_semestres: int`
* Métodos:
  * `+agregar_asignatura(asig: Asignatura): None`
  * `+obtener_malla(): list[Asignatura]`

**Asignatura**

* Atributos:
  * `+codigo: str`
  * `+nombre: str`
  * `+creditos: int`
* Métodos:
  * `+crear_curso(seccion: str, profesor: Profesor, periodo: PeriodoAcademico): Curso`

**Curso** (sección de una asignatura)

* Atributos:
  * `+id_curso: int`
  * `+seccion: str`
  * `+cupo_maximo: int`
* Métodos:
  * `+inscribir_alumno(alumno: Alumno): bool`
  * `+listar_alumnos(): list[Alumno]`
  * `+calcular_promedio(alumno: Alumno): float`

**PeriodoAcademico**

* Atributos:
  * `+anio: int`
  * `+semestre: int`  (1 o 2)
  * `+fecha_inicio: date`
  * `+fecha_fin: date`
* Métodos:
  * `+es_fecha_valida(fecha: date): bool`

**Sala**

* Atributos:
  * `+codigo: str`
  * `+capacidad: int`
  * `+tipo: str`  (ej: "laboratorio", "sala común")
* Métodos:
  * `+esta_disponible(fecha: date, bloque: str): bool`

**Horario**

* Atributos:
  * `+dia_semana: str`
  * `+bloque: str`  (ej: "M1", "M2", "T1")
* Métodos:
  * `+solapa_con(otro: Horario): bool`

**Matricula**

* Atributos:
  * `+id_matricula: int`
  * `+fecha: date`
  * `+estado: str`  (ej: "vigente", "retirada")
* Métodos:
  * `+calcular_arancel(): float`

**Evaluacion**

* Atributos:
  * `+id_evaluacion: int`
  * `+nombre: str`
  * `+fecha: date`
  * `+ponderacion: float`  (0–1)
* Métodos:
  * `+es_aprobatoria(nota: float): bool`

**Nota**

* Atributos:
  * `+valor: float`
* Métodos:
  * `+es_aprobada(): bool`

---

### 1.2 Relaciones y multiplicidades

* **Herencia**

  * `Persona` es clase base:
    * `Persona` ◁── `Alumno`
    * `Persona` ◁── `Profesor`
    * `Persona` ◁── `Administrativo`
* **Carrera – Alumno**

  * Una `Carrera` tiene muchos `Alumno`.
  * Un `Alumno` pertenece a una sola `Carrera`.
  * `Carrera 1 --- * Alumno` (asociación).
* **Carrera – Asignatura**

  * Una `Carrera` agrupa muchas `Asignatura`.
  * Relación de  **agregación** :
    * `Carrera 1 o── * Asignatura`.
* **Asignatura – Curso**

  * Una `Asignatura` se imparte en muchas secciones (`Curso`).
  * Composición (un curso no tiene sentido sin asignatura):
    * `Asignatura 1 *── * Curso`.
* **Curso – Profesor**

  * Un `Curso` es dictado por un `Profesor` (1).
  * Un `Profesor` puede dictar muchos `Curso`.
  * `Profesor 1 --- * Curso`.
* **Curso – Horario – Sala**

  * `Curso 1 --- 1 Horario`
  * `Curso 1 --- 1 Sala`
* **Alumno – Matricula – Curso**

  (modelo más explícito con tabla de relación)

  * `Alumno 1 --- * Matricula`
  * `Curso 1 --- * Matricula`
  * Cada `Matricula` une un alumno con un curso en un periodo.
* **Curso – Evaluacion**

  * `Curso 1 --- * Evaluacion`
* **Evaluacion – Nota – Alumno**

  * Cada `Evaluacion` tiene muchas `Nota`.
  * Cada `Alumno` tiene muchas `Nota`.
  * `Evaluacion 1 --- * Nota`
  * `Alumno 1 --- * Nota`
* **PeriodoAcademico**

  * `PeriodoAcademico 1 --- * Curso`
  * `PeriodoAcademico 1 --- * Matricul`
