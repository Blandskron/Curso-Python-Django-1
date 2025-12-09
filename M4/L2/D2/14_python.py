# =====================================
# Ejemplo 14: Sobrecarga por tipo con singledispatch
# =====================================

from functools import singledispatchmethod

class Formateador:
    @singledispatchmethod
    def formatear(self, dato):
        print(f"Valor genérico: {dato}")

    @formatear.register
    def _(self, dato: int):
        print(f"Entero: {dato}")

    @formatear.register
    def _(self, dato: str):
        print(f"Cadena: {dato.upper()}")

fmt = Formateador()
fmt.formatear(10)
fmt.formatear("hola")
fmt.formatear(3.14)
