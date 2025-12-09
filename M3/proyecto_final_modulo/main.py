"""
Módulo 3 – E-commerce CLI
Fundamentos de Programación en Python

Funcionalidades:
- Mostrar catálogo de productos.
- Buscar productos por nombre o categoría.
- Agregar productos al carrito.
- Ver carrito y total a pagar.
- Vaciar carrito.

Se utilizan únicamente contenidos del Módulo 3:
tipos de datos, condicionales, ciclos, estructuras y funciones.
"""
from funciones import menu
from funciones.listar import listar_productos
from funciones.buscar import buscar_productos
from funciones.carrito import agregar_al_carrito, mostrar_carrito_y_total, vaciar_carrito

# ==========================================
# CATÁLOGO DE PRODUCTOS
# ==========================================

# Catálogo definido como diccionario:
# clave = id del producto
# valor = diccionario con datos del producto
catalogo = {
    1: {"nombre": "Polera básica", "categoria": "ropa", "precio": 7990},
    2: {"nombre": "Pantalón jeans", "categoria": "ropa", "precio": 19990},
    3: {"nombre": "Audífonos Bluetooth", "categoria": "tecnologia", "precio": 24990},
    4: {"nombre": "Teclado USB", "categoria": "tecnologia", "precio": 12990},
    5: {"nombre": "Lámpara de escritorio", "categoria": "hogar", "precio": 15990},
}

# Carrito: lista de diccionarios
# Cada ítem tendrá: id, nombre, precio, cantidad
carrito = []

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main() -> None:
    while True:
        menu.mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_productos(catalogo)

        elif opcion == "2":
            buscar_productos(catalogo)

        elif opcion == "3":
            agregar_al_carrito(catalogo, carrito)

        elif opcion == "4":
            mostrar_carrito_y_total(carrito)

        elif opcion == "5":
            vaciar_carrito(carrito)

        elif opcion == "0":
            print("Gracias por usar el Ecommerce. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
