# 23) Clausura con estado
def contador():
    c = 0
    def inc():
        nonlocal c
        c += 1
        return c
    return inc

c1 = contador()
print(c1())
print(c1())
