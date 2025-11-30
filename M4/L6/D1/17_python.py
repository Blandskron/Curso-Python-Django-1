# Ejemplo 17: Control fino de codificación y errores

texto = "café ☕"

with open("salida_latin1.txt", "w", encoding="latin-1", errors="replace") as f:
    # 'errors="replace"' evita fallos de codificación
    f.write(texto)
