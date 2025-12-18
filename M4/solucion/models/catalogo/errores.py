"""
Errores del dominio catálogo.
"""


class CatalogoError(ValueError):
    pass


class ProductoNoExisteError(CatalogoError):
    pass


class ProductoYaExisteError(CatalogoError):
    pass


class CantidadInvalidaError(CatalogoError):
    pass


class StockInsuficienteError(CatalogoError):
    pass
