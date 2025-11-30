# Ejemplo 10: Composición Pedido -> LineaPedido
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

class LineaPedido:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self) -> float:
        return self.producto.precio * self.cantidad

class Pedido:
    def __init__(self, numero: int):
        self.numero = numero
        self.lineas: list[LineaPedido] = []

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        self.lineas.append(LineaPedido(producto, cantidad))  # composición

    def total(self) -> float:
        return sum(lp.subtotal() for lp in self.lineas)
