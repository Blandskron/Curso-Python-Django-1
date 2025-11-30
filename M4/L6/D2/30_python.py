# Ejemplo 30: Escritura binaria de estructura personalizada

import struct

# entero (I), flotante (f)
registro = struct.pack("If", 42, 3.14)

with open("binario.dat", "wb") as f:
    f.write(registro)
