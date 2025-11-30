# Ejemplo 10: Escribir varias líneas con writelines()

lineas = [
    "id,nombre,prioridad\n",
    "1,Inicio del sistema,Alta\n",
    "2,Usuario conectado,Media\n",
]

with open("bitacora.csv", "w", encoding="utf-8") as f:
    f.writelines(lineas)
