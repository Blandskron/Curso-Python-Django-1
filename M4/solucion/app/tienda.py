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
from utils.validaciones import email_valido
from utils.logger import LoggerTXT


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

        # Logger opcional (memoria)
        self.logger = LoggerTXT()
        self.logger.log("Aplicación iniciada")

    def ejecutar(self):
        """
        Ejecuta el loop principal de la aplicación.
        """
        while True:
            op = menu_principal()

            if op == "1":
                self.logger.log("Ingreso al menú ADMIN")
                self._ejecutar_admin()

            elif op == "2":
                self._ejecutar_cliente()

            elif op == "0":
                self.logger.log("Usuario seleccionó salir del sistema")
                self._cerrar_aplicacion()
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
                    self.logger.log("ADMIN listó el catálogo")

                elif op == "2":
                    crear_producto(self.catalogo)
                    self.logger.log("ADMIN creó un producto")

                elif op == "3":
                    actualizar_producto(self.catalogo)
                    self.logger.log("ADMIN actualizó un producto")

                elif op == "4":
                    eliminar_producto(self.catalogo)
                    self.logger.log("ADMIN eliminó un producto")

                elif op == "5":
                    sumar_stock(self.catalogo)
                    self.logger.log("ADMIN sumó stock a un producto")

                elif op == "0":
                    self.logger.log("ADMIN salió del menú administrador")
                    break

                else:
                    print("Opción inválida.")

            except ValueError as e:
                self.logger.log(f"Error en menú ADMIN: {e}")
                print(f"Error: {e}")

    def _ejecutar_cliente(self):
        """
        Ejecuta el menú del rol cliente.
        """
        nombre = input("Nombre cliente: ").strip()

        while True:
            email = input("Email cliente: ").strip()

            if not email_valido(email):
                print("Email inválido. Ejemplo válido: usuario@correo.com")
                continue

            break

        cliente = Cliente(nombre, email)
        self.logger.log(
            f"Cliente ingresó al sistema: {cliente.nombre} ({cliente.email})"
        )

        while True:
            op = menu_cliente(cliente.nombre)
            try:
                if op == "1":
                    ver_catalogo(self.catalogo)
                    self.logger.log("Cliente visualizó el catálogo")

                elif op == "2":
                    buscar_producto(self.catalogo)
                    self.logger.log("Cliente realizó una búsqueda")

                elif op == "3":
                    agregar_al_carrito(self.catalogo, cliente)
                    self.logger.log("Cliente agregó productos al carrito")

                elif op == "4":
                    ver_carrito(self.catalogo, cliente)
                    self.logger.log("Cliente visualizó el carrito")

                elif op == "5":
                    confirmar_compra(self.catalogo, cliente)
                    self.logger.log("Cliente confirmó la compra")

                elif op == "0":
                    self.logger.log(
                        f"Cliente salió del sistema: {cliente.nombre}"
                    )
                    break

                else:
                    print("Opción inválida.")

            except ValueError as e:
                self.logger.log(f"Error en menú CLIENTE: {e}")
                print(f"Error: {e}")

    def _cerrar_aplicacion(self):
        """
        Pregunta si se desea guardar el historial antes de salir.
        """
        guardar = input(
            "¿Desea guardar el historial de la sesión en un archivo .txt? (s/n): "
        ).lower()

        if guardar == "s":
            nombre_archivo = input(
                "Ingrese el nombre del archivo (sin extensión o con .txt): "
            ).strip()

            if not nombre_archivo:
                nombre_archivo = "historial_app.txt"
            elif not nombre_archivo.endswith(".txt"):
                nombre_archivo += ".txt"

            self.logger.log("Historial guardado por decisión del usuario")
            self.logger.guardar(nombre_archivo)

            print(f"📄 Historial guardado en '{nombre_archivo}'")
        else:
            print("Historial no guardado.")


        print("¡Hasta luego!")
