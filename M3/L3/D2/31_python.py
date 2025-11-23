# Ejemplo de condición de salida de seguridad en un bucle

intentos = 0
encontrado = False

while not encontrado:
    valor = int(input("Adivina el número secreto (0-5): "))
    intentos += 1

    if valor == 3:
        encontrado = True
        print("¡Correcto! Número secreto encontrado.")
    else:
        print("Incorrecto, intenta de nuevo.")

    if intentos >= 5:
        print("Demasiados intentos. Terminando búsqueda.")
        break  # condición de salida de emergencia