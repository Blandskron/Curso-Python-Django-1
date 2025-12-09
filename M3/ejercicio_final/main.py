catalogo_productos = [{"id": 1, "nombre": "atum", "categoria": "abarrotes", "precio": 1000}, {"id": 2, "nombre": "arroz", "categoria": "abarrotes", "precio": 2000}, {"id": 3, "nombre": "fideos", "categoria": "abarrotes", "precio": 1500}, {"id": 4, "nombre": "champoo", "categoria": "aseo personal", "precio": 2000}, {"id": 5, "nombre": "queso", "categoria": "perecederos", "precio": 5000}]

print("""
1) Ver catálogo de productos
2) Buscar producto por nombre o categoría
3) Agregar producto al carrito
4) Ver carrito y total
5) Vaciar carrito
0) Salir
""")

def ver_catalogo():
    for producto in catalogo_productos:
        print(catalogo_productos)
        for clave, valor in producto.items():
            print(producto)
            seleccion = input("Ingrese el nombre del producto: ")
            if seleccion == valor:
                print("producto encontrado", clave, valor)
    return f"producto encontrado {clave}, {valor}"

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    for producto in catalogo_productos:
        ver_catalogo()
elif opcion == 2:
    buscar = int(input("Producto opcion 1 - Categoria opcion 2:"))
    if buscar == 1:
        ver_catalogo()

    elif buscar == 2:
        pass
    else:
        print("opcion incorrecta saliendo del programa....")
elif opcion == 3:
    pass
elif opcion == 4:
    pass
elif opcion == 5:
    pass
elif opcion == 0:
    print("Saliendo del programa")
else:
    print("opcion incorrecta")
