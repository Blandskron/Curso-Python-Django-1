# Ejemplo 22: Renombrar y eliminar con pathlib (enfoque moderno)

from pathlib import Path

archivo = Path("datos_viejos.txt")

if archivo.exists():
    archivo.rename("datos_nuevos.txt")

# borrar luego
Path("datos_nuevos.txt").unlink(missing_ok=True)
