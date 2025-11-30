# Ejemplo 15: Copia binaria de archivo grande por bloques

TAM_BLOQUE = 64 * 1024  # 64 KB

with open("origen.bin", "rb") as origen, open("copia.bin", "wb") as destino:
    while True:
        bloque = origen.read(TAM_BLOQUE)
        if not bloque:
            break
        destino.write(bloque)
