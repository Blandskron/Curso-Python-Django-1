# =====================================
# Ejemplo 17: Patrón Strategy con funciones en lugar de clases
# =====================================

def impuesto_basico(monto):
    return monto * 0.19

def impuesto_cero(monto):
    return 0.0

class FacturaEstrategiaFunc:
    def __init__(self, subtotal, estrategia_impuesto):
        self.subtotal = subtotal
        self._estrategia = estrategia_impuesto  # función colaboradora

    @property
    def impuesto(self):
        return self._estrategia(self.subtotal)

    @property
    def total(self):
        return self.subtotal + self.impuesto

f_a = FacturaEstrategiaFunc(100, impuesto_basico)
f_b = FacturaEstrategiaFunc(100, impuesto_cero)
print(f_a.total, f_b.total)
