# Ejemplo 33: Herencia múltiple con conflictos resueltos por MRO

class X:
    def metodo(self) -> str:
        return "X"


class Y(X):
    def metodo(self) -> str:
        return "Y"


class Z(X):
    def metodo(self) -> str:
        return "Z"


class Mezcla(Y, Z):
    pass


resultado = Mezcla().metodo()  # "Y" según MRO
