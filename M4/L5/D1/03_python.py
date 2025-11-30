# Ejemplo 3: Captura específica con try/except

def dividir(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return None
