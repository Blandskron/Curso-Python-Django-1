# Manejo de condiciones de borde: raíz cuadrada simple

def calcular_raiz_cuadrada(x: float) -> float | None:
    """Calcula raíz cuadrada real solo si x es >= 0."""
    if x < 0:
        print("Error: no se puede calcular la raíz de un número negativo")
        return None

    # Implementación simple usando el operador **
    return x ** 0.5


valor = float(input("Ingrese un número para la raíz: "))
resultado = calcular_raiz_cuadrada(valor)
if resultado is not None:
    print("La raíz es:", resultado)