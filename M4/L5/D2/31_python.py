# Ejemplo 31: Excepción de validación de formulario

class ValidacionError(Exception):
    pass

def validar_email(email: str) -> None:
    if "@" not in email:
        raise ValidacionError("Email sin '@'")
