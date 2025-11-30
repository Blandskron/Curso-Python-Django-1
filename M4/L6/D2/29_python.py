# Ejemplo 29: Uso de newline="" para trabajar con csv correctamente

import csv

with open("datos.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["id", "nombre"])
    escritor.writerow([1, "Ana"])
    escritor.writerow([2, "Luis"])
