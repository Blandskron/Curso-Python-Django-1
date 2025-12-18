"""
Módulo tienda.

Define la clase Tienda, que actúa como orquestador principal
del sistema de e-commerce por consola.
"""

from models.catalogo import Catalogo
from models.producto import Producto
from models.user.usuario import Admin, Cliente


class Tienda:
    """
    Representa la tienda y controla el flujo principal
    de la aplicación (menús, roles y operaciones).
    """

    def __init__(self):
        """
        Inicializa la tienda con un catálogo y productos base.
        """
        self.catalogo = Catalogo()
        self._cargar_productos_iniciales()

    def _cargar_productos_iniciales(self):
        """
        Carga productos iniciales en el catálogo.

        Este método simula una base de datos inicial.
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
            self.catalogo.agregar_producto_nuevo(producto, stock)

    # --------- MENÚ PRINCIPAL ---------

    def ejecutar(self):
        """
        Ejecuta el menú principal de la tienda.
        """
        while True:
            print("\n=== TIENDA ===")
            print("1) Entrar como ADMIN")
            print("2) Entrar como CLIENTE")
            print("0) Salir")

            op = input("Opción: ").strip()

            if op == "1":
                admin = Admin("Admin", "admin@tienda.com")
                self.menu_admin(admin)

            elif op == "2":
                nombre = input("Nombre cliente: ").strip()
                email = input("Email cliente: ").strip()
                cliente = Cliente(nombre, email)
                self.menu_cliente(cliente)

            elif op == "0":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida.")

    # --------- MENÚ ADMIN ---------

    def menu_admin(self, admin):
        """
        Menú de administración del catálogo.

        Args:
            admin (Admin): Usuario administrador.
        """
        while True:
            print("\n--- MENÚ ADMIN ---")
            print("1) Listar catálogo")
            print("2) Crear producto")
            print("3) Actualizar producto")
            print("4) Eliminar producto")
            print("5) Sumar stock")
            print("0) Volver")

            op = input("Opción: ").strip()

            try:
                if op == "1":
                    self.catalogo.listar()

                elif op == "2":
                    producto_id = input("ID: ").strip()
                    nombre = input("Nombre: ").strip()
                    categoria = input("Categoría: ").strip()
                    precio = input("Precio: ").strip()
                    stock = input("Stock inicial: ").strip()

                    producto = Producto(producto_id, nombre, categoria, precio)
                    self.catalogo.agregar_producto_nuevo(producto, stock)
                    print("Producto creado correctamente.")

                elif op == "3":
                    pid = input("ID producto: ").strip()
                    nombre = input("Nuevo nombre (enter para omitir): ")
                    categoria = input("Nueva categoría (enter para omitir): ")
                    precio = input("Nuevo precio (enter para omitir): ")

                    self.catalogo.actualizar_producto(
                        pid, nombre=nombre, categoria=categoria, precio=precio
                    )
                    print("Producto actualizado.")

                elif op == "4":
                    pid = input("ID producto: ").strip()
                    self.catalogo.eliminar_producto(pid)
                    print("Producto eliminado.")

                elif op == "5":
                    pid = input("ID producto: ").strip()
                    cant = input("Cantidad a sumar: ").strip()
                    self.catalogo.sumar_stock(pid, cant)
                    print("Stock actualizado.")

                elif op == "0":
                    break

                else:
                    print("Opción inválida.")

            except ValueError as e:
                print(f"Error: {e}")

    # --------- MENÚ CLIENTE ---------

    def menu_cliente(self, cliente):
        """
        Menú de operaciones para clientes.

        Args:
            cliente (Cliente): Cliente actual.
        """
        while True:
            print(f"\n--- MENÚ CLIENTE ({cliente.nombre}) ---")
            print("1) Ver catálogo")
            print("2) Buscar producto")
            print("3) Agregar al carrito")
            print("4) Ver carrito")
            print("5) Confirmar compra")
            print("0) Volver")

            op = input("Opción: ").strip()

            try:
                if op == "1":
                    self.catalogo.listar()

                elif op == "2":
                    texto = input("Buscar: ").strip()
                    resultados = self.catalogo.buscar(texto)

                    if not resultados:
                        print("No se encontraron productos.")
                    else:
                        print("\n--- RESULTADOS ---")
                        for data in resultados:
                            producto = data["producto"]
                            stock = data["stock"]
                            print(f"{producto} | Stock: {stock}")

                elif op == "3":
                    pid = input("ID producto: ").strip()
                    cant = input("Cantidad: ").strip()

                    if not self.catalogo.existe(pid):
                        print("Producto no existe.")
                        continue

                    if not self.catalogo.hay_stock(pid, cant):
                        print("No hay stock suficiente.")
                        continue

                    # Se descuenta stock y se agrega al carrito
                    self.catalogo.descontar_stock(pid, cant)
                    cliente.carrito.agregar(pid, cant)
                    print("Producto agregado al carrito.")

                elif op == "4":
                    cliente.carrito.ver_detalle(self.catalogo)

                elif op == "5":
                    if cliente.carrito.esta_vacio():
                        print("El carrito está vacío.")
                        continue

                    total = cliente.carrito.ver_detalle(self.catalogo)
                    ok = input("¿Confirmar compra? (s/n): ").lower()

                    if ok == "s":
                        cliente.carrito.vaciar()
                        print(f"Compra confirmada. Total: ${total:.0f}")
                    else:
                        print("Compra cancelada.")

                elif op == "0":
                    break

                else:
                    print("Opción inválida.")

            except ValueError as e:
                print(f"Error: {e}")
