# 32) Anti-ejemplo: función con estado global
puntos = 0

def sumar_puntos():
    global puntos
    puntos += 10
