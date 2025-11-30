# Ejemplo 27: Uso de assert para verificar invariantes

def raiz(x: float) -> float:
    assert x >= 0, "x debe ser no negativo"
    return x ** 0.5
