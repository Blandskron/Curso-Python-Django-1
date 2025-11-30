# Ejemplo 4: Uso de readline() con bucle while

with open("datos.csv", "r", encoding="utf-8") as f:
    while True:
        linea = f.readline()
        if linea == "":
            break  # EOF real
        # procesar linea
