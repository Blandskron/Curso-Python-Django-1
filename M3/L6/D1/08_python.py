# 8) Parámetros **kwargs
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, valor)

mostrar_datos(nombre="Ana", edad=30, ciudad="Santiago")
