# Ejemplo 28: Módulos y paquetes (estructura lógica)
# Supongamos la siguiente estructura de archivos:
#
# mi_paquete/
# ├── __init__.py
# └── utiles.py
#
# Contenido de utiles.py:
#
# def saludar(nombre):
#     print(f"Hola desde el paquete, {nombre}")
#
# Uso en otro archivo (por ejemplo, main.py):
from mi_paquete import utiles

utiles.saludar("Ana")  # Llama función definida en el módulo utiles
