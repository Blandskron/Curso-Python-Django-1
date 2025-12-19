import re

def email_valido(email: str) -> bool:
    """
    Valida si un email tiene un formato correcto.

    Args:
        email (str): Email a validar.

    Returns:
        bool: True si es válido, False si no.
    Matches anything other than a letter, digit or underscore. Equivalent to [^a-zA-Z0-9_]
    /\W+/g
    not.a@word%character
    [a-z-A-Z-0-9_]+@[]
    r"\w+@\w+\.\w+"
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email) is not None
