# Ejemplo 26: Bitácora de eventos con creación, lectura y append

from pathlib import Path

BITACORA = Path("eventos.csv")


def crear_bitacora() -> None:
    encabezado = "id,evento,prioridad\n"
    with open(BITACORA, "w", encoding="utf-8") as f:
        f.write(encabezado)


def registrar_evento(id_ev: int, descripcion: str, prioridad: str) -> None:
    with open(BITACORA, "a", encoding="utf-8") as f:
        f.write(f"{id_ev},{descripcion},{prioridad}\n")


def leer_bitacora() -> None:
    if not BITACORA.exists():
        return
    with open(BITACORA, "r", encoding="utf-8") as f:
        for linea in f:
            ...
