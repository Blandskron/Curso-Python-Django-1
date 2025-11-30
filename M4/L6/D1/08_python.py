# Ejemplo 8: Escritura destructiva con 'w' (sobrescribe)

with open("reporte.txt", "w", encoding="utf-8") as f:
    f.write("Reporte de ventas 2025\n")
    f.write("Total: 12345\n")
