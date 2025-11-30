# 5) while con else (solo se ejecuta si NO hubo break)
n = 3
while n > 0:
    print("Dentro del bucle, n =", n)
    n -= 1
else:
    print("Bucle while finalizado de forma natural, n =", n)
