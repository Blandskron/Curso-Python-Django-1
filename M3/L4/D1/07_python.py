# 7) Menú interactivo con while True
def menu_simple():
    while True:
        print("1) Saludar")
        print("2) Sumar 2 números")
        print("3) Salir")
        opcion = input("Elige opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            print(f"Hola, {nombre}")
        elif opcion == "2":
            a = int(input("a: "))
            b = int(input("b: "))
            print("Resultado:", a + b)
        elif opcion == "3":
            print("Chao!")
            break
        else:
            print("Opción no válida")

# menu_simple()
