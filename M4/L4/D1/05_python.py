# Ejemplo 5: Herencia múltiple simple

class Volador:
    def mover(self) -> str:
        return "Me desplazo volando"


class Nadador:
    def mover(self) -> str:
        return "Me desplazo nadando"


class Anfibio(Volador, Nadador):
    pass  # hereda el método mover de Volador primero


anfibio = Anfibio()
resultado = anfibio.mover()
