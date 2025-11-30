# Ejemplo 28: Procesamiento parcial de archivo muy grande (streaming)

def contar_lineas_no_vacias(ruta: str) -> int:
    contador = 0
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                contador += 1
    return contador
