def ver_catalogo(catalogo_productos):
        for producto in catalogo_productos:
            print(f"ID: {producto['id']} | {producto['nombre']} | Cat: {producto['categoria']} | Precio: ${producto['precio']}")