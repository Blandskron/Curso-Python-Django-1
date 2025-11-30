# 35) Simulación de inventario con dict
inventario = {
    "prod_100": 10,
    "prod_200": 5,
}

def agregar_stock(codigo, cantidad):
    inventario[codigo] = inventario.get(codigo, 0) + cantidad

def vender(codigo, cantidad):
    stock = inventario.get(codigo, 0)
    if stock >= cantidad:
        inventario[codigo] = stock - cantidad
        return True
    return False

agregar_stock("prod_200", 3)
vender("prod_100", 4)
print(inventario)
