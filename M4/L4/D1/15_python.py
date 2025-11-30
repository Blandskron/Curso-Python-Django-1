# Ejemplo 15: Clase abstracta para pagos

from abc import ABC, abstractmethod

class Pagable(ABC):
    @abstractmethod
    def calcular_pago(self) -> float:
        ...


class EmpleadoFijo(Pagable):
    def __init__(self, sueldo_mensual: float):
        self.sueldo_mensual = sueldo_mensual

    def calcular_pago(self) -> float:
        return self.sueldo_mensual / 4.0
