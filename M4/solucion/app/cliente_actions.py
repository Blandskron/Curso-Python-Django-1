"""
Acciones del rol cliente.
"""

from ui.catalogo_view import mostrar_catalogo, mostrar_resultados_busqueda


def ver_catalogo(catalogo):
    mostrar_catalogo(catalogo)


def buscar_producto(catalogo):
    texto = input("Buscar: ").strip()
    resultados = catalogo.buscar(texto)
    mostrar_resultados_busqueda(resultados)


def agregar_al_carrito(catalogo, cliente):
    pid = input("ID producto: ").strip()
    cant = input("Cantidad: ").strip()

    if not catalogo.hay_stock(pid, cant):
        print("No hay stock suficiente.")
        return

    catalogo.descontar_stock(pid, cant)
    cliente.carrito.agregar(pid, cant)
    print("Producto agregado al carrito.")


def ver_carrito(catalogo, cliente):
    cliente.carrito.ver_detalle(catalogo)


def confirmar_compra(catalogo, cliente):
    if cliente.carrito.esta_vacio():
        print("El carrito está vacío.")
        return

    total = cliente.carrito.ver_detalle(catalogo)
    ok = input("¿Confirmar compra? (s/n): ").strip().lower()

    if ok == "s":
        cliente.carrito.vaciar()
        print(f"Compra confirmada. Total: ${total:.0f}")
    else:
        print("Compra cancelada.")
