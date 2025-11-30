# Ejemplo 23: Comparación de gestión de recursos (mala vs buena)

# MALO: si algo falla, el archivo puede quedar abierto
f = open("salida.txt", "w", encoding="utf-8")
f.write("Hola\n")
f.close()

# BUENO: with garantiza el cierre incluso con excepciones
with open("salida_segura.txt", "w", encoding="utf-8") as f2:
    f2.write("Hola\n")
