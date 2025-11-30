# Ejemplo 33: Enfoque EAFP para lectura (asumir éxito y capturar error)

def leer_eafp(ruta: str) -> str:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""
