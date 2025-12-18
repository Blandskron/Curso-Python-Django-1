"""
Lógica de inventario (stock).
"""

from .errores import (
    ProductoNoExisteError,
    CantidadInvalidaError,
    StockInsuficienteError,
)


class InventarioMixin:
    """
    Operaciones relacionadas con stock.
    """

    def obtener_stock(self, producto_id):
        return self.items[int(producto_id)]["stock"]

    def hay_stock(self, producto_id, cantidad):
        producto_id = int(producto_id)
        cantidad = int(cantidad)

        if producto_id not in self.items:
            return False

        return self.items[producto_id]["stock"] >= cantidad

    def sumar_stock(self, producto_id, cantidad):
        producto_id = int(producto_id)
        cantidad = int(cantidad)

        if producto_id not in self.items:
            raise ProductoNoExisteError("Producto no existe.")

        if cantidad <= 0:
            raise CantidadInvalidaError("Cantidad debe ser > 0.")

        self.items[producto_id]["stock"] += cantidad

    def descontar_stock(self, producto_id, cantidad):
        producto_id = int(producto_id)
        cantidad = int(cantidad)

        if cantidad <= 0:
            raise CantidadInvalidaError("Cantidad debe ser > 0.")

        if not self.hay_stock(producto_id, cantidad):
            raise StockInsuficienteError("No hay stock suficiente.")

        self.items[producto_id]["stock"] -= cantidad
