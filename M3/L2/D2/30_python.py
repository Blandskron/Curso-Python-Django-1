# 30_python.py
# programa con menú simple (while + if/elif)

opcion = ""

while opcion != "4":
    print("=== MENÚ ===")
    print("1) Saludar")
    print("2) Sumar dos números")
    print("3) Mostrar rango 1-5")
    print("4) Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Hola, ¿cómo estás?")
    elif opcion == "2":
        a = float(input("Ingresa a: "))
        b = float(input("Ingresa b: "))
        print("Resultado:", a + b)
    elif opcion == "3":
        for i in range(1, 6):
            print(i)
    elif opcion == "4":
        print("Saliendo...")
    else:
        print("Opción inválida")
