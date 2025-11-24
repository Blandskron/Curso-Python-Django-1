# 12_python.py
# condicionales anidadas

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida")
else:
    if edad < 12:
        print("Eres niño/a")
    elif edad < 18:
        print("Eres adolescente")
    else:
        print("Eres adulto/a")
