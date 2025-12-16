class Producto:
    def __init__(self, id, nombre, categoria, precio):
        self.id = int(id)
        self.nombre = str(nombre)
        self.categoria = str(categoria)
        self.precio = float(precio)

    def __repr__(self):
        return f"[{self.id}] {self.nombre} | {self.categoria} | ${self.precio:.0f}"
