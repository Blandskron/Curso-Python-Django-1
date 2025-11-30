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

# Ejemplo 16: Jerarquía de empleados con herencia multinivel

class EmpleadoPorHoras(Pagable):
    def __init__(self, tarifa: float, horas: float):
        self.tarifa = tarifa
        self.horas = horas

    def calcular_pago(self) -> float:
        return self.tarifa * self.horas


class EmpleadoComisionFijo(EmpleadoFijo):
    def __init__(self, sueldo_mensual: float, porcentaje: float, ventas: float):
        super().__init__(sueldo_mensual)
        self.porcentaje = porcentaje
        self.ventas = ventas

    def calcular_pago(self) -> float:
        base = super().calcular_pago()
        return base + self.ventas * self.porcentaje

# Ejemplo 17: Sistema de nómina polimórfico

class Nomina:
    def procesar(self, items: list[Pagable]) -> float:
        total = 0.0
        for item in items:
            if isinstance(item, Pagable):
                total += item.calcular_pago()
        return total
