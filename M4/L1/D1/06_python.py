# Ejemplo 5: Método (implementación) vs Comportamiento (efecto observable)

class Figura:
    def area(self):
        raise NotImplementedError

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):  # método concreto
        from math import pi
        return pi * (self.radio ** 2)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

def imprimir_area(figura: Figura):
    # comportamiento polimórfico: mismo mensaje, distintos métodos
    print("Área:", figura.area())

f1 = Circulo(3)
f2 = Cuadrado(4)
imprimir_area(f1)
imprimir_area(f2)
# Ejemplo 6: Polimorfismo por sustitución

figuras: list[Figura] = [Circulo(1), Cuadrado(2), Circulo(3)]

for f in figuras:         # mismo código para tipos distintos
    print(type(f).__name__, f.area())