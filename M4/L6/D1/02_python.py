# Ejemplo 2: Lectura por bloques (chunking) para archivos grandes

TAMANIO_BLOQUE = 1024 * 1024  # 1 MB

with open("logs_grandes.txt", "r", encoding="utf-8") as f:
    while True:
        bloque = f.read(TAMANIO_BLOQUE)
        if not bloque:
            break
        # procesar bloque
