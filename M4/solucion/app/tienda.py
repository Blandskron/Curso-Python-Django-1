"""
Orquestador principal de la aplicación de e-commerce por consola.

Este módulo coordina menús, flujos y acciones entre
catálogo, usuarios y casos de uso.
"""

from models.catalogo import Catalogo
from models.user.usuario import Cliente

from app.seed import cargar_productos_iniciales
from app.menus import menu_principal, menu_admin, menu_cliente
from app.admin_actions import (
    listar_catalogo,
    crear_producto,
    actualizar_producto,
    eliminar_producto,
    sumar_stock,
)
from app.cliente_actions import (
    ver_catalogo,
    buscar_producto,
    agregar_al_carrito,
    ver_carrito,
    confirmar_compra,
)


class Tienda:
    """
    Controla el flujo principal de la aplicación (roles y menús).
    """

    def __init__(self):
        """
        Inicializa la tienda con un catálogo cargado.
        """
        self.catalogo = Catalogo()
        cargar_productos_iniciales(self.catalogo)

    def ejecutar(self):
        """
        Ejecuta el loop principal de la aplicación.
        """
        while True:
            op = menu_principal()

            if op == "1":
                self._ejecutar_admin()

            elif op == "2":
                self._ejecutar_cliente()

            elif op == "0":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida.")

    def _ejecutar_admin(self):
        """
        Ejecuta el menú del rol administrador.
        """
        while True:
            op = menu_admin()
            try:
                if op == "1":
                    listar_catalogo(self.catalogo)
                elif op == "2":
                    crear_producto(self.catalogo)
                elif op == "3":
                    actualizar_producto(self.catalogo)
                elif op == "4":
                    eliminar_producto(self.catalogo)
                elif op == "5":
                    sumar_stock(self.catalogo)
                elif op == "0":
                    break
                else:
                    print("Opción inválida.")
            except ValueError as e:
                print(f"Error: {e}")

    def _ejecutar_cliente(self):
        """
        Ejecuta el menú del rol cliente.
        """
        nombre = input("Nombre cliente: ").strip()
        email = input("Email cliente: ").strip()
        cliente = Cliente(nombre, email)

        while True:
            op = menu_cliente(cliente.nombre)
            try:
                if op == "1":
                    ver_catalogo(self.catalogo)
                elif op == "2":
                    buscar_producto(self.catalogo)
                elif op == "3":
                    agregar_al_carrito(self.catalogo, cliente)
                elif op == "4":
                    ver_carrito(self.catalogo, cliente)
                elif op == "5":
                    confirmar_compra(self.catalogo, cliente)
                elif op == "0":
                    break
                else:
                    print("Opción inválida.")
            except ValueError as e:
                print(f"Error: {e}")
