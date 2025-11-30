# 20) Uso de zip: iteración en paralelo
productos = ["Manzana", "Pera", "Naranja"]
precios = [1.2, 1.5, 0.8]
cantidades = [10, 5, 12]

for prod, precio, cant in zip(productos, precios, cantidades):
    total = precio * cant
    print(f"{prod}: {cant} unidades, total = {total}")
