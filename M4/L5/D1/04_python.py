# Ejemplo 4: Captura de múltiples excepciones con tupla

def leer_entero(desde: str) -> int | None:
    try:
        return int(desde)
    except (TypeError, ValueError) as e:
        print(f"Entrada inválida: {e}")
        return None
