# Ejemplo 14: Atributos de clase vs atributos de instancia

class Config:
    version = "1.0"  # atributo de clase (compartido)

    def __init__(self, nombre):
        self.nombre = nombre  # de instancia

conf1 = Config("A")
conf2 = Config("B")
print(conf1.version, conf2.version)
Config.version = "2.0"
print(conf1.version, conf2.version)  # ambos ven el cambio
