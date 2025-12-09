# =====================================
# Ejemplo 10: Calculadora de impuestos como colaborador
# =====================================

class CalculadoraImpuestos:
    def __init__(self, tasa):
        self._tasa = float(tasa)

    def calcular(self, base):
        return base * self._tasa

    @property
    def tasa(self):
        return self._tasa

class FacturaSimple:
    def __init__(self, subtotal, servicio_impuestos: CalculadoraImpuestos):
        # inyección de dependencia
        self.subtotal = subtotal
        self._servicio = servicio_impuestos

    @property
    def impuesto(self):
        return self._servicio.calcular(self.subtotal)

    @property
    def total(self):
        return self.subtotal + self.impuesto

imp_19 = CalculadoraImpuestos(0.19)
fac = FacturaSimple(100, imp_19)
print(fac.total)
