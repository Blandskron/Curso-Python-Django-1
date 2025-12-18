class Catalogo:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def agregar(self, producto):
        self.producto.append(producto)

    def eliminar(self, producto):
        self.producto.pop(producto)

    def actualizar(self, producto):
        self.producto.append(producto)