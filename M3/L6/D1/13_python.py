# 13) Evitar efectos secundarios usando copia
def procesar(lista):
    nueva = lista.copy()
    nueva.append(99)
    return nueva

original = [1, 2, 3]
resultado = procesar(original)
print(original, resultado)
