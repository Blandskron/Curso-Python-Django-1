# Ejemplo 1: Programación estructurada vs POO (carrito de compras)

# Versión estructurada: datos + funciones separadas
precios = [10, 20, 30]

def calcular_total(lista):
    total = 0
    for p in lista:
        total += p
    return total

def aplicar_descuento(total, porcentaje):
    return total * (1 - porcentaje / 100)

total = calcular_total(precios)
total_final = aplicar_descuento(total, 10)

# Versión POO: datos + lógica en una unidad
class Carrito:
    def __init__(self):
        self._items = []  # estado interno

    def agregar(self, precio):
        self._items.append(precio)

    def total(self):
        return sum(self._items)

    def total_con_descuento(self, porcentaje):
        return self.total() * (1 - porcentaje / 100)

carrito = Carrito()
carrito.agregar(10)
carrito.agregar(20)
carrito.agregar(30)
total_carrito = carrito.total_con_descuento(10)
