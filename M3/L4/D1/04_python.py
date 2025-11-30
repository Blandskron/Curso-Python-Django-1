# 4) while True con break (patrón input validado)
def solicitar_entero_positivo():
    while True:
        entrada = input("Ingrese un número entero positivo: ")
        try:
            numero = int(entrada)
            if numero > 0:
                return numero
            else:
                print("El número debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida. Ingrese solo dígitos.")

# uso:
# edad = solicitar_entero_positivo()
# print("Edad válida:", edad)
