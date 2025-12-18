"""
Menús y utilidades de consola.

Centraliza la UI: impresión de menús y lectura de opciones.
"""


def menu_principal():
    print("\n=== TIENDA ===")
    print("1) Entrar como ADMIN")
    print("2) Entrar como CLIENTE")
    print("0) Salir")
    return input("Opción: ").strip()


def menu_admin():
    print("\n--- MENÚ ADMIN ---")
    print("1) Listar catálogo")
    print("2) Crear producto")
    print("3) Actualizar producto")
    print("4) Eliminar producto")
    print("5) Sumar stock")
    print("0) Volver")
    return input("Opción: ").strip()


def menu_cliente(nombre_cliente):
    print(f"\n--- MENÚ CLIENTE ({nombre_cliente}) ---")
    print("1) Ver catálogo")
    print("2) Buscar producto")
    print("3) Agregar al carrito")
    print("4) Ver carrito")
    print("5) Confirmar compra")
    print("0) Volver")
    return input("Opción: ").strip()
