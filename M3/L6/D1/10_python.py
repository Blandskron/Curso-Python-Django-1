# 10) Orden correcto de parámetros
def ejemplo(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)

ejemplo(1, 2, 3, 4, c=20, x=99)
