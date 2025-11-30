# Ejemplo 10: Estado que condiciona comportamiento

class ConexionRed:
    def __init__(self):
        self._estado = "desconectado"

    def conectar(self):
        self._estado = "conectado"

    def desconectar(self):
        self._estado = "desconectado"

    def enviar(self, datos):
        if self._estado != "conectado":
            raise RuntimeError("No hay conexión")
        print(f"Enviando: {datos}")

conn = ConexionRed()
# conn.enviar("hola")  # lanzaría error
conn.conectar()
conn.enviar("hola")