from producto import Producto
from catalogo import Catalogo

class Tienda:
    def __init__(self):
        self.catalogo = Catalogo()
        self._cargar_productos_iniciales()

    def _cargar_productos_iniciales(self):
        iniciales = [
            (1, "Mouse", "Periféricos", 9990, 10),
            (2, "Teclado", "Periféricos", 14990, 8),
            (3, "Audífonos", "Audio", 19990, 6),
            (4, "Pendrive 64GB", "Almacenamiento", 8990, 12),
            (5, "Webcam", "Accesorios", 25990, 5),
        ]
        for id, nombre, categoria, precio, stock in iniciales:
            self.catalogo.agregar_producto_nuevo(Producto(id, nombre, categoria, precio), stock)
