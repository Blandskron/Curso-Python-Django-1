catalogo_productos = [{1: {"nombre": "Polera", "categoria": "ropa", "precio": 10000}}, {2: {"nombre": "Iphone", "categoria": "tecnologia", "precio": 1500000}}, {3: {"nombre": "Mesa", "categoria": "hogar", "precio": 100000}}, {4: {"nombre": "Pantalon", "categoria": "ropa", "precio": 20000}}, {5: {"nombre": "Notebook", "categoria": "tecnologia", "precio": 85000}}]
    
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Cliente:
    def __init__(self, identificador):
        self.identificador = identificador

class Admin:
    def __init__(self, privilegio):
        self.privilegio = privilegio

    """
    1. Listar productos del catálogo.
    2. Crear producto nuevo indicando al menos: id, nombre, categoría, precio.
    3. Actualizar producto (por ejemplo, cambiar nombre, precio o categoría).
    4. Eliminar producto del catálogo.
    5. Guardar catálogo en archivo (ej: catalogo.txt o catalogo.csv).
    """

class Producto:
    def __init__(self, id, nombre, categoria, precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @property
    def producto(self):
        return f"ID: {self.id} Nombre: {self.nombre}"

class Catalogo:
    def __init__(self):
        self._items = []

class Carrito:
    def __init__(self):
        self._items = []  # estado interno

    def agregar(self, producto: Producto):
        self._items.append(producto)

    def total(self):
        return sum(self._items)

    def total_con_descuento(self, porcentaje):
        return self.total() * (1 - porcentaje / 100)

producto_uno = Producto(1, "Polera", "ropa", 10000)
print(producto_uno.producto)

carrito = Carrito()
carrito.agregar(10)

def menu():
    print("""
        Bienvenido/a a tu Ecommerce
          
        1) Ver catálogo de productos
        2) Buscar producto por nombre o categoría
        3) Agregar producto al carrito
        4) Ver carrito y total
        5) Vaciar carrito
        0) Salir
        """)
    
while True:
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 0:
        print("Saliendo del programa")
        break
    else:
        print("opcion incorrecta")
