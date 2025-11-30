# 17) for sobre diccionario: claves
precios = {"manzana": 500, "pera": 600, "naranja": 450}
for fruta in precios:
    print("Fruta:", fruta)

# 18) for sobre diccionario: items (clave y valor)
for fruta, precio in precios.items():
    print(f"{fruta} cuesta {precio}")
