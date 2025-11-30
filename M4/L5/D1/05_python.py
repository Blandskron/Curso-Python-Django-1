# Ejemplo 5: Captura genérica como último recurso

def procesar_texto(txt: str) -> None:
    try:
        print(txt.upper())
    except Exception as e:  # último nivel
        print(f"Error inesperado: {type(e).__name__}: {e}")
