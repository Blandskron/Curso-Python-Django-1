# 28) Contar aprobados y reprobados
calificaciones = [85, 40, 72, 59, 91]
aprobados = 0
reprobados = 0

for cal in calificaciones:
    if cal >= 60:
        aprobados += 1
    else:
        reprobados += 1

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
