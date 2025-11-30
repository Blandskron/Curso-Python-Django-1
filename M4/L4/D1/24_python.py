# Ejemplo 24: Mixins para auditar operaciones

class AuditMixin:
    def auditar(self, mensaje: str) -> None:
        print(f"[AUDIT] {mensaje}")


class ServicioTransferencia(AuditMixin):
    def transferir(self, monto: float) -> None:
        self.auditar(f"Transferencia de {monto}")
        # lógica de transferencia
