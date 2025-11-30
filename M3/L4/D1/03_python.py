# 3) while con condición basada en estructura truthy/falsy
texto = "hola"
while texto:
    print("Texto actual:", texto)
    texto = texto[1:]  # va quedando vacío
