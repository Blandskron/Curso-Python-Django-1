# Ejemplo 14: Lectura/escritura en modo binario (imagen)

with open("foto.jpg", "rb") as f:
    cabecera = f.read(16)  # primeros bytes (cabecera)
