# 35) Pipeline funcional
resultado = list(
    map(lambda x: x * 2,
        filter(lambda x: x > 0, [-2, -1, 0, 1, 2, 3]))
)
print(resultado)
