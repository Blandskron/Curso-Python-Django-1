# Ejemplo 24: Duck typing (si camina como pato...)
class Pato:
    def volar(self):
        print("Pato volando")

class Avion:
    def volar(self):
        print("Avión volando")

def hacer_volar(objeto):
    objeto.volar()  # No importa el tipo, solo que tenga el método

hacer_volar(Pato())
hacer_volar(Avion())
