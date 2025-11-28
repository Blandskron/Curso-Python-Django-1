# 1. DECISIÓN SIMPLE
# Pedimos un número al usuario y determinamos si es mayor o menor de edad.

print("=== 1) Decisión simple: Mayor o menor de edad ===")
edad = int(input("Ingresa tu edad: "))  # Convertimos la entrada a entero

if edad >= 18:
    # Este bloque se ejecuta si la edad es 18 o más
    print("Eres mayor de edad")
else:
    # Este bloque se ejecuta si la condición anterior NO se cumple
    print("Eres menor de edad")

print()  # Línea en blanco para separar secciones


"""Ejemplo 1: decisión simple para determinar mayoría de edad."""

print("=== 1) Decisión simple: Mayor o menor de edad ===")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

print()  # Línea en blanco para separar secciones
