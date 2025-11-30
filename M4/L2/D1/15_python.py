# =====================================
# Ejemplo 15: Constructores alternativos con @classmethod
# =====================================

class Fecha:
    def __init__(self, anio, mes, dia):
        self.anio = anio
        self.mes = mes
        self.dia = dia

    @classmethod
    def from_string(cls, texto):
        anio, mes, dia = map(int, texto.split("-"))
        return cls(anio, mes, dia)

    @classmethod
    def hoy(cls):
        from datetime import date
        d = date.today()
        return cls(d.year, d.month, d.day)

f1 = Fecha(2024, 5, 1)
f2 = Fecha.from_string("2024-05-01")
f3 = Fecha.hoy()
