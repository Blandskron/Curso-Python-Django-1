# 9) Combinación parámetros normales, *args y **kwargs
def funcion_completa(a, b=10, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

funcion_completa(1, 2, 3, 4, x=5, y=6)
