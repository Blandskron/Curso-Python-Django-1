# 18) Tupla en set (permitido) vs lista en set (no permitido)
s = set()
s.add((1, 2))       # OK: tupla inmutable
# s.add([1, 2])     # TypeError: unhashable type: 'list'
print(s)
