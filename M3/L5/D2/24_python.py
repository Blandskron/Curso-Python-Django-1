# 24) frozenset: set inmutable como clave de diccionario
permisos = frozenset({"leer", "escribir"})
roles = {
    permisos: "editor",
}

print(roles[permisos])
