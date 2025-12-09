# =====================================
# Ejemplo 13: Simulación de sobrecarga con *args
# =====================================

class Acumulador:
    def sumar(self, *numeros):
        total = 0
        for n in numeros:
            total += n
        return total

acc = Acumulador()
print(acc.sumar(1))
print(acc.sumar(1, 2, 3, 4))
