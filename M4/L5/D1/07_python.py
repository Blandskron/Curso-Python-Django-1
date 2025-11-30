# Ejemplo 7: Uso de finally para garantizar limpieza

def escribir_archivo(ruta: str, contenido: str) -> None:
    f = None
    try:
        f = open(ruta, "w", encoding="utf-8")
        f.write(contenido)
    except OSError as e:
        print(f"Error de escritura: {e}")
    finally:
        if f is not None:
            f.close()
