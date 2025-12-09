from funciones.ver_catalogo import ver_catalogo

catalogo_productos = [{"id": 1, "nombre": "atun", "categoria": "abarrotes", "precio": 1000}, {"id": 2, "nombre": "arroz", "categoria": "abarrotes", "precio": 2000}, {"id": 3, "nombre": "fideos", "categoria": "abarrotes", "precio": 1500}, {"id": 4, "nombre": "shampoo", "categoria": "aseo personal", "precio": 2000}, {"id": 5, "nombre": "queso", "categoria": "perecederos", "precio": 5000}]

print("""
1) Ver catálogo de productos
2) Buscar producto por nombre o categoría
3) Agregar producto al carrito
4) Ver carrito y total
5) Vaciar carrito
0) Salir
""")

def buscar_producto():
    opcion = int(input("Opciones \n 1-Nombre \n 2-Categoria"))
    if opcion == 1:
        for producto in catalogo_productos:
            eleccion = input("Ingrese un nombre")
            if producto['nombre'] == eleccion:
                print(f"ID: {producto['id']} | {producto['nombre']} | Cat: {producto['categoria']} | Precio: ${producto['precio']}")
                break
            elif producto != eleccion:
                continue
            else:
                print("Producto no encontrado")
    elif opcion == 2:
        pass
    else:
        print("opcion invalida")

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    ver_catalogo(catalogo_productos)
elif opcion == 2:
    buscar_producto()
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
