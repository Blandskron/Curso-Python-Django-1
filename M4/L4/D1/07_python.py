# Ejemplo 7: Uso correcto de super() en herencia múltiple

class LoggerMixin:
    def guardar(self, mensaje: str) -> None:
        print(f"[LOG] {mensaje}")
        super().guardar(mensaje)


class RepositorioBase:
    def guardar(self, mensaje: str) -> None:
        # acción mínima para permitir la cadena de super()
        pass


class RepositorioConLog(LoggerMixin, RepositorioBase):
    def guardar(self, mensaje: str) -> None:
        super().guardar(mensaje)
