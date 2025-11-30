"""
personas.py
Clases relacionadas con personas del sistema educacional:
- Persona (abstracta)
- Alumno
- Profesor
- Administrativo
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from academia import Curso



class Persona(ABC):
    """
    Clase abstracta base para Alumno, Profesor y Administrativo.
    """

    def __init__(self, rut: str, nombre: str, email: str) -> None:
        self._rut = rut
        self._nombre = nombre
        self._email = email
        self._sesion_activa = False

    @property
    def rut(self) -> str:
        return self._rut

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def email(self) -> str:
        return self._email

    def login(self, usuario: str, clave: str) -> bool:
        """
        Implementación simple de login.
        En un caso real se validaría contra una base de datos / hash.
        """
        if usuario == self._email and bool(clave):
            self._sesion_activa = True
        return self._sesion_activa

    def logout(self) -> None:
        self._sesion_activa = False

    @abstractmethod
    def mostrar_rol(self) -> str:
        """Método abstracto para demostrar polimorfismo."""
        ...

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._rut} - {self._nombre})"


class Alumno(Persona):
    def __init__(
        self,
        rut: str,
        nombre: str,
        email: str,
        numero_matricula: str,
        fecha_ingreso: date,
        estado: str,
    ) -> None:
        super().__init__(rut, nombre, email)
        self._numero_matricula = numero_matricula
        self._fecha_ingreso = fecha_ingreso
        self._estado = estado
        # cursos inscritos (se cargan desde academia.Curso)
        self._cursos: List[Curso] = []

    def inscribirse_curso(self, curso: Curso) -> None:
        self._cursos.append(curso)

    def cursos_inscritos(self) -> List["Curso"]:
        return list(self._cursos)

    def mostrar_rol(self) -> str:
        return f"Alumno regular ({self._estado})"


class Profesor(Persona):
    def __init__(self, rut: str, nombre: str, email: str, titulo: str, departamento: str) -> None:
        super().__init__(rut, nombre, email)
        self._titulo = titulo
        self._departamento = departamento

    def mostrar_rol(self) -> str:
        return f"Profesor de {self._departamento}"


class Administrativo(Persona):
    def __init__(self, rut: str, nombre: str, email: str, cargo: str) -> None:
        super().__init__(rut, nombre, email)
        self._cargo = cargo

    def mostrar_rol(self) -> str:
        return f"Administrativo ({self._cargo})"
