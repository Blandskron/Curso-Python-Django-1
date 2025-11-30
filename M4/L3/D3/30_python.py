# Ejemplo 30: Name Mangling de atributo privado
class CajaSegura:
    def __init__(self, clave: str):
        self.__clave = clave

    def verificar(self, intento: str) -> bool:
        return intento == self.__clave

caja = CajaSegura("XYZ")
# acceso indirecto al atributo: caja._CajaSegura__clave (no recomendado)
