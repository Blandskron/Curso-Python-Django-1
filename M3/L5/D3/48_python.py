# 48) Iteración segura mientras se eliminan claves de un dict
datos = {"a": 1, "b": -2, "c": 3, "d": -4}

for clave in list(datos.keys()):  # copia de claves
    if datos[clave] < 0:
        del datos[clave]

print(datos)
