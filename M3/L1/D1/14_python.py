# Ejemplo 14: Dict comprehension
nombres = ["Ana", "Luis", "Carla"]
longitudes = {nombre: len(nombre) for nombre in nombres}  # clave: nombre, valor: longitud
print(longitudes)
