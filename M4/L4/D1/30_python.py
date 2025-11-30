# Ejemplo 30: Clases de reporte con mixins y herencia múltiple

class ExportableCSVMixin:
    def exportar_csv(self) -> str:
        return ";".join(f"{k}={v}" for k, v in self.__dict__.items())


class ReporteBase:
    def __init__(self, titulo: str):
        self.titulo = titulo


class ReporteVentas(ExportableCSVMixin, ReporteBase):
    def __init__(self, titulo: str, total: float):
        super().__init__(titulo)
        self.total = total
