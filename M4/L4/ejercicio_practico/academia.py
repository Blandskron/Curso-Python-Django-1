"""
academia.py
Clases del dominio académico:
- Carrera
- Asignatura
- PeriodoAcademico
- Horario
- Sala
- Curso
- Matricula
- Evaluacion
- Nota
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Dict, List, Optional

from personas import Alumno, Profesor


class Carrera:
    def __init__(self, codigo: str, nombre: str, duracion_semestres: int) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.duracion_semestres = duracion_semestres
        self._asignaturas: List[Asignatura] = []

    def agregar_asignatura(self, asignatura: "Asignatura") -> None:
        self._asignaturas.append(asignatura)

    def obtener_malla(self) -> List["Asignatura"]:
        return list(self._asignaturas)


class Asignatura:
    def __init__(self, codigo: str, nombre: str, creditos: int) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self._cursos: List[Curso] = []

    def crear_curso(
        self,
        seccion: str,
        profesor: Profesor,
        periodo: "PeriodoAcademico",
        cupo_maximo: int,
        sala: "Sala",
        horario: "Horario",
    ) -> "Curso":
        """
        Crea una nueva sección (Curso) de esta asignatura.
        Aquí se evidencia la relación de composición Asignatura- Curso.
        """
        nuevo_id = len(self._cursos) + 1
        curso = Curso(
            id_curso=nuevo_id,
            asignatura=self,
            seccion=seccion,
            profesor=profesor,
            periodo=periodo,
            cupo_maximo=cupo_maximo,
            sala=sala,
            horario=horario,
        )
        self._cursos.append(curso)
        return curso

    def cursos(self) -> List["Curso"]:
        return list(self._cursos)


class PeriodoAcademico:
    def __init__(self, anio: int, semestre: int, fecha_inicio: date, fecha_fin: date) -> None:
        self.anio = anio
        self.semestre = semestre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def es_fecha_valida(self, fecha: date) -> bool:
        return self.fecha_inicio <= fecha <= self.fecha_fin

    def __str__(self) -> str:
        return f"{self.anio}-{self.semestre}"


class Horario:
    def __init__(self, dia_semana: str, bloque: str) -> None:
        self.dia_semana = dia_semana
        self.bloque = bloque

    def solapa_con(self, otro: "Horario") -> bool:
        # Comparación simple: mismo día y mismo bloque
        return self.dia_semana == otro.dia_semana and self.bloque == otro.bloque

    def __str__(self) -> str:
        return f"{self.dia_semana} {self.bloque}"


class Sala:
    def __init__(self, codigo: str, capacidad: int, tipo: str) -> None:
        self.codigo = codigo
        self.capacidad = capacidad
        self.tipo = tipo

    def esta_disponible(self, fecha: date, bloque: str) -> bool:
        # Demo: siempre disponible
        return True

    def __str__(self) -> str:
        return f"Sala {self.codigo} ({self.tipo}, cap. {self.capacidad})"


class Curso:
    """
    Sección de una asignatura.
    """

    def __init__(
        self,
        id_curso: int,
        asignatura: Asignatura,
        seccion: str,
        profesor: Profesor,
        periodo: PeriodoAcademico,
        cupo_maximo: int,
        sala: Sala,
        horario: Horario,
    ) -> None:
        self.id_curso = id_curso
        self.asignatura = asignatura
        self.seccion = seccion
        self.profesor = profesor
        self.periodo = periodo
        self.cupo_maximo = cupo_maximo
        self.sala = sala
        self.horario = horario
        self._alumnos: List[Alumno] = []
        self._evaluaciones: List[Evaluacion] = []

        # notas[alumno][evaluacion] = Nota
        self._notas: Dict[Alumno, Dict[Evaluacion, Nota]] = {}

    # ----------------------------------------------------------
    # Interacción: inscribir alumno
    # ----------------------------------------------------------
    def inscribir_alumno(self, alumno: Alumno) -> bool:
        if len(self._alumnos) >= self.cupo_maximo:
            return False
        if alumno in self._alumnos:
            return False
        self._alumnos.append(alumno)
        alumno.inscribirse_curso(self)
        self._notas[alumno] = {}
        return True

    def listar_alumnos(self) -> List[Alumno]:
        return list(self._alumnos)

    # ----------------------------------------------------------
    # Evaluaciones y sobrecarga simulada
    # ----------------------------------------------------------
    def agregar_evaluacion(self, evaluacion: "Evaluacion") -> None:
        self._evaluaciones.append(evaluacion)
        for alumno in self._alumnos:
            self._notas[alumno].setdefault(evaluacion, Nota(0.0))

    def registrar_nota(self, alumno: Alumno, evaluacion: "Evaluacion", valor: float) -> None:
        if alumno not in self._alumnos or evaluacion not in self._evaluaciones:
            return
        self._notas[alumno][evaluacion] = Nota(valor)

    def _promedio_alumno(self, alumno: Alumno) -> float:
        notas_evals = self._notas.get(alumno, {})
        if not notas_evals:
            return 0.0
        total = 0.0
        for ev, nota in notas_evals.items():
            total += nota.valor * ev.ponderacion
        return total

    def _promedio_curso(self) -> float:
        if not self._alumnos:
            return 0.0
        suma = sum(self._promedio_alumno(a) for a in self._alumnos)
        return suma / len(self._alumnos)

    def calcular_promedio(self, alumno: Optional[Alumno] = None) -> float:
        """
        'Sobrecarga' por parámetro opcional:
        - Si se entrega un alumno -> promedio de ese alumno.
        - Si no se entrega -> promedio general del curso.
        """
        if alumno is not None:
            return self._promedio_alumno(alumno)
        return self._promedio_curso()


class Matricula:
    def __init__(
        self,
        id_matricula: int,
        alumno: Alumno,
        curso: Curso,
        periodo: PeriodoAcademico,
        fecha: date,
        estado: str,
        arancel_base: float,
    ) -> None:
        self.id_matricula = id_matricula
        self.alumno = alumno
        self.curso = curso
        self.periodo = periodo
        self.fecha = fecha
        self.estado = estado
        self.arancel_base = arancel_base

    def calcular_arancel(self, descuento: float = 0.0) -> float:
        """
        'Sobrecarga' simulada:
        - Sin descuento (0.0): retorna arancel base.
        - Con descuento: aplica porcentaje (0.0 a 1.0).
        """
        if descuento <= 0:
            return self.arancel_base
        return self.arancel_base * (1 - descuento)


@dataclass
class Evaluacion:
    id_evaluacion: int
    nombre: str
    fecha: date
    ponderacion: float  # 0..1

    def es_aprobatoria(self, nota: float) -> bool:
        # ejemplo simple: >= 4.0
        return nota >= 4.0


@dataclass
class Nota:
    valor: float

    def es_aprobada(self) -> bool:
        return self.valor >= 4.0
