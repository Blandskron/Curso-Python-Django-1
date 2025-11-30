# =====================================
# Ejemplo 2: Colaboración transitoria ("usa a" por método)
# =====================================

class GPS:
    def calcular_ruta(self, origen, destino):
        print(f"Ruta {origen} → {destino}")

class Conductor:
    def conducir(self, origen, destino, gps: GPS):
        # colabora puntualmente con GPS
        gps.calcular_ruta(origen, destino)
        print("Conduciendo...")

gps = GPS()
chofer = Conductor()
chofer.conducir("A", "B", gps)