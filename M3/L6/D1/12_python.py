# 12) Paso de objeto mutable (lista)
def agregar_item(lista):
    lista.append(100)

nums = [1, 2, 3]
agregar_item(nums)
print(nums)
