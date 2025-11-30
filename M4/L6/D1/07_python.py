# Ejemplo 7: Inspección de atributos de archivo

with open("config.yml", "r", encoding="utf-8") as f:
    nombre = f.name
    modo = f.mode
    codificacion = f.encoding
    cerrado = f.closed
