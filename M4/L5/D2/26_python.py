# Ejemplo 26: No capturar BaseException

def no_capturar_base() -> None:
    try:
        raise KeyboardInterrupt()
    except Exception:
        print("Solo se capturan excepciones de aplicación")
