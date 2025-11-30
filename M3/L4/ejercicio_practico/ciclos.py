"""
Actividad N° 4 – Estructuras Repetitivas en Python
Módulo: Fundamentos de Programación en Python

Este archivo contiene los ejercicios solicitados sobre ciclos while y for,
incluyendo uso de break y continue.
"""


# 1. Uso básico de while
# Este ciclo while imprime los números del 1 al 5.
# El ciclo termina cuando la variable contador supera el valor 5.
contador = 1

while contador <= 5:
    print(f"While 1-5 -> {contador}")
    contador += 1


print("-" * 40)


# 2. Uso básico de for
# Este ciclo for recorre una lista de frutas y las imprime en pantalla.
# El ciclo termina automáticamente cuando se recorren todos los elementos de la lista.
frutas = ["manzana", "plátano", "naranja"]

for fruta in frutas:
    print(f"For frutas -> {fruta}")


print("-" * 40)


# 3. Condición en un ciclo
# Este ciclo for recorre los números del 1 al 10.
# Para cada número, se verifica si es par o impar usando el operador módulo (%).
# El ciclo finaliza cuando se han recorrido todos los números del rango.
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"{numero} -> Par")
    else:
        print(f"{numero} -> Impar")


print("-" * 40)


# 4. Ciclo infinito controlado con break
# Este ciclo while True es teóricamente infinito.
# Se detiene cuando el usuario ingresa el número 0,
# momento en el que se ejecuta la sentencia break.
while True:
    numero_ingresado = int(input("Ingresa un número (0 para salir): "))

    if numero_ingresado == 0:
        print("Se ingresó 0, saliendo del ciclo...")
        break

    print(f"Ingresaste: {numero_ingresado}")


print("-" * 40)


# 5. Ciclo anidado
# Este programa imprime la tabla de multiplicar del 1 al 3.
# El ciclo externo controla el número base (1 a 3).
# El ciclo interno recorre los multiplicadores (1 a 10).
# Cada ciclo termina cuando completa su rango de números.
for numero_base in range(1, 4):
    print(f"Tabla del {numero_base}")
    for multiplicador in range(1, 11):
        resultado = numero_base * multiplicador
        print(f"{numero_base} x {multiplicador} = {resultado}")
    print("-" * 20)


print("-" * 40)


# 6. Uso de continue
# Este ciclo recorre una lista de nombres.
# Cuando el nombre es "Juan", se ejecuta continue,
# lo que hace que se salte el resto del cuerpo del ciclo
# para esa iteración específica.
# El ciclo finaliza cuando se recorren todos los nombres.
nombres = ["Ana", "Juan", "Luis", "María", "Juan", "Pedro"]

for nombre in nombres:
    if nombre == "Juan":
        # Se omite la impresión para "Juan"
        continue
    print(f"Nombre -> {nombre}")
