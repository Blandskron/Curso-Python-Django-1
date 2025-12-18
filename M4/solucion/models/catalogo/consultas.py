"""
Consultas del catálogo (sin UI).
"""


class ConsultasCatalogoMixin:
    """
    Consultas de lectura del catálogo.
    """

    def listar_items(self):
        """
        Retorna una lista de (producto, stock).
        """
        return [
            (data["producto"], data["stock"])
            for data in self.items.values()
        ]

    def buscar(self, texto):
        """
        Busca por nombre o categoría.

        Returns:
            list[tuple]: [(producto, stock), ...]
        """
        texto = str(texto).strip().lower()
        resultados = []

        for data in self.items.values():
            producto = data["producto"]
            if texto in producto.nombre.lower() or texto in producto.categoria.lower():
                resultados.append((producto, data["stock"]))

        return resultados
