# 42) Funciones anidadas
def externa():
    def interna():
        return "dentro"
    return interna()

print(externa())
