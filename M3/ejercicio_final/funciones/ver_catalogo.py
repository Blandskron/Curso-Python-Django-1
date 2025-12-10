def ver_catalogo(productos):
        for producto in productos:
            print(f"ID: {producto['id']} | {producto['nombre']} | Cat: {producto['categoria']} | Precio: ${producto['precio']}")