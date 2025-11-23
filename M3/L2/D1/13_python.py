# 13_python.py
# manejo de condiciones de borde (rango válido)

numero = int(input("Ingresa un número entre 1 y 10: "))

if numero < 1:
    print("Demasiado pequeño (menor que 1)")
elif numero > 10:
    print("Demasiado grande (mayor que 10)")
else:
    print("Dentro del rango [1, 10]")
