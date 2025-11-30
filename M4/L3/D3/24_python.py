# Ejemplo 24: Contador estático de instancias
class TicketSoporte:
    _contador = 0  # atributo estático

    def __init__(self, asunto: str):
        TicketSoporte._contador += 1
        self.id = TicketSoporte._contador
        self.asunto = asunto
