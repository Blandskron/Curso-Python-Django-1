"""
o Producto
o Catalogo (contiene muchos Producto)
o Carrito (contiene ítems de producto + cantidad)
o Usuario (clase base)
o Admin y Cliente (heredan de Usuario)
o Aplicacion o Tienda (coordina la ejecución y menús)
"""

from modelos.admin import Admin
from modelos.producto import Producto
from modelos.catalogo import Catalogo


class Carrito:
    pass

class Usuario:
    pass

class Cliente:
    pass

class Tienda:
    pass


admin_uno = Admin()
producto_1 = Producto()
catalogo = Catalogo()