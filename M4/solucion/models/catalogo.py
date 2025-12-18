"""
Módulo catalogo.

Contiene la clase Catalogo, responsable de gestionar los productos
disponibles, su stock y las operaciones de administración del inventario.
"""


class Catalogo:
    """
    Representa el catálogo de productos del e-commerce.

    Internamente maneja un diccionario con la siguiente estructura:

    {
        producto_id: {
            "producto": Producto,
            "stock": int
        }
    }
    """

    def __init__(self):
        """
        Inicializa un catálogo vacío.
        """
        self.items = {}

    def listar(self):
        """
        Muestra el catálogo completo por consola.
        """
        if not self.items:
            print("Catálogo vacío.")
            return

        print("\n--- CATÁLOGO ---")
        for data in self.items.values():
            producto = data["producto"]
            stock = data["stock"]
            print(f"{producto} | Stock: {stock}")

    def existe(self, producto_id):
        """
        Verifica si un producto existe en el catálogo.

        Args:
            producto_id (int | str): ID del producto.

        Returns:
            bool: True si existe, False en caso contrario.
        """
        return int(producto_id) in self.items

    def obtener(self, producto_id):
        """
        Obtiene un producto del catálogo.

        Args:
            producto_id (int | str): ID del producto.

        Returns:
            Producto: Producto correspondiente al ID.
        """
        return self.items[int(producto_id)]["producto"]

    def obtener_stock(self, producto_id):
        """
        Obtiene el stock disponible de un producto.

        Args:
            producto_id (int | str): ID del producto.

        Returns:
            int: Cantidad disponible.
        """
        return self.items[int(producto_id)]["stock"]

    def agregar_producto_nuevo(self, producto, cantidad):
        """
        Agrega un nuevo producto al catálogo.

        Args:
            producto (Producto): Producto a agregar.
            cantidad (int | str): Stock inicial.

        Raises:
            ValueError: Si el producto ya existe o la cantidad es inválida.
        """
        if self.existe(producto.producto_id):
            raise ValueError("Ya existe un producto con ese ID.")

        if int(cantidad) <= 0:
            raise ValueError("La cantidad debe ser > 0.")

        self.items[producto.producto_id] = {
            "producto": producto,
            "stock": int(cantidad),
        }

    def sumar_stock(self, producto_id, cantidad):
        """
        Incrementa el stock de un producto existente.

        Args:
            producto_id (int | str): ID del producto.
            cantidad (int | str): Cantidad a sumar.

        Raises:
            ValueError: Si el producto no existe o la cantidad es inválida.
        """
        producto_id = int(producto_id)

        if not self.existe(producto_id):
            raise ValueError("Producto no existe.")

        if int(cantidad) <= 0:
            raise ValueError("La cantidad debe ser > 0.")

        self.items[producto_id]["stock"] += int(cantidad)

    def actualizar_producto(self, producto_id, nombre=None, categoria=None, precio=None):
        """
        Actualiza los datos de un producto existente.

        Solo se actualizan los campos enviados.

        Args:
            producto_id (int | str): ID del producto.
            nombre (str, optional): Nuevo nombre.
            categoria (str, optional): Nueva categoría.
            precio (float | str, optional): Nuevo precio.

        Raises:
            ValueError: Si el producto no existe.
        """
        producto_id = int(producto_id)

        if not self.existe(producto_id):
            raise ValueError("Producto no existe.")

        producto = self.items[producto_id]["producto"]

        if nombre:
            producto.nombre = str(nombre)

        if categoria:
            producto.categoria = str(categoria)

        if precio is not None and str(precio) != "":
            producto.precio = float(precio)

    def eliminar_producto(self, producto_id):
        """
        Elimina un producto del catálogo.

        Args:
            producto_id (int | str): ID del producto.

        Raises:
            ValueError: Si el producto no existe.
        """
        producto_id = int(producto_id)

        if not self.existe(producto_id):
            raise ValueError("Producto no existe.")

        del self.items[producto_id]

    def buscar(self, texto):
        """
        Busca productos por nombre o categoría.

        Args:
            texto (str): Texto a buscar.

        Returns:
            list[dict]: Lista de coincidencias con estructura
                        {"producto": Producto, "stock": int}
        """
        texto = str(texto).strip().lower()
        resultados = []

        for data in self.items.values():
            producto = data["producto"]

            if (
                texto in producto.nombre.lower()
                or texto in producto.categoria.lower()
            ):
                resultados.append(data)

        return resultados

    def hay_stock(self, producto_id, cantidad):
        """
        Verifica si hay stock suficiente para una cantidad solicitada.

        Args:
            producto_id (int | str): ID del producto.
            cantidad (int | str): Cantidad requerida.

        Returns:
            bool: True si hay stock suficiente.
        """
        producto_id = int(producto_id)
        cantidad = int(cantidad)

        if not self.existe(producto_id):
            return False

        return self.items[producto_id]["stock"] >= cantidad

    def descontar_stock(self, producto_id, cantidad):
        """
        Descuenta stock de un producto.

        Args:
            producto_id (int | str): ID del producto.
            cantidad (int | str): Cantidad a descontar.

        Raises:
            ValueError: Si la cantidad es inválida o no hay stock suficiente.
        """
        producto_id = int(producto_id)
        cantidad = int(cantidad)

        if cantidad <= 0:
            raise ValueError("Cantidad debe ser > 0.")

        if not self.hay_stock(producto_id, cantidad):
            raise ValueError("No hay stock suficiente.")

        self.items[producto_id]["stock"] -= cantidad
