# 32_python.py
# ejemplo desde diagrama de flujo: validar número 1-10

valor = input("Ingresa un número entre 1 y 10: ")

if not valor.strip():
    print("No se ingresó un número")
else:
    numero = int(valor)
    if numero < 1 or numero > 10:
        print("El número está fuera del rango (1-10)")
    else:
        print("Número correcto:", numero)
