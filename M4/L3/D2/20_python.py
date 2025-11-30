# Ejemplo 20: Visibilidad de paquete (~) simulada a nivel de módulo
_modulo_estado = {}  # uso interno del módulo

class ServicioModulo:
    def registrar(self, clave: str, valor: str) -> None:
        _modulo_estado[clave] = valor
