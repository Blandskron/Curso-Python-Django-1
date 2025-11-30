# Ejemplo 35: Composición para compartir comportamiento entre tipos distintos

from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar(self, monto: float) -> float:
        ...


class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje

    def aplicar(self, monto: float) -> float:
        return monto * (1 - self.porcentaje)


class PedidoConDescuento:
    def __init__(self, monto: float, estrategia: EstrategiaDescuento):
        self.monto = monto
        self.estrategia = estrategia

    def total(self) -> float:
        return self.estrategia.aplicar(self.monto)
