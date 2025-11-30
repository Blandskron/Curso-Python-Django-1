# Ejemplo 22: Protocolo de Pagable (PEP 544)

from typing import Protocol

class PagableProtocol(Protocol):
    def calcular_pago(self) -> float:
        ...


class Proveedor:
    def __init__(self, monto_factura: float):
        self.monto_factura = monto_factura

    def calcular_pago(self) -> float:
        return self.monto_factura


def pagar_item(item: PagableProtocol) -> float:
    return item.calcular_pago()

# Ejemplo 23: Función polimórfica con lista heterogénea y protocolo

def total_pagable(items: list[PagableProtocol]) -> float:
    total = 0.0
    for i in items:
        total += i.calcular_pago()
    return total
