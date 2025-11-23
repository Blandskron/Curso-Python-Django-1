# Patrón robusto de validación de entrada con while True

while True:
    entrada = input("Ingrese su edad (0-120): ")
    try:
        edad = int(entrada)
        if 0 <= edad <= 120:
            print("Edad válida:", edad)
            break  # salimos cuando la edad es correcta
        else:
            print("Error: la edad debe estar entre 0 y 120.")
    except ValueError:
        print("Error: debe ingresar un número entero.")