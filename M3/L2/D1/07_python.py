# 07_python.py
# valores verdaderos y falsos

valores = [0, 1, "", "hola", [], [1], None, True, False]

for v in valores:
    if v:
        print(repr(v), "=> es truthy")
    else:
        print(repr(v), "=> es falsy")
