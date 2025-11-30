# Ejemplo 31: Lectura binaria y desempaquetado

import struct

with open("binario.dat", "rb") as f:
    datos = f.read(struct.calcsize("If"))
    identificador, valor = struct.unpack("If", datos)
