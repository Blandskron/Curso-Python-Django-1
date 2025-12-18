"""
Seed inicial del sistema.

Define productos base para poblar el catálogo al iniciar.
"""

from models.producto import Producto


def cargar_productos_iniciales(catalogo):
    """
    Carga productos iniciales en el catálogo.

    Args:
        catalogo (Catalogo): Instancia del catálogo.
    """
    iniciales = [
        (1, "Mouse", "Periféricos", 9990, 10),
        (2, "Teclado", "Periféricos", 14990, 8),
        (3, "Audífonos", "Audio", 19990, 6),
        (4, "Pendrive 64GB", "Almacenamiento", 8990, 12),
        (5, "Webcam", "Accesorios", 25990, 5),
    ]

    for producto_id, nombre, categoria, precio, stock in iniciales:
        producto = Producto(producto_id, nombre, categoria, precio)
        catalogo.agregar_producto_nuevo(producto, stock)
