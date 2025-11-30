# Ejemplo 4: Invariante de clase + encapsulamiento

class Rectangulo:
    def __init__(self, ancho, alto):
        # invariante: ancho y alto > 0
        if ancho <= 0 or alto <= 0:
            raise ValueError("Dimensiones deben ser positivas")
        self.__ancho = ancho      # atributo encapsulado
        self.__alto = alto

    def area(self):
        return self.__ancho * self.__alto

    def escalar(self, factor):
        if factor <= 0:
            raise ValueError("Factor debe ser positivo")
        self.__ancho *= factor
        self.__alto *= factor

r = Rectangulo(2, 3)
print(r.area())
r.escalar(2)
print(r.area())