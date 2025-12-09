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