# Ejemplo 14: Jerarquía básica de excepciones de dominio

class ErrorApp(Exception):
    """Base de errores de aplicación."""
    pass

class EntradaUsuarioError(ErrorApp):
    pass

class RecursoNoDisponibleError(ErrorApp):
    pass

# Ejemplo 15: Excepción personalizada con datos enriquecidos

class SaldoInsuficienteError(ErrorApp):
    def __init__(self, necesario: float, disponible: float):
        self.necesario = necesario
        self.disponible = disponible
        super().__init__(f"Necesario: {necesario}, disponible: {disponible}")
