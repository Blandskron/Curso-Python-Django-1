# 50) Arquitectura funcional simple
def obtener_datos():
    return [10, 5, "x", 20]

def limpiar_datos(datos):
    return [d for d in datos if isinstance(d, int)]

def procesar_datos(datos):
    return sum(datos)

datos = obtener_datos()
datos_limpios = limpiar_datos(datos)
resultado = procesar_datos(datos_limpios)
print(resultado)
