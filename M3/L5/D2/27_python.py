# 26) Dict: creación y acceso
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Santiago",
}

print(persona["nombre"])
persona["edad"] = 31
persona["correo"] = "ana@example.com"

# 27) Dict: métodos keys(), values(), items()
for clave in persona.keys():
    print("clave:", clave)

for valor in persona.values():
    print("valor:", valor)

for clave, valor in persona.items():
    print(clave, "->", valor)
