"""
Módulo producto.

Define la clase Producto, que representa un ítem del catálogo
del sistema de e-commerce.
"""


class Producto:
    """
    Representa un producto disponible para la venta.

    Atributos:
        producto_id (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        categoria (str): Categoría a la que pertenece.
        precio (float): Precio unitario del producto.
    """

    def __init__(self, producto_id, nombre, categoria, precio):
        """
        Inicializa un producto con sus datos básicos.

        Args:
            producto_id (int | str): Identificador del producto.
            nombre (str): Nombre del producto.
            categoria (str): Categoría del producto.
            precio (float | int | str): Precio del producto.
        """
        # Se convierten los valores para asegurar consistencia de tipos
        self.producto_id = int(producto_id)
        self.nombre = str(nombre)
        self.categoria = str(categoria)
        self.precio = float(precio)

    def __repr__(self):
        """
        Representación informal del producto.

        Se utiliza principalmente para mostrar el producto
        en listados por consola y debugging.
        """
        return (
            f"[{self.producto_id}] "
            f"{self.nombre} | {self.categoria} | "
            f"${self.precio:.0f}"
        )
