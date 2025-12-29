from datetime import date
from typing import List, Optional

class Persona:
    def __init__(self, rut: str, nombre: str, apellido: str, fecha_nacimiento: date):
        self._rut = rut
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"

    @property
    def edad(self) -> int:
        hoy = date.today()
        return hoy.year - self._fecha_nacimiento.year - ((hoy.month, hoy.day) < (self._fecha_nacimiento.month, self._fecha_nacimiento.day))

    def __str__(self):
        return f"{self.nombre_completo} (RUT: {self._rut})"

class Profesor(Persona):
    def __init__(self, rut: str, nombre: str, apellido: str, fecha_nacimiento: date, id_profesor: str, departamento: str):
        super().__init__(rut, nombre, apellido, fecha_nacimiento)
        self._id_profesor = id_profesor
        self.departamento = departamento
        self._asignaturas_que_dicta = []

    def asignar_asignatura(self, asignatura):
        self._asignaturas_que_dicta.append(asignatura)

    def listar_asignaturas(self):
        return [asig.nombre for asig in self._asignaturas_que_dicta]

    def __str__(self):
        return f"Prof. {super().__str__()} - Depto: {self.departamento}"

class Alumno(Persona):
    def __init__(self, rut: str, nombre: str, apellido: str, fecha_nacimiento: date, matricula: str, carrera: str):
        super().__init__(rut, nombre, apellido, fecha_nacimiento)
        self._matricula = matricula
        self.carrera = carrera
        self._promedio_notas = 0.0

    @property
    def matricula(self):
        return self._matricula

    def estudiar(self, materia: str):
        print(f"El alumno {self.nombre_completo} está estudiando {materia}")

    def __str__(self):
        return f"Alumno: {super().__str__()} - Carrera: {self.carrera}"

class Asignatura:
    def __init__(self, codigo: str, nombre: str, creditos: int):
        self._codigo = codigo
        self._nombre = nombre
        self._creditos = creditos
        self._profesor_titular: Optional[Profesor] = None

    @property
    def nombre(self):
        return self._nombre

    def asignar_profesor(self, profesor: Profesor):
        self._profesor_titular = profesor
        profesor.asignar_asignatura(self)

    def __str__(self):
        profesor_str = self._profesor_titular.nombre_completo if self._profesor_titular else "Sin asignar"
        return f"Asignatura: {self._nombre} ({self._codigo}) - Prof: {profesor_str}"

class Curso:
    def __init__(self, asignatura: Asignatura, semestre: int, anio: int):
        self._asignatura = asignatura
        self._semestre = semestre
        self._anio = anio
        self._alumnos_inscritos: List[Alumno] = []

    def inscribir_alumno(self, alumno: Alumno):
        if alumno not in self._alumnos_inscritos:
            self._alumnos_inscritos.append(alumno)
            print(f"Alumno {alumno.nombre_completo} inscrito en {self._asignatura.nombre}")
        else:
            print(f"El alumno {alumno.nombre_completo} ya está inscrito.")

    def listar_alumnos(self):
        print(f"Lista de alumnos en {self._asignatura.nombre} ({self._semestre}/{self._anio}):")
        for alumno in self._alumnos_inscritos:
            print(f"- {alumno}")

# Bloque de prueba
if __name__ == "__main__":
    print("=== EJEMPLO 1: Curso de CÁLCULO ===")
    # Crear Profesor
    profe_juan = Profesor("12345678-9", "Juan", "Pérez", date(1980, 5, 15), "PROF001", "Matemáticas")
    
    # Crear Asignatura
    calculo = Asignatura("MAT101", "Cálculo I", 10)
    
    # Asignar Profesor a Asignatura
    calculo.asignar_profesor(profe_juan)
    
    # Crear Alumnos
    alumno_ana = Alumno("20123456-7", "Ana", "Gómez", date(2000, 3, 10), "2023001", "Ingeniería")
    alumno_pedro = Alumno("20987654-3", "Pedro", "Soto", date(2001, 7, 22), "2023002", "Ingeniería")
    
    # Crear Curso
    curso_calculo_2024 = Curso(calculo, 1, 2024)
    
    # Inscribir Alumnos
    curso_calculo_2024.inscribir_alumno(alumno_ana)
    curso_calculo_2024.inscribir_alumno(alumno_pedro)
    
    # Mostrar información
    print("\n--- Información del Profesor ---")
    print(profe_juan)
    print("Dicta:", profe_juan.listar_asignaturas())
    
    print("\n--- Información del Curso ---")
    curso_calculo_2024.listar_alumnos()

    print("\n" + "="*30 + "\n")

    print("=== EJEMPLO 2: Curso de PROGRAMACIÓN (Nuevo Profesor y Asignatura) ===")
    profe_maria = Profesor("98765432-1", "María", "López", date(1985, 8, 20), "PROF002", "Informática")
    programacion = Asignatura("INF101", "Programación Python", 8)
    programacion.asignar_profesor(profe_maria)
    
    curso_progra = Curso(programacion, 1, 2024)
    alumno_lucas = Alumno("21456789-0", "Lucas", "Díaz", date(2002, 11, 5), "2023003", "Informática")
    
    curso_progra.inscribir_alumno(alumno_lucas)
    curso_progra.inscribir_alumno(alumno_ana) # Ana toma dos cursos
    
    print(f"Profesor: {profe_maria}")
    curso_progra.listar_alumnos()

    print("\n" + "="*30 + "\n")

    print("=== EJEMPLO 3: Alumno tomando MÚLTIPLES cursos (Verificación) ===")
    # Ana está en Cálculo y Programación. Verifiquemos imprimiendo un resumen manual
    print(f"Resumen para {alumno_ana.nombre_completo}:")
    print("Cursos inscritos (simulado):")
    print(f"- {calculo.nombre}")
    print(f"- {programacion.nombre}")
    alumno_ana.estudiar("Programación Avanzada")

    print("\n" + "="*30 + "\n")

    print("=== EJEMPLO 4: Profesor Multidisciplinario (Un profe, varias asignaturas) ===")
    # El profesor Juan Pérez ahora también dictará Álgebra
    algebra = Asignatura("MAT102", "Álgebra Lineal", 8)
    algebra.asignar_profesor(profe_juan)
    
    print(f"Actualización del Profesor {profe_juan.nombre_completo}:")
    print("Ahora dicta las siguientes asignaturas:")
    for asig in profe_juan.listar_asignaturas():
        print(f" -> {asig}")
