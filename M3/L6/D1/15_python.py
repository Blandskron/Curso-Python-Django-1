# 15) Desempaquetado de diccionario en llamada
def crear_persona(nombre, edad, ciudad):
    return f"{nombre}-{edad}-{ciudad}"

datos = {"nombre": "Ana", "edad": 30, "ciudad": "Santiago"}
print(crear_persona(**datos))
