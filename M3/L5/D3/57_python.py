# 57) Combinación dict + set para permisos
permisos_por_usuario = {
    "alice": {"leer", "escribir"},
    "bob": {"leer"},
}

def puede(usuario, permiso):
    return permiso in permisos_por_usuario.get(usuario, set())

print(puede("alice", "escribir"))
print(puede("bob", "escribir"))
