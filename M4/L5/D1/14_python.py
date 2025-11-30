# Ejemplo 14: Jerarquía básica de excepciones de dominio

class ErrorApp(Exception):
    """Base de errores de aplicación."""
    pass

class EntradaUsuarioError(ErrorApp):
    pass

class RecursoNoDisponibleError(ErrorApp):
    pass
