# Cláusulas de guarda para evitar anidamiento profundo

TARIFA_HORA = 10.0

class Empleado:
    def __init__(self, activo: bool, horas: int) -> None:
        self.activo = activo
        self.horas = horas


def calcular_pago(empleado: Empleado) -> float | None:
    """Ejemplo de guard clauses para simplificar la lógica."""
    if not empleado.activo:
        return None  # empleado inactivo

    if empleado.horas <= 0:
        return 0.0  # sin horas trabajadas

    return empleado.horas * TARIFA_HORA  # camino "feliz"


empleado_demo = Empleado(activo=True, horas=8)
print("Pago:", calcular_pago(empleado_demo))