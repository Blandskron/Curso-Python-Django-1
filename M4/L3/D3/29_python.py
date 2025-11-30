# Ejemplo 29: Método protegido reutilizado por subclase
class Procesador:
    def procesar(self, datos: list[int]) -> int:
        return self._calcular(datos)

    def _calcular(self, datos: list[int]) -> int:
        return sum(datos)

class ProcesadorPromedio(Procesador):
    def _calcular(self, datos: list[int]) -> int:
        return int(super()._calcular(datos) / len(datos))
