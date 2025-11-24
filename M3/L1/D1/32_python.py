# Ejemplo 32: Uso de módulos propios con from ... import ...
# archivo operaciones.py
# def sumar(a, b):
#     return a + b
#
# def restar(a, b):
#     return a - b
#
# En otro archivo:
from operaciones import sumar, restar

print(sumar(10, 5))   # 15
print(restar(10, 5))  # 5
