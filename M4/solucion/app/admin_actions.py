"""
Acciones del rol administrador.
"""

from ui.catalogo_view import mostrar_catalogo
from models.producto import Producto


def listar_catalogo(catalogo):
    mostrar_catalogo(catalogo)


def crear_producto(catalogo):
    producto_id = input("ID: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio = input("Precio: ").strip()
    stock = input("Stock inicial: ").strip()

    producto = Producto(producto_id, nombre, categoria, precio)
    catalogo.agregar_producto_nuevo(producto, stock)
    print("Producto creado correctamente.")


def actualizar_producto(catalogo):
    pid = input("ID producto: ").strip()
    nombre = input("Nuevo nombre (enter para omitir): ")
    categoria = input("Nueva categoría (enter para omitir): ")
    precio = input("Nuevo precio (enter para omitir): ")

    catalogo.actualizar_producto(pid, nombre=nombre, categoria=categoria, precio=precio)
    print("Producto actualizado.")


def eliminar_producto(catalogo):
    pid = input("ID producto: ").strip()
    catalogo.eliminar_producto(pid)
    print("Producto eliminado.")


def sumar_stock(catalogo):
    pid = input("ID producto: ").strip()
    cant = input("Cantidad a sumar: ").strip()
    catalogo.sumar_stock(pid, cant)
    print("Stock actualizado.")
