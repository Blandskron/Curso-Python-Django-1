"""
o agregar/eliminar/actualizar producto,
o agregar al carrito,
o calcular total,
o guardar/leer de archivo, etc.
"""
class Carrito:
    def __init__(self, items=None):
        # patrón correcto con None para evitar lista compartida
        self.items = [] if items is None else list(items)

    def agregar(self, producto):
        self.items.append(producto)

    def eliminar(self, producto):
        self.items.pop(producto)
