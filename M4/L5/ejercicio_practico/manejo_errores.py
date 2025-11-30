"""
Módulo 4 – Programación Avanzada en Python
Actividad N° 5 – Captura y Control de Errores en Python

Este archivo implementa:

1. Captura básica de errores al dividir dos números.
2. Manejo de múltiples excepciones (ZeroDivisionError, ValueError).
3. Excepción personalizada EdadInvalidaError y función validar_edad().
4. Uso de finally para limpieza de recursos simulando apertura/cierre de archivo.
"""


# ============================================================
# 1 y 2. Captura básica de errores + múltiples excepciones
# ============================================================

def dividir_numeros() -> None:
    """
    Pide al usuario dos números y los divide, manejando:
      - ZeroDivisionError: división por cero.
      - ValueError: si el usuario no ingresa números válidos.
    """
    print("=== División de dos números (con manejo de errores) ===")
    try:
        texto_a = input("Ingresa el primer número: ")
        texto_b = input("Ingresa el segundo número: ")

        # Puede lanzar ValueError si el texto no es convertible a float.
        a = float(texto_a)
        b = float(texto_b)

        # Puede lanzar ZeroDivisionError si b es 0.
        resultado = a / b

    except ZeroDivisionError:
        print("Error: no se puede dividir por cero. Intenta con otro valor.")
    except ValueError:
        print("Error: debes ingresar solo números (por ejemplo, 3 ó 4.5).")
    else:
        # Solo se ejecuta si no hubo ninguna excepción.
        print(f"Resultado de {a} / {b} = {resultado}")
    finally:
        # Mensaje informativo al final de la operación.
        print("Operación de división finalizada.\n")


# ============================================================
# 3. Excepciones personalizadas – EdadInvalidaError
# ============================================================

class EdadInvalidaError(Exception):
    """
    Excepción personalizada para edades inválidas.
    Se lanza cuando la edad es menor que 0.
    """
    pass


def validar_edad(edad: int) -> None:
    """
    Valida que la edad no sea negativa.
    Lanza EdadInvalidaError si edad < 0.
    """
    if edad < 0:
        raise EdadInvalidaError(f"La edad no puede ser negativa (edad={edad}).")


def demo_validar_edad() -> None:
    """
    Demostración de uso de validar_edad con manejo de excepción personalizada.
    """
    print("=== Validación de edad (con excepción personalizada) ===")
    texto = input("Ingresa tu edad (entero): ")

    try:
        valor = int(texto)
        validar_edad(valor)
    except ValueError:
        print("Error: debes ingresar un número entero para la edad.")
    except EdadInvalidaError as e:
        # Captura de la excepción personalizada.
        print(f"Error de validación: {e}")
    else:
        print(f"Edad válida: {valor} años.")
    finally:
        print("Validación de edad finalizada.\n")


# ============================================================
# 4. Limpieza de recursos con finally
# ============================================================

def demo_archivo_simulado() -> None:
    """
    Simula la apertura y cierre de un archivo usando try / finally.
    No se trabaja con un archivo real, solo se muestran mensajes.
    """
    print("=== Simulación de manejo de archivo ===")

    # Simulación de apertura de recurso
    print("Abriendo archivo...")

    try:
        # Bloque donde podría ocurrir algún error.
        # Forzamos un error para ver el comportamiento del finally.
        opcion = input("¿Simular error? (s/n): ").lower().strip()
        if opcion == "s":
            # Simulamos un error genérico.
            raise RuntimeError("Error simulado de lectura/escritura.")
        else:
            print("Operación con archivo realizada correctamente.")
    except RuntimeError as e:
        print(f"Ocurrió un error durante la operación con el archivo: {e}")
    finally:
        # Este bloque se ejecuta siempre, ocurra o no una excepción.
        print("Cerrando archivo...\n")


# ============================================================
# PROGRAMA PRINCIPAL (DEMO)
# ============================================================

def mostrar_menu() -> None:
    print("=== ACTIVIDAD M4_L5 – Manejo de errores en Python ===")
    print("1) Dividir dos números (try/except múltiple)")
    print("2) Validar edad (excepción personalizada)")
    print("3) Simular manejo de archivo (try/finally)")
    print("0) Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            dividir_numeros()
        elif opcion == "2":
            demo_validar_edad()
        elif opcion == "3":
            demo_archivo_simulado()
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta nuevamente.\n")


if __name__ == "__main__":
    main()
