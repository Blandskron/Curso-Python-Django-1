# 4) Parámetros con valor por defecto
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar("Luis"))
print(saludar("Luis", "Buenos días"))
