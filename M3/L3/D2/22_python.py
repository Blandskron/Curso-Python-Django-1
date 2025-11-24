# Condición de salida en bucle con while True + break

while True:
    texto = input("Escribe algo (o 'fin' para salir): ")
    if texto == "fin":
        print("Terminando el programa...")
        break  # condición de salida
    print("Has escrito:", texto)