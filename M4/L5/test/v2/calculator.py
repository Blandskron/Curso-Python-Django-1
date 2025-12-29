# calculator.py
from __future__ import annotations

from numbers import Real


def suma(a: Real, b: Real, c: Real) -> Real:
    """
    Suma exactamente 3 números reales (int/float).
    Lanza excepciones claras si el input no es válido.
    """
    for name, value in (("a", a), ("b", b), ("c", c)):
        if not isinstance(value, Real):
            raise TypeError(f"{name} debe ser un número (int/float). Recibido: {type(value).__name__}")

    return a + b + c
