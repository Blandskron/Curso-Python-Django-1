# Ejemplo 34: Polimorfismo con colección heterogénea de formas

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


class RectanguloConNombre(FiguraConNombre):
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def area(self) -> float:
        return self.ancho * self.alto


figuras: list[FiguraConNombre] = [
    CirculoConNombre(1.0),
    RectanguloConNombre(2.0, 3.0),
]

for f in figuras:
    print(str(f))
