# Ejemplo 32: Verificar existencia antes de leer (LBYL)

from pathlib import Path

ruta = Path("entrada.txt")

if ruta.is_file():
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
else:
    contenido = ""
