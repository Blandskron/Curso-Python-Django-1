"""
main.py
Script de demostración de:
- Interacción entre objetos
- Polimorfismo (Persona y subclases)
- Sobrecarga (simulada) en métodos de Curso y Matricula
"""

from datetime import date

from personas import Alumno, Profesor, Administrativo, Persona
from academia import (
    Carrera,
    Asignatura,
    PeriodoAcademico,
    Horario,
    Sala,
    Matricula,
    Evaluacion,
)


def demo_sistema() -> None:
    # ====== Configuración básica del sistema académico ======
    carrera = Carrera(codigo="INF", nombre="Ingeniería en Informática", duracion_semestres=8)
    asignatura = Asignatura(codigo="PROG101", nombre="Programación I", creditos=6)
    carrera.agregar_asignatura(asignatura)

    periodo = PeriodoAcademico(
        anio=2025,
        semestre=1,
        fecha_inicio=date(2025, 3, 1),
        fecha_fin=date(2025, 7, 31),
    )

    horario = Horario(dia_semana="Lunes", bloque="M1")
    sala = Sala(codigo="LAB-101", capacidad=30, tipo="Laboratorio")

    profesor = Profesor(
        rut="11.111.111-1",
        nombre="Ana Docente",
        email="ana@instituto.cl",
        titulo="Ingeniera en Computación",
        departamento="Informática",
    )

    # Curso (sección)
    curso = asignatura.crear_curso(
        seccion="001",
        profesor=profesor,
        periodo=periodo,
        cupo_maximo=3,
        sala=sala,
        horario=horario,
    )

    # ====== Creación de alumnos y administrativo ======
    alumno1 = Alumno(
        rut="22.222.222-2",
        nombre="Carlos Alumno",
        email="carlos@correo.cl",
        numero_matricula="A2025-001",
        fecha_ingreso=date(2025, 3, 1),
        estado="regular",
    )

    alumno2 = Alumno(
        rut="33.333.333-3",
        nombre="Beatriz Alumna",
        email="bea@correo.cl",
        numero_matricula="A2025-002",
        fecha_ingreso=date(2025, 3, 1),
        estado="regular",
    )

    admin = Administrativo(
        rut="44.444.444-4",
        nombre="Pedro Admin",
        email="pedro@instituto.cl",
        cargo="Secretario académico",
    )

    # ====== Polimorfismo: lista de Persona ======
    personas: list[Persona] = [profesor, alumno1, alumno2, admin]
    print("=== DEMO POLIMORFISMO PERSONA.mostrar_rol() ===")
    for p in personas:
        # Cada subclase implementa mostrar_rol de forma distinta
        print(f"{p}: {p.mostrar_rol()}")

    # ====== Interacción: login genérico ======
    print("\n=== DEMO login / logout ===")
    for p in personas:
        sesion = p.login(usuario=p.email, clave="secreto")
        print(f"{p.nombre} login: {sesion}")
        p.logout()

    # ====== Inscripción de alumnos en el curso ======
    print("\n=== INSCRIPCIÓN A CURSO ===")
    for a in (alumno1, alumno2):
        ok = curso.inscribir_alumno(a)
        estado = "OK" if ok else "SIN CUPO"
        print(f"Inscribir {a.nombre} en {asignatura.nombre} seccion {curso.seccion}: {estado}")

    print("\nAlumnos inscritos en el curso:")
    for a in curso.listar_alumnos():
        print("-", a.nombre)

    # ====== Matriculas y sobrecarga en calcular_arancel ======
    print("\n=== MATRÍCULAS ===")
    matricula1 = Matricula(
        id_matricula=1,
        alumno=alumno1,
        curso=curso,
        periodo=periodo,
        fecha=date(2025, 3, 2),
        estado="vigente",
        arancel_base=500000.0,
    )
    matricula2 = Matricula(
        id_matricula=2,
        alumno=alumno2,
        curso=curso,
        periodo=periodo,
        fecha=date(2025, 3, 2),
        estado="vigente",
        arancel_base=500000.0,
    )

    print(
        f"Arancel {alumno1.nombre} sin descuento: "
        f"{matricula1.calcular_arancel():,.0f}"
    )
    print(
        f"Arancel {alumno2.nombre} con 20% descuento: "
        f"{matricula2.calcular_arancel(descuento=0.2):,.0f}"
    )

    # ====== Evaluaciones, notas y sobrecarga en calcular_promedio ======
    print("\n=== EVALUACIONES Y NOTAS ===")
    eval1 = Evaluacion(id_evaluacion=1, nombre="Control 1", fecha=date(2025, 4, 10), ponderacion=0.3)
    eval2 = Evaluacion(id_evaluacion=2, nombre="Examen", fecha=date(2025, 7, 20), ponderacion=0.7)

    curso.agregar_evaluacion(eval1)
    curso.agregar_evaluacion(eval2)

    # Registrar notas
    curso.registrar_nota(alumno1, eval1, 6.0)
    curso.registrar_nota(alumno1, eval2, 5.0)

    curso.registrar_nota(alumno2, eval1, 4.0)
    curso.registrar_nota(alumno2, eval2, 3.0)

    # Promedios por alumno (sobrecarga con parámetro)
    prom1 = curso.calcular_promedio(alumno=alumno1)
    prom2 = curso.calcular_promedio(alumno=alumno2)

    print(f"Promedio final {alumno1.nombre}: {prom1:.2f}")
    print(f"Promedio final {alumno2.nombre}: {prom2:.2f}")

    # Promedio del curso (sobrecarga sin parámetro)
    prom_curso = curso.calcular_promedio()
    print(f"Promedio general del curso: {prom_curso:.2f}")


if __name__ == "__main__":
    demo_sistema()
