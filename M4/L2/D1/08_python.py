# =====================================
# Ejemplo 8: Misma idea usando @property (pythonico)
# =====================================

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("Nombre vacío")
        self._nombre = valor

p = Persona("Ana")
p.nombre = "Ana María"  # valida en el setter
print(p.nombre)
