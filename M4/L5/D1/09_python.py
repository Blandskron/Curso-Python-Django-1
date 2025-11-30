# Ejemplo 9: Estilo EAFP (Easier to Ask Forgiveness than Permission)

def leer_eafp(ruta: str) -> str | None:
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    except OSError:
        print("Archivo no disponible (EAFP)")
        return None
