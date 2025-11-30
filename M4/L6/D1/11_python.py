# Ejemplo 11: Modo 'r+' para leer y sobrescribir en el mismo archivo

with open("contador.txt", "r+", encoding="utf-8") as f:
    valor = int(f.read().strip() or "0")
    f.seek(0)
    f.write(str(valor + 1))
    f.truncate()
