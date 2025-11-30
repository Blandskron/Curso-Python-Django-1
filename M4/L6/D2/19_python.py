# Ejemplo 19: Uso de enumerate para numerar líneas

with open("poema.txt", "r", encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):
        # número de línea disponible para logs
        ...
