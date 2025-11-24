# 27_python.py
# diccionarios: claves y valores

persona = {
    "nombre": "Luis",
    "edad": 30,
    "ciudad": "Santiago",
}

print("Nombre:", persona["nombre"])
print("Edad:", persona.get("edad"))
print("País:", persona.get("pais", "no registrado"))

persona["profesion"] = "Desarrollador"
persona["edad"] = 31

for clave, valor in persona.items():
    print(clave, "=>", valor)
