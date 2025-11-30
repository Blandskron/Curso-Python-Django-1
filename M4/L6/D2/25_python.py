# Ejemplo 25: Obtención del descriptor de archivo subyacente

with open("registro.log", "a", encoding="utf-8") as f:
    fd = f.fileno()  # número de descriptor de archivo del SO
