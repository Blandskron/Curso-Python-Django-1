# Ejemplo 12: Dependencia por instanciación local
class Logger:
    def log(self, mensaje: str) -> None:
        print(f"[LOG] {mensaje}")

class Servicio:
    def procesar(self) -> None:
        logger = Logger()         # creado y usado dentro del método
        logger.log("Procesando")  # no queda como atributo
