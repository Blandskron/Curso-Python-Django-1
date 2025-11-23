# Ejemplo 26: Inspección de un módulo con dir()
import math

nombres = dir(math)  # Lista los nombres definidos en math
print(len(nombres))  # Cantidad de nombres
print(nombres[:10])  # Muestra los primeros 10
