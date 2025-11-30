"""
Portafolio M4 – Manejo de Archivos en Python

Objetivo:
- Leer el archivo 'registro_notas.txt'.
- Calcular el promedio de las notas.
- Escribir el resultado en 'promedio_notas.txt'.
"""

ARCHIVO_ENTRADA = "registro_notas.txt"
ARCHIVO_SALIDA = "promedio_notas.txt"


def leer_notas(ruta: str) -> list[int]:
    """
    Lee el archivo de notas y retorna una lista con los valores numéricos.
    """
    notas: list[int] = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, nota = linea.strip().split()
            notas.append(int(nota))

    return notas


def calcular_promedio(notas: list[int]) -> float:
    """
    Calcula el promedio de una lista de notas.
    """
    return sum(notas) / len(notas)


def escribir_promedio(ruta: str, promedio: float) -> None:
    """
    Escribe el promedio en un archivo de salida.
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(f"El promedio de las notas es: {promedio:.2f}\n")


def main() -> None:
    notas = leer_notas(ARCHIVO_ENTRADA)
    promedio = calcular_promedio(notas)
    escribir_promedio(ARCHIVO_SALIDA, promedio)

    print("Proceso finalizado correctamente.")
    print(f"Promedio calculado: {promedio:.2f}")


if __name__ == "__main__":
    main()
