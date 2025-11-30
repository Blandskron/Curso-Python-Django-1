# Ejemplo 12: Polimorfismo nominal (clase base explícita)

class Forma:
    def dibujar(self) -> None:
        raise NotImplementedError


class Triangulo(Forma):
    def dibujar(self) -> None:
        print("Dibujando triángulo")


class Cuadrado(Forma):
    def dibujar(self) -> None:
        print("Dibujando cuadrado")
