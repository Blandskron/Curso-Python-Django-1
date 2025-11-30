# Ejemplo 32: Dependencia Notificador -> EmailService
class EmailService:
    def enviar(self, destinatario: str, mensaje: str) -> None:
        print(f"Enviando a {destinatario}: {mensaje}")

class Notificador:
    def notificar_bienvenida(self, correo: str) -> None:
        servicio = EmailService()           # dependencia local
        servicio.enviar(correo, "Bienvenido al sistema")
