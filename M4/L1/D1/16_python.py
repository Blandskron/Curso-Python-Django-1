# Ejemplo 16: Mensajes encadenados entre objetos

class Logger:
    def log(self, mensaje):
        print("[LOG]", mensaje)

class ServicioPagos:
    def __init__(self, logger: Logger):
        self.logger = logger

    def pagar(self, monto):
        self.logger.log(f"Procesando pago de {monto}")
        print("Pago realizado")

class ControladorPagos:
    def __init__(self, servicio: ServicioPagos):
        self.servicio = servicio

    def post_pagar(self, monto):
        # mensaje externo → controlador → servicio → logger
        self.servicio.pagar(monto)

logger = Logger()
servicio = ServicioPagos(logger)
controlador = ControladorPagos(servicio)
controlador.post_pagar(100)
