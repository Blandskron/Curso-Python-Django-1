# 38) Corrección con None
def agregar_item_bien(x, lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista

print(agregar_item_bien(1))
print(agregar_item_bien(2))
