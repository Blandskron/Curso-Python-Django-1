"""
M3_L6_Actividad N° 7 - Función con condicional y bucles
Fundamentos de Programación en Python

Ejercicio 1:
- Pedir un número:
    - Si es PAR entre 2 y 100 → imprimir todos los pares siguientes hasta 100.
    - Si es IMPAR entre 1 y 99 → imprimir todos los impares siguientes hasta 99.
    - Si es 0, menor que 0 o mayor que 100 → mostrar mensaje de error
      y volver a pedir el número.

Ejercicio 2:
- Leer 5 notas (entre 0 y 10).
- Mostrar:
    - Todas las notas.
    - La nota media.
    - La más alta.
    - La más baja.

Ejercicio 3:
- Pedir un número de mes (1–12).
- Indicar cuántos días tiene y el nombre del mes.
- Debes usar listas (una para nombres, otra para días).
"""

# =========================================================
# EJERCICIO 1
# =========================================================

def pedir_numero_entre_1_y_100() -> int:
    """
    Pide un número al usuario y valida que esté entre 1 y 100.
    Regla especial de la actividad:
      - Si es 0 o menor que 0, o mayor que 100 -> mensaje de error y repite.
    """
    while True:
        try:
            numero = int(input("Ingresa un número entre 1 y 100: "))
        except ValueError:
            print("Error: debes ingresar un número entero.")
            continue

        if numero <= 0:
            print("No es posible realizarlo (no se permiten números <= 0). Intenta de nuevo.")
        elif numero > 100:
            print("No es posible realizarlo (no se permiten números mayores a 100). Intenta de nuevo.")
        else:
            return numero


def ejercicio1():
    """
    Implementa la lógica pedida en el Ejercicio 1.
    - Detecta si el número es par o impar.
    - Imprime los números siguientes de la misma paridad en el rango indicado.
    """
    numero = pedir_numero_entre_1_y_100()

    if numero % 2 == 0:
        print(f"\nUsted ha ingresado un número PAR ({numero}).")
        print("Los números pares siguientes hasta 100 son:")
        # siguiente par es numero + 2 (para que sean "siguientes" y no incluir el mismo)
        for n in range(numero + 2, 101, 2):
            print(n, end=" ")
        print()  # salto de línea final
    else:
        print(f"\nUsted ha ingresado un número IMPAR ({numero}).")
        print("Los números impares siguientes hasta 99 son:")
        for n in range(numero + 2, 100, 2):
            print(n, end=" ")
        print()


# =========================================================
# EJERCICIO 2
# =========================================================

def pedir_nota_valida(indice: int) -> float:
    """
    Pide una nota al usuario y valida que esté entre 0 y 10.
    Se repite hasta que la entrada sea correcta.
    """
    while True:
        try:
            nota = float(input(f"Ingrese la nota {indice} (0 a 10): "))
        except ValueError:
            print("Error: debes ingresar un número (puede ser decimal).")
            continue

        if 0 <= nota <= 10:
            return nota
        else:
            print("La nota debe estar entre 0 y 10. Intenta de nuevo.")


def ejercicio2():
    """
    Lee 5 notas, luego:
      - Muestra todas las notas.
      - Calcula y muestra la media.
      - Encuentra la nota más alta y la más baja.
    """
    notas: list[float] = []

    for i in range(1, 6):
        notas.append(pedir_nota_valida(i))

    print("\nNotas ingresadas:", notas)

    promedio = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)

    print(f"Nota media: {promedio:.2f}")
    print(f"Nota más alta: {nota_max:.2f}")
    print(f"Nota más baja: {nota_min:.2f}")


# =========================================================
# EJERCICIO 3
# =========================================================

def pedir_mes() -> int:
    """
    Pide un número de mes entre 1 y 12.
    Repite hasta que el usuario ingrese un valor válido.
    """
    while True:
        try:
            mes = int(input("Ingresa un número de mes (1-12): "))
        except ValueError:
            print("Error: debes ingresar un número entero.")
            continue

        if 1 <= mes <= 12:
            return mes
        else:
            print("El mes debe estar entre 1 y 12. Intenta de nuevo.")


def ejercicio3():
    """
    Pide un número de mes y muestra:
      - Nombre del mes.
      - Cantidad de días.
    Usa listas para nombres y días.
    """
    nombres_meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre",
    ]

    # Lista de días por mes (suponiendo febrero con 28 días)
    dias_por_mes = [
        31,  # Enero
        28,  # Febrero
        31,  # Marzo
        30,  # Abril
        31,  # Mayo
        30,  # Junio
        31,  # Julio
        31,  # Agosto
        30,  # Septiembre
        31,  # Octubre
        30,  # Noviembre
        31,  # Diciembre
    ]

    mes = pedir_mes()
    indice = mes - 1  # convertimos a índice de lista (0 a 11)

    nombre = nombres_meses[indice]
    dias = dias_por_mes[indice]

    print(f"\nMes {mes}: {nombre} tiene {dias} días.")


# =========================================================
# MENÚ PRINCIPAL PARA PROBAR LOS 3 EJERCICIOS
# =========================================================

def mostrar_menu():
    print("\n=== ACTIVIDAD N° 7 – Función con condicional y bucles ===")
    print("1) Ejercicio 1: Números pares/impares siguientes")
    print("2) Ejercicio 2: Notas de un alumno")
    print("3) Ejercicio 3: Mes, días y nombre del mes")
    print("0) Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
