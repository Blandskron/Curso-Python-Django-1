# 43) Registro inmutable con tupla dentro de lista
registro_ventas = []
registro_ventas.append(("2025-11-29", "prod_1", 3))
registro_ventas.append(("2025-11-30", "prod_2", 1))

for fecha, producto, cantidad in registro_ventas:
    print(fecha, producto, cantidad)
