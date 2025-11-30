# Ejemplo 18: Lectura de CSV línea a línea con split

with open("usuarios.csv", "r", encoding="utf-8") as f:
    for linea in f:
        campos = linea.rstrip("\n").split(",")
        # procesar campos
