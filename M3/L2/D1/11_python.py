# 11_python.py
# if - elif - else para clasificar notas

nota = float(input("Ingresa una nota (1.0 a 7.0): "))

if nota < 1.0 or nota > 7.0:
    print("Nota inválida")
elif nota >= 6.0:
    print("Desempeño: Excelente")
elif nota >= 4.0:
    print("Desempeño: Aprobado")
else:
    print("Desempeño: Reprobado")
