# =====================================
# Ejemplo 9: Propiedad de solo lectura + calculada
# =====================================

class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @property
    def area(self):
        return self._ancho * self._alto

r = Rectangulo(2, 5)
print(r.area)
