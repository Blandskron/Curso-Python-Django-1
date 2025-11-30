# Ejemplo 28: Encadenamiento implícito al fallar dentro de except

def doble_fallo() -> None:
    try:
        1 / 0
    except ZeroDivisionError:
        # Aquí se produce otra excepción
        int("no-numérico")
