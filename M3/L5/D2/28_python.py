# 28) Dict: get() con valor por defecto
config = {"modo": "oscuro", "lenguaje": "es"}

tema = config.get("modo", "claro")
tamanio_fuente = config.get("fuente", 12)

print(tema, tamanio_fuente)
