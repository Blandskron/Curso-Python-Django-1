# 14) Diccionario como parámetro
def aumentar_stock(stock, producto, cantidad):
    stock[producto] = stock.get(producto, 0) + cantidad

inventario = {"p1": 10}
aumentar_stock(inventario, "p1", 5)
print(inventario)
