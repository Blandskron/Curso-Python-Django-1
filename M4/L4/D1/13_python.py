# Ejemplo 13: isinstance vs type

def describir_entero(x) -> str:
    if isinstance(x, bool):
        return "Es un booleano"
    if isinstance(x, int):
        return "Es un entero"
    return "No es entero ni booleano"
