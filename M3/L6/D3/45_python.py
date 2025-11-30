# 45) Función con control de errores
def dividir_seguro(a, b):
    if b == 0:
        return None
    return a / b

print(dividir_seguro(10, 0))
