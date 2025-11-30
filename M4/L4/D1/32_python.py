# Ejemplo 32: Uso de __str__ polimórfico

from abc import ABC, abstractmethod


class FiguraConNombre(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (area={self.area():.2f})"


class CirculoConNombre(FiguraConNombre):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return 3.14159 * self.radio ** 2
