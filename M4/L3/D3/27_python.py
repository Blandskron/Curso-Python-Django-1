# Ejemplo 27: Ticket efímero devuelto por una operación
class TicketOperacion:
    def __init__(self, mensaje: str):
        self.mensaje = mensaje

def ejecutar_operacion() -> TicketOperacion:
    # lógica de negocio
    return TicketOperacion("Operación completada")  # objeto temporal
