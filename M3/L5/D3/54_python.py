# 54) Uso de any() y all() sobre estructuras
calificaciones = [70, 80, 55, 90]

hay_reprobados = any(nota < 60 for nota in calificaciones)
todos_aprobados = all(nota >= 60 for nota in calificaciones)

print(hay_reprobados, todos_aprobados)
