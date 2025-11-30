# Ejemplo 17: Polimorfismo con Figura y subclases
class Figura:
    def area(self) -> float:
        raise NotImplementedError

class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return 3.14 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def area(self) -> float:
        return self.ancho * self.alto
