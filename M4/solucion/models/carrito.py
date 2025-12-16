from catalogo import Catalogo

class Carrito:
    def __init__(self):
        # id -> cantidad
        self.items = {}

    def esta_vacio(self):
        return len(self.items) == 0

    def agregar(self, producto_id, cantidad):
        producto_id = int(producto_id)
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser > 0.")
        self.items[producto_id] = self.items.get(producto_id, 0) + cantidad

    def vaciar(self):
        self.items = {}

    def ver_detalle(self, catalogo: Catalogo):
        if self.esta_vacio():
            print("Carrito vacío.")
            return 0.0

        print("\n--- CARRITO ---")
        total = 0.0
        for producto_id, cantidad in self.items.items():
            if not catalogo.existe(producto_id):
                # si el admin borró el producto, se ignora o podrías avisar
                continue
            p = catalogo.obtener(producto_id)
            subtotal = p.precio * cantidad
            total += subtotal
            print(f"{p.nombre} | Cant: {cantidad} | Unit: ${p.precio:.0f} | Subtotal: ${subtotal:.0f}")

        print(f"TOTAL A PAGAR: ${total:.0f}")
        return total