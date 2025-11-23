# Función profesional para año bisiesto con validación

def es_bisiesto_profesional(anio: int) -> bool:
    """Devuelve True si el año es bisiesto, False en caso contrario."""
    if not isinstance(anio, int) or anio <= 0:
        raise ValueError("El año debe ser un entero positivo")

    return (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0)


try:
    anio_usuario = int(input("Ingrese un año (entero positivo): "))
    if es_bisiesto_profesional(anio_usuario):
        print("Es bisiesto")
    else:
        print("No es bisiesto")
except ValueError as error:
    print("Error:", error)