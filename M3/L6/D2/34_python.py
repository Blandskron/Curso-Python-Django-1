# 34) Composición de funciones
def limpiar(datos):
    return [d for d in datos if isinstance(d, (int, float))]

def convertir(c):
    return c * 9 / 5 + 32

def convertir_lista(lista):
    return [convertir(x) for x in lista]

datos = [20, 15, "N/A", -5]
limpios = limpiar(datos)
convertidos = convertir_lista(limpios)
print(convertidos)
