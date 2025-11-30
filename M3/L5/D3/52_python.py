# 52) Conversión de dict anidado a lista para reporte
inventario = {
    "bodega1": {"p1": 10, "p2": 5},
    "bodega2": {"p1": 3, "p3": 7},
}

reporte = []

for bodega, productos in inventario.items():
    for codigo, stock in productos.items():
        reporte.append((bodega, codigo, stock))

print(reporte)
