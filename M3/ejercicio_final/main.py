from funciones.ver_catalogo import ver_catalogo
from funciones.buscar import buscar_producto
from funciones.carrito import agregar_carrito, ver_carrito


catalogo_productos = [{"id": 1, "nombre": "atun", "categoria": "abarrotes", "precio": 1000}, {"id": 2, "nombre": "arroz", "categoria": "abarrotes", "precio": 2000}, {"id": 3, "nombre": "fideos", "categoria": "abarrotes", "precio": 1500}, {"id": 4, "nombre": "shampoo", "categoria": "aseo personal", "precio": 2000}, {"id": 5, "nombre": "queso", "categoria": "perecederos", "precio": 5000}]

while True:
    print("""
    1) Ver catálogo de productos
    2) Buscar producto por nombre o categoría
    3) Agregar producto al carrito
    4) Ver carrito y total
    5) Vaciar carrito
    0) Salir
    """)

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        ver_catalogo(catalogo_productos)
    elif opcion == 2:
        buscar_producto(catalogo_productos)
    elif opcion == 3:
        ver_catalogo(catalogo_productos)
        continuar = True
        while continuar:
            agregar_carrito(catalogo_productos)
            eleccion = input("Desea agregar mas productos Si o No")
            if eleccion == "si":
                continuar = True
            elif eleccion == "no":
                continuar = False
            else:
                print("debe escribir si o no")
    elif opcion == 4:
        ver_carrito()
    elif opcion == 5:
        pass
    elif opcion == 0:
        print("Saliendo del programa")
        break
    else:
        print("opcion incorrecta")
