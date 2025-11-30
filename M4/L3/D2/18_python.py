# Ejemplo 18: Clase abstracta usando abc (clase en cursiva en UML)
from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def guardar(self, entidad: object) -> None:
        ...

class RepositorioMemoria(Repositorio):
    def __init__(self):
        self._datos: list[object] = []

    def guardar(self, entidad: object) -> None:
        self._datos.append(entidad)
