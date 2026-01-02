# Ejemplo 14: Lectura/escritura en modo binario (imagen)

with open("M4\\L6\\D1\\data\\foto.jpg", "rb") as f:
    cabecera = f.read()  # primeros bytes (cabecera)
    print(cabecera)