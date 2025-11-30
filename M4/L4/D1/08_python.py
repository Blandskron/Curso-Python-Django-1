# Ejemplo 8: Llamada directa al padre (no recomendado con múltiple)

class Padre:
    def __init__(self) -> None:
        self.valor = 1


class Hijo(Padre):
    def __init__(self) -> None:
        Padre.__init__(self)  # acopla al nombre concreto
        self.valor *= 2
