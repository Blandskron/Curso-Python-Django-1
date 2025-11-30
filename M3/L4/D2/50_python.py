# 50) Uso combinado de zip, enumerate y list comprehension
nombres = ["Ana", "Luis", "Marta"]
notas = [95, 70, 55]

# crear reporte "índice - nombre: estado"
reporte = [
    f"{i} - {nombre}: {'APROBADO' if nota >= 60 else 'REPROBADO'}"
    for i, (nombre, nota) in enumerate(zip(nombres, notas), start=1)
]

for linea in reporte:
    print(linea)
