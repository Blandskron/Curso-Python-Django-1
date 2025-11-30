# Ejemplo 25: Versión específica que respeta mejores prácticas

def manejar_especifico() -> None:
    try:
        1 / 0
    except ZeroDivisionError:
        print("Error matemático: división por cero")
