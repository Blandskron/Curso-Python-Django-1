# Ejemplo 10: Bucle que insiste hasta recibir un entero válido

def pedir_entero() -> int:
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
        except ValueError:
            print("Debe ingresar un entero.")
        else:
            return valor
