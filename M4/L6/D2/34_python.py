# Ejemplo 34: Registro simple con sellos de tiempo

from datetime import datetime

def log_evento(mensaje: str) -> None:
    ahora = datetime.now().isoformat(timespec="seconds")
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(f"{ahora} - {mensaje}\n")
