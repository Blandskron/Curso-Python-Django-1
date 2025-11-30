# Ejemplo 8: Colaboración mediante mensajes

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class CarritoColaborador:
    def __init__(self):
        self._items: list[Producto] = []

    def agregar(self, producto: Producto):
        self._items.append(producto)

    def total(self):
        return sum(p.precio for p in self._items)

    def listar(self):
        for p in self._items:
            print(p.nombre, p.precio)

p1 = Producto("Libro", 15)
p2 = Producto("Mouse", 25)
carrito2 = CarritoColaborador()
carrito2.agregar(p1)
carrito2.agregar(p2)
carrito2.listar()
print(carrito2.total())