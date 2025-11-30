# Ejemplo 9: Escritura acumulativa con 'a' (append)

with open("aplicacion.log", "a", encoding="utf-8") as f:
    f.write("2025-11-30T10:00Z - Inicio de la aplicación\n")
