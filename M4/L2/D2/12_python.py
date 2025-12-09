# =====================================
# Ejemplo 12: Simulación de sobrecarga con argumentos por defecto
# =====================================

class Conexion:
    def conectar(self, host, puerto=80, timeout=30):
        print(f"Conectando a {host}:{puerto} (timeout={timeout})")

c = Conexion()
c.conectar("servidor.com")
c.conectar("servidor.com", 443)
c.conectar("servidor.com", 443, timeout=5)
