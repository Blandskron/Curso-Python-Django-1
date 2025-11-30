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

# Ejemplo 16: Uso de excepción personalizada en lógica de negocio

class Cuenta:
    def __init__(self, saldo_inicial: float = 0.0):
        self.saldo = saldo_inicial

    def retirar(self, monto: float) -> None:
        if monto <= 0:
            raise EntradaUsuarioError("El monto debe ser positivo")
        if monto > self.saldo:
            raise SaldoInsuficienteError(monto, self.saldo)
        self.saldo -= monto
