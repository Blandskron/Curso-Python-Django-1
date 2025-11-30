# 60) Mezcla: set para intersección rápida sobre claves de dict
a = {"p1": 10, "p2": 5, "p3": 7}
b = {"p2": 3, "p3": 1, "p4": 9}

comunes = a.keys() & b.keys()   # set de claves comunes
for clave in comunes:
    print(clave, "total:", a[clave] + b[clave])
