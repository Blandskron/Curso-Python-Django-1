# Ejemplo 17: *args y **kwargs
def demo_args(*args, **kwargs):
    print("args:", args)      # Tupla de argumentos posicionales
    print("kwargs:", kwargs)  # Diccionario de argumentos nombrados

demo_args(1, 2, 3, nombre="Ana", edad=30)
