# Ejemplo 18: Uso de with para gestión de recursos (archivo)

def leer_lineas(ruta: str) -> list[str]:
    with open(ruta, encoding="utf-8") as f:
        return [linea.strip() for linea in f]
