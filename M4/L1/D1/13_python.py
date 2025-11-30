# Ejemplo 13: Identidad vs igualdad

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Punto(1, 2)
p2 = Punto(1, 2)

print(p1 == p2)     # igualdad por defecto: False (identidad)
print(id(p1), id(p2))

# redefiniendo __eq__ para igualdad lógica
class PuntoEq(Punto):
    def __eq__(self, other):
        return isinstance(other, PuntoEq) and self.x == other.x and self.y == other.y

q1 = PuntoEq(1, 2)
q2 = PuntoEq(1, 2)
print(q1 == q2)     # True: igualdad por estado
