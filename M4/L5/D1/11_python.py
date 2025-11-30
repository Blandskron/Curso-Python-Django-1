# Ejemplo 11: raise para validar argumento

def establecer_edad(edad: int) -> None:
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
