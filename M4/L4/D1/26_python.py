# Ejemplo 26: Método plantilla (Template Method)

from abc import ABC, abstractmethod


class ProcesadorArchivo(ABC):
    def procesar(self, ruta: str) -> None:
        contenido = self._leer(ruta)
        contenido = self._transformar(contenido)
        self._guardar(contenido)

    def _leer(self, ruta: str) -> str:
        return "contenido"  # simula lectura

    @abstractmethod
    def _transformar(self, contenido: str) -> str:
        ...

    def _guardar(self, contenido: str) -> None:
        # aquí se podría escribir a disco
        pass


class ProcesadorMayus(ProcesadorArchivo):
    def _transformar(self, contenido: str) -> str:
        return contenido.upper()
