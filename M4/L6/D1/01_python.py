# Ejemplo 1: Lectura completa de archivo pequeño (modo texto)

with open("config.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
