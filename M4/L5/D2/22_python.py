# Ejemplo 22: Manejo diferenciado de FileNotFoundError y PermissionError

def abrir_archivo_seguro(ruta: str) -> None:
    try:
        with open(ruta, encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("El archivo no existe")
    except PermissionError:
        print("Permiso denegado")
