# Ejemplo 21: Eliminar archivo con os.remove()

import os

ruta = "archivo_temp.tmp"

if os.path.exists(ruta):
    os.remove(ruta)
