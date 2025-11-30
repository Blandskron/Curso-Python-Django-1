# Ejemplo 5: readlines() para archivos pequeños con acceso aleatorio

with open("mensajes.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

primera = lineas[0]
ultima = lineas[-1]
