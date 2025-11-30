# 51) Mezcla de estructuras: lista de tuplas + set para detectar duplicados
ventas = [
    ("Ana", "prod1"),
    ("Ana", "prod2"),
    ("Ana", "prod1"),  # repetido
]

vendidos = set()
ventas_unicas = []

for cliente, producto in ventas:
    clave = (cliente, producto)
    if clave not in vendidos:
        vendidos.add(clave)
        ventas_unicas.append(clave)

print(ventas_unicas)
