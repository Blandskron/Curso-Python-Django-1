from datetime import datetime


class LoggerTXT:
    """
    Logger simple para guardar acciones de la aplicación en un archivo .txt
    """

    def __init__(self):
        self._registros = []

    def log(self, mensaje: str):
        """
        Guarda un evento en memoria con timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._registros.append(f"[{timestamp}] {mensaje}")

    def guardar(self, archivo: str = "historial_app.txt"):
        """
        Persiste los registros en un archivo .txt
        """
        with open(archivo, "w", encoding="utf-8") as f:
            for linea in self._registros:
                f.write(linea + "\n")
