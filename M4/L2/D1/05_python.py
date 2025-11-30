# =====================================
# Ejemplo 5: Constructor con composición y parámetro mutable evitado
# =====================================

class Carrito:
    def __init__(self, items=None):
        # patrón correcto con None para evitar lista compartida
        self.items = [] if items is None else list(items)

    def agregar(self, producto):
        self.items.append(producto)

c1 = Carrito()
c2 = Carrito()
c1.agregar("Libro")
print(c1.items, c2.items)