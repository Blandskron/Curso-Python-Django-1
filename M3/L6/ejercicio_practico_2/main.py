"""
M3_L6_Actividad N° 6 - Función con condicional y bucles
Programación Básica en Python

Enunciado (resumen):
- Preguntar al usuario CUÁNTOS datos (notas) va a ingresar.
- Pedir las notas una por una.
- Entregar como salida cuántas notas ingresadas son MAYORES que el promedio.

Ejemplo (según enunciado):
Cuantos datos ingresara? 5
Dato 1: 6.5
Dato 2: 2.1
Dato 3: 2.2
Dato 4: 9.8
Dato 5: 6.1
2 datos son mayores que el promedio
"""


def pedir_cantidad_datos() -> int:
    """
    Pide al usuario la cantidad de datos a ingresar.
    Valida que sea un entero mayor que 0.
    """
    while True:
        try:
            cantidad = int(input("Cuántos datos ingresará? "))
        except ValueError:
            print("Error: debes ingresar un número entero.")
            continue

        if cantidad <= 0:
            print("La cantidad debe ser un entero mayor que 0. Intenta nuevamente.")
        else:
            return cantidad


def pedir_nota(indice: int) -> float:
    """
    Pide una nota (dato) al usuario.
    No se restringe el rango porque el enunciado no lo exige,
    solo se valida que sea un número (float).
    """
    while True:
        try:
            nota = float(input(f"Dato {indice}: "))
            return nota
        except ValueError:
            print("Error: debes ingresar un número (puede ser decimal). Intenta nuevamente.")


def leer_notas(cantidad: int) -> list[float]:
    """
    Lee 'cantidad' de notas desde teclado y las devuelve en una lista.
    """
    notas: list[float] = []
    for i in range(1, cantidad + 1):
        notas.append(pedir_nota(i))
    return notas


def contar_mayores_que_promedio(notas: list[float]) -> tuple[float, int]:
    """
    Calcula el promedio de la lista de notas y cuenta
    cuántas son estrictamente mayores que ese promedio.

    Retorna:
        (promedio, cantidad_mayores)
    """
    promedio = sum(notas) / len(notas)
    mayores = sum(1 for n in notas if n > promedio)
    return promedio, mayores


def main() -> None:
    """
    Flujo principal del programa:
      1) Pregunta cuántos datos se ingresarán.
      2) Lee cada nota.
      3) Calcula el promedio.
      4) Muestra cuántas notas son mayores que el promedio.
    """
    cantidad = pedir_cantidad_datos()
    notas = leer_notas(cantidad)
    promedio, mayores = contar_mayores_que_promedio(notas)

    # Mensaje final (solo exige contar mayores que el promedio,
    # pero además mostramos el promedio como apoyo).
    print(f"\nEl promedio de las notas es: {promedio:.2f}")
    if mayores == 1:
        print("1 dato es mayor que el promedio")
    else:
        print(f"{mayores} datos son mayores que el promedio")


if __name__ == "__main__":
    main()
