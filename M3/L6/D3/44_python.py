# 44) Función como callback
def procesar(valores, fn):
    return [fn(v) for v in valores]

print(procesar([1, 2, 3], lambda x: x ** 3))
