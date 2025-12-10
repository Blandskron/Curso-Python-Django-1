def buscar_producto(productos):
    opcion = int(input("Opciones \n 1-Nombre \n 2-Categoria"))
    if opcion == 1:
        eleccion = input("Ingrese un nombre")
        for producto in productos:
            if producto['nombre'] != eleccion:
               continue
            elif producto['nombre'] == eleccion:
                print(f"ID: {producto['id']} | {producto['nombre']} | Cat: {producto['categoria']} | Precio: ${producto['precio']}")
                break
            else:
                print("Producto no encontrado")
    elif opcion == 2:
        eleccion = input("Ingrese un nombre")
        for producto in productos:
            if producto['categoria'] != eleccion:
               continue
            elif producto['categoria'] == eleccion:
                print(f"ID: {producto['id']} | {producto['nombre']} | Cat: {producto['categoria']} | Precio: ${producto['precio']}")
                break
            else:
                print("Producto no encontrado")
    else:
        print("opcion invalida")