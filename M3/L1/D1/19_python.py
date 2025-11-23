# Ejemplo 19: Manejo básico de excepciones (try/except/finally)
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
        resultado = None       # Valor por defecto en caso de error
    finally:
        print("Bloque finally ejecutado")  # Siempre se ejecuta
    return resultado

print(dividir(10, 2))
print(dividir(10, 0))
