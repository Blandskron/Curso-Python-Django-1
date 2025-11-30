# =====================================
# Ejemplo 11: Componer datos (líneas) y colaborar con lógica (descuento)
# =====================================

class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self.precio = precio  # usa property

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("Precio negativo")
        self._precio = valor

class LineaPedido:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    @property
    def subtotal(self):
        return self.producto.precio * self.cantidad

class EstrategiaDescuento:
    def calcular(self, total):
        return 0.0

class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def calcular(self, total):
        return total * self.porcentaje

class Pedido:
    def __init__(self, descuento: EstrategiaDescuento):
        self._items: list[LineaPedido] = []   # composición
        self._descuento = descuento           # colaborador

    def agregar(self, linea: LineaPedido):
        self._items.append(linea)

    @property
    def total_bruto(self):
        return sum(l.subtotal for l in self._items)

    @property
    def total_descuento(self):
        return self._descuento.calcular(self.total_bruto)

    @property
    def total_neto(self):
        return self.total_bruto - self.total_descuento

prod1 = Producto("Teclado", 30)
prod2 = Producto("Mouse", 20)
pedido = Pedido(DescuentoPorcentaje(0.1))
pedido.agregar(LineaPedido(prod1, 2))
pedido.agregar(LineaPedido(prod2, 1))
print(pedido.total_neto)
