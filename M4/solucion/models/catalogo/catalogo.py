"""
Catálogo de productos (dominio).

Gestiona productos y delega stock y consultas a mixins.
"""

from .consultas import ConsultasCatalogoMixin
from .inventario import InventarioMixin
from .errores import (
    ProductoNoExisteError,
    ProductoYaExisteError,
    CantidadInvalidaError,
)


class Catalogo(ConsultasCatalogoMixin, InventarioMixin):
    """
    Catálogo del e-commerce.

    Estructura interna:
        {
            producto_id: {
                "producto": Producto,
                "stock": int
            }
        }
    """

    def __init__(self):
        self.items = {}

    def existe(self, producto_id):
        return int(producto_id) in self.items

    def obtener(self, producto_id):
        if not self.existe(producto_id):
            raise ProductoNoExisteError("Producto no existe.")
        return self.items[int(producto_id)]["producto"]

    def agregar_producto_nuevo(self, producto, cantidad):
        if self.existe(producto.producto_id):
            raise ProductoYaExisteError("Ya existe un producto con ese ID.")

        cantidad = int(cantidad)
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser > 0.")

        self.items[producto.producto_id] = {
            "producto": producto,
            "stock": cantidad,
        }

    def actualizar_producto(self, producto_id, nombre=None, categoria=None, precio=None):
        producto_id = int(producto_id)

        if not self.existe(producto_id):
            raise ProductoNoExisteError("Producto no existe.")

        producto = self.items[producto_id]["producto"]

        if nombre:
            producto.nombre = str(nombre)

        if categoria:
            producto.categoria = str(categoria)

        if precio is not None and str(precio) != "":
            producto.precio = float(precio)

    def eliminar_producto(self, producto_id):
        producto_id = int(producto_id)

        if not self.existe(producto_id):
            raise ProductoNoExisteError("Producto no existe.")

        del self.items[producto_id]
