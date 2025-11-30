# Ejemplo 35: Escaneo de directorio y escritura de listado a archivo

from pathlib import Path

def listar_archivos(origen: str, salida: str) -> None:
    base = Path(origen)
    archivos = [p.name for p in base.iterdir() if p.is_file()]
    with open(salida, "w", encoding="utf-8") as f:
        for nombre in archivos:
            f.write(nombre + "\n")
