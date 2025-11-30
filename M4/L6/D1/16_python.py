# Ejemplo 16: Uso de buffering explícito

with open("datos.log", "w", buffering=8192, encoding="utf-8") as f:
    for i in range(1000):
        f.write(f"línea {i}\n")
    f.flush()  # vacía el búfer al SO
