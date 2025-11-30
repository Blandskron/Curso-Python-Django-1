# Ejemplo 21: Captura de LookupError genérico

def obtener_elemento(seq, idx: int):
    try:
        return seq[idx]
    except LookupError:
        print("Índice fuera de rango o clave inexistente")
        return None
