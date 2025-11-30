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
# FUNCIONES
# ==========================================

def mostrar_menu() -> None:
    print("\nBienvenido/a a tu Ecommerce")
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")


def listar_productos(cat: dict) -> None:
    print("\n--- CATÁLOGO DE PRODUCTOS ---")
    for id_prod, datos in cat.items():
        print(
            f"ID: {id_prod} | "
            f"Nombre: {datos['nombre']} | "
            f"Categoría: {datos['categoria']} | "
            f"Precio: ${datos['precio']}"
        )


def buscar_productos(cat: dict) -> None:
    texto = input("\nIngrese texto a buscar (nombre o categoría): ").lower()
    encontrados = False

    print("\n--- RESULTADOS DE BÚSQUEDA ---")
    for id_prod, datos in cat.items():
        if texto in datos["nombre"].lower() or texto in datos["categoria"].lower():
            print(
                f"ID: {id_prod} | "
                f"Nombre: {datos['nombre']} | "
                f"Categoría: {datos['categoria']} | "
                f"Precio: ${datos['precio']}"
            )
            encontrados = True

    if not encontrados:
        print("No se encontraron productos con ese criterio.")


def agregar_al_carrito(cat: dict, car: list) -> None:
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
    except ValueError:
        print("ID inválido.")
        return

    if id_producto not in cat:
        print("El producto no existe.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad (> 0): "))
    except ValueError:
        print("Cantidad inválida.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0.")
        return

    producto = cat[id_producto]

    # Se agrega una copia del producto con cantidad
    car.append({
        "id": id_producto,
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "cantidad": cantidad
    })

    print("Producto agregado al carrito correctamente.")


def mostrar_carrito_y_total(car: list) -> None:
    if not car:
        print("\nEl carrito está vacío.")
        return

    print("\n--- CARRITO DE COMPRAS ---")
    total = 0

    for item in car:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(
            f"ID: {item['id']} | "
            f"Nombre: {item['nombre']} | "
            f"Cantidad: {item['cantidad']} | "
            f"Precio unitario: ${item['precio']} | "
            f"Subtotal: ${subtotal}"
        )

    print(f"\nTOTAL A PAGAR: ${total}")


def vaciar_carrito(car: list) -> None:
    car.clear()
    print("El carrito ha sido vaciado correctamente.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main() -> None:
    while True:
        mostrar_menu()
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
