# Ejemplo 20: Context manager con archivos (with open)
ruta = "datos.txt"
with open(ruta, "w", encoding="utf-8") as f:
    f.write("Línea de ejemplo\n")  # Escribe en el archivo de forma segura

with open(ruta, "r", encoding="utf-8") as f:
    contenido = f.read()           # Lee el contenido completo
    print(contenido)
