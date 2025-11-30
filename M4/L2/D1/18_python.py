# =====================================
# Ejemplo 18: Testing sencillo usando colaborador "mock"
# =====================================

class ImpuestoMock:
    def __init__(self):
        self.llamadas = 0

    def calcular(self, monto):
        self.llamadas += 1
        return 0.0  # siempre cero

class FacturaTest:
    def __init__(self, subtotal, servicio_impuestos):
        self.subtotal = subtotal
        self._servicio = servicio_impuestos

    @property
    def total(self):
        return self.subtotal + self._servicio.calcular(self.subtotal)

mock = ImpuestoMock()
fac_test = FacturaTest(50, mock)
print(fac_test.total, mock.llamadas)
