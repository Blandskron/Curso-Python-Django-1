class Catalogo:
    def __init__(self):
        # id -> {"producto": Producto, "stock": int}
        self.items = {}

    def listar(self):
        if not self.items:
            print("Catálogo vacío.")
            return
        print("\n--- CATÁLOGO ---")
        for data in self.items.values():
            p = data["producto"]
            stock = data["stock"]
            print(f"{p} | Stock: {stock}")

    def existe(self, producto_id):
        return int(producto_id) in self.items

    def obtener(self, producto_id):
        return self.items[int(producto_id)]["producto"]

    def stock(self, producto_id):
        return self.items[int(producto_id)]["stock"]

    def agregar_producto_nuevo(self, producto, cantidad):
        if self.existe(producto.id):
            raise ValueError("Ya existe un producto con ese ID.")
        if int(cantidad) <= 0:
            raise ValueError("La cantidad debe ser > 0.")
        self.items[producto.id] = {"producto": producto, "stock": int(cantidad)}

    def sumar_stock(self, producto_id, cantidad):
        producto_id = int(producto_id)
        if not self.existe(producto_id):
            raise ValueError("Producto no existe.")
        if int(cantidad) <= 0:
            raise ValueError("La cantidad debe ser > 0.")
        self.items[producto_id]["stock"] += int(cantidad)

    def actualizar_producto(self, producto_id, nombre=None, categoria=None, precio=None):
        producto_id = int(producto_id)
        if not self.existe(producto_id):
            raise ValueError("Producto no existe.")
        p = self.items[producto_id]["producto"]
        if nombre is not None and nombre != "":
            p.nombre = str(nombre)
        if categoria is not None and categoria != "":
            p.categoria = str(categoria)
        if precio is not None and str(precio) != "":
            p.precio = float(precio)

    def eliminar_producto(self, producto_id):
        producto_id = int(producto_id)
        if not self.existe(producto_id):
            raise ValueError("Producto no existe.")
        del self.items[producto_id]

    def buscar(self, texto):
        texto = str(texto).strip().lower()
        resultados = []
        for data in self.items.values():
            p = data["producto"]
            if texto in p.nombre.lower() or texto in p.categoria.lower():
                resultados.append(data)
        return resultados

    def hay_stock(self, producto_id, cantidad):
        producto_id = int(producto_id)
        cantidad = int(cantidad)
        if not self.existe(producto_id):
            return False
        return self.items[producto_id]["stock"] >= cantidad

    def descontar_stock(self, producto_id, cantidad):
        producto_id = int(producto_id)
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser > 0.")
        if not self.hay_stock(producto_id, cantidad):
            raise ValueError("No hay stock suficiente.")
        self.items[producto_id]["stock"] -= cantidad

