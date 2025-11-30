# 37) Función con lista por defecto MAL (anti-patrón)
def agregar_item_mal(x, lista=[]):
    lista.append(x)
    return lista

print(agregar_item_mal(1))
print(agregar_item_mal(2))
