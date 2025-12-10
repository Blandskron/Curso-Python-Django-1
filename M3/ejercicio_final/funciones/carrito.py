carrito = []

def agregar_carrito(productos):
    eleccion = int(input("Agregar a Carrito segun ID: "))
    for producto in productos:
        if producto['id'] != eleccion:
            continue
        elif producto['id'] == eleccion:
            carrito.append(f"ID: {producto['id']} | {producto['nombre']} | Cat: {producto['categoria']} | Precio: ${producto['precio']}")
            print(f"Se agrego {producto['nombre']} | Precio: ${producto['precio']} al carrito")
            break
        else:
            print("Producto no encontrado")
    return carrito

def ver_carrito():
    for precio in carrito:
        total = int(precio['precio']) + int(precio['precio'])
    print(f"Productos en el carrito: {carrito}  total carrito: {total}")