# Ejemplo 6: Inspección del MRO (Orden de Resolución de Métodos)

class A:
    def metodo(self) -> str:
        return "A"


class B(A):
    def metodo(self) -> str:
        return "B"


class C(A):
    def metodo(self) -> str:
        return "C"


class D(B, C):
    pass


print(D.__mro__)        # cadena de búsqueda
print(D().metodo())     # se usa B.metodo por el MRO
