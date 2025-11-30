# =====================================
# Ejemplo 7: Estilo no pythonico con getters/setters explícitos
# =====================================

class PersonaJavaStyle:
    def __init__(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

p_js = PersonaJavaStyle("Ana")
p_js.set_nombre("Ana María")
print(p_js.get_nombre())
