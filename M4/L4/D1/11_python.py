# Ejemplo 11: Duck Typing (tipado de pato)

class Circulo:
    def dibujar(self) -> None:
        print("Dibujando un círculo")


class Mapa:
    def dibujar(self) -> None:
        print("Dibujando un mapa")


def renderizar(objeto) -> None:
    # solo asumimos que existe dibujar()
    objeto.dibujar()


objetos = [Circulo(), Mapa()]
for o in objetos:
    renderizar(o)
