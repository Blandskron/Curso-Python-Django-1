# Ejemplo 29: Sobrecarga manual basada en isinstance

def formatear(valor) -> str:
    if isinstance(valor, (int, float)):
        return f"{valor:.2f}"
    if isinstance(valor, str):
        return valor.upper()
    return str(valor)
