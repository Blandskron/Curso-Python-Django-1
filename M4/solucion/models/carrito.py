"""
Módulo carrito.

Define la clase Carrito, responsable de gestionar los productos
seleccionados por el cliente antes de la compra.
"""

from models.catalogo import Catalogo


class Carrito:
    """
    Representa el carrito de compras de un cliente.

    El carrito solo almacena IDs de productos y cantidades.
    La información del producto se obtiene desde el catálogo.
    """

    def __init__(self):
        """
        Inicializa un carrito vacío.

        Estructura interna:
            {
                producto_id: cantidad
            }
        """
        self.items = {}

    def esta_vacio(self):
        """
        Verifica si el carrito está vacío.

        Returns:
            bool: True si no hay productos.
        """
        return len(self.items) == 0

    def agregar(self, producto_id, cantidad):
        """
        Agrega un producto al carrito o incrementa su cantidad.

        No valida stock disponible; esa responsabilidad
        pertenece al catálogo al momento de confirmar la compra.

        Args:
            producto_id (int | str): ID del producto.
            cantidad (int | str): Cantidad a agregar.

        Raises:
            ValueError: Si la cantidad es inválida.
        """
        producto_id = int(producto_id)
        cantidad = int(cantidad)

        if cantidad <= 0:
            raise ValueError("Cantidad debe ser > 0.")

        self.items[producto_id] = self.items.get(producto_id, 0) + cantidad

    def vaciar(self):
        """
        Vacía completamente el carrito.
        """
        self.items = {}

    def ver_detalle(self, catalogo: Catalogo):
        """
        Muestra el detalle del carrito y calcula el total.

        Si un producto ya no existe en el catálogo (por ejemplo,
        fue eliminado por un administrador), se ignora.

        Args:
            catalogo (Catalogo): Catálogo de productos.

        Returns:
            float: Total a pagar.
        """
        if self.esta_vacio():
            print("Carrito vacío.")
            return 0.0

        print("\n--- CARRITO ---")
        total = 0.0

        for producto_id, cantidad in self.items.items():
            if not catalogo.existe(producto_id):
                # El producto fue eliminado del catálogo
                continue

            producto = catalogo.obtener(producto_id)
            subtotal = producto.precio * cantidad
            total += subtotal

            print(
                f"{producto.nombre} | "
                f"Cant: {cantidad} | "
                f"Unit: ${producto.precio:.0f} | "
                f"Subtotal: ${subtotal:.0f}"
            )

        print(f"TOTAL A PAGAR: ${total:.0f}")
        return total
