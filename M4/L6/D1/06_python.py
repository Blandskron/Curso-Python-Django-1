# Ejemplo 6: Uso de seek() y tell() para mover el puntero

with open("texto.txt", "r+", encoding="utf-8") as f:
    inicio = f.tell()
    linea = f.readline()
    posicion_despues = f.tell()
    f.seek(inicio)  # volver al comienzo
