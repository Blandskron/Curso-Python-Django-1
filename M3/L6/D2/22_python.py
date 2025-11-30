# 22) Función que retorna otra función (closure simple)
def multiplicador(factor):
    def operar(n):
        return n * factor
    return operar

por_dos = multiplicador(2)
print(por_dos(5))
