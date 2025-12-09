# =====================================
# Ejemplo 16: Sistema de reservas con composición y colaboración
# =====================================

class Sala:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad

class Reserva:
    def __init__(self, sala: Sala, persona, asistentes: int):
        self.sala = sala
        self.persona = persona
        self.asistentes = asistentes

class ServicioNotificaciones:
    def enviar(self, mensaje, destino):
        print(f"Enviando a {destino}: {mensaje}")

class SistemaReservas:
    def __init__(self, notificador: ServicioNotificaciones):
        self._reservas: list[Reserva] = []          # composición
        self._notificador = notificador             # colaborador

    def crear_reserva(self, sala: Sala, persona, asistentes):
        if asistentes > sala.capacidad:
            raise ValueError("Capacidad excedida")
        reserva = Reserva(sala, persona, asistentes)
        self._reservas.append(reserva)
        self._notificador.enviar("Reserva confirmada", persona)
        return reserva

notificador = ServicioNotificaciones()
sistema = SistemaReservas(notificador)
sala1 = Sala("Sala A", 10)
sistema.crear_reserva(sala1, "ana@email.com", 5)
