from usuario import Usuario
from ..carrito import Carrito
from ..producto import Producto
from admin import Admin

class Cliente(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.carrito = Carrito()

    # --------- MENÚS ---------

    def ejecutar(self):
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

    def menu_admin(self, admin):
        while True:
            print("\n--- MENÚ ADMIN ---")
            print("1) Listar catálogo")
            print("2) Crear producto (id, nombre, categoría, precio, stock)")
            print("3) Actualizar producto (nombre/categoría/precio)")
            print("4) Eliminar producto")
            print("5) Sumar stock a producto existente")
            print("0) Volver")

            op = input("Opción: ").strip()

            try:
                if op == "1":
                    self.catalogo.listar()

                elif op == "2":
                    id = input("ID: ").strip()
                    nombre = input("Nombre: ").strip()
                    categoria = input("Categoría: ").strip()
                    precio = input("Precio: ").strip()
                    stock = input("Stock inicial: ").strip()
                    p = Producto(id, nombre, categoria, precio)
                    self.catalogo.agregar_producto_nuevo(p, stock)
                    print("Producto creado y agregado al catálogo.")

                elif op == "3":
                    pid = input("ID producto a actualizar: ").strip()
                    nombre = input("Nuevo nombre (enter para no cambiar): ")
                    categoria = input("Nueva categoría (enter para no cambiar): ")
                    precio = input("Nuevo precio (enter para no cambiar): ")
                    self.catalogo.actualizar_producto(pid, nombre=nombre, categoria=categoria, precio=precio)
                    print("Producto actualizado.")

                elif op == "4":
                    pid = input("ID producto a eliminar: ").strip()
                    self.catalogo.eliminar_producto(pid)
                    print("Producto eliminado del catálogo.")

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

    def menu_cliente(self, cliente):
        while True:
            print(f"\n--- MENÚ CLIENTE ({cliente.nombre}) ---")
            print("1) Ver catálogo")
            print("2) Buscar por nombre o categoría")
            print("3) Agregar al carrito (id, cantidad)")
            print("4) Ver carrito y total")
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
                            p = data["producto"]
                            stock = data["stock"]
                            print(f"{p} | Stock: {stock}")

                elif op == "3":
                    pid = input("ID producto: ").strip()
                    cant = input("Cantidad: ").strip()

                    if not self.catalogo.existe(pid):
                        print("Ese producto no existe en el catálogo.")
                        continue

                    if int(cant) <= 0:
                        print("Cantidad debe ser un entero > 0.")
                        continue

                    if not self.catalogo.hay_stock(pid, cant):
                        print("No hay stock suficiente.")
                        continue

                    # Descontar stock y agregar al carrito
                    self.catalogo.descontar_stock(pid, cant)
                    cliente.carrito.agregar(pid, cant)
                    print("Producto agregado al carrito.")

                elif op == "4":
                    cliente.carrito.ver_detalle(self.catalogo)

                elif op == "5":
                    if cliente.carrito.esta_vacio():
                        print("El carrito está vacío. No puedes confirmar compra.")
                        continue
                    total = cliente.carrito.ver_detalle(self.catalogo)
                    ok = input("¿Confirmar compra? (s/n): ").strip().lower()
                    if ok == "s":
                        cliente.carrito.vaciar()
                        print(f"Compra confirmada. Total pagado: ${total:.0f}. Carrito vaciado.")
                    else:
                        print("Compra cancelada.")

                elif op == "0":
                    break
                else:
                    print("Opción inválida.")

            except ValueError as e:
                print(f"Error: {e}")