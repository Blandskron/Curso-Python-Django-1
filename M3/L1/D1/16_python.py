# Ejemplo 16: Función con parámetros por defecto y argumentos nombrados
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}")  # Usa mensaje por defecto o personalizado

saludar("Ana")                     # Usa el mensaje por defecto
saludar("Luis", mensaje="Buenos días")  # Usa mensaje personalizado
