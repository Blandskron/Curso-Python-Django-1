# Ejemplo 27: Cargar configuración JSON desde archivo

import json

def cargar_config(ruta: str) -> dict:
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_config(ruta: str, datos: dict) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
