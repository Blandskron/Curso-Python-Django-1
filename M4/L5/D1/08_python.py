# Ejemplo 8: Estilo LBYL (Look Before You Leap)

import os

def leer_lbyl(ruta: str) -> str | None:
    if os.path.exists(ruta) and os.path.isfile(ruta):
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    print("Archivo no disponible (LBYL)")
    return None
