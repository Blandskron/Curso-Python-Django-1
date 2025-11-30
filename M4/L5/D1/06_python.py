# Ejemplo 6: Uso de else para el camino exitoso

def leer_archivo(ruta: str) -> str | None:
    try:
        f = open(ruta, "r", encoding="utf-8")
    except OSError:
        print("No se pudo abrir el archivo")
        return None
    else:
        contenido = f.read()
        f.close()
        return contenido
