# 6) Retorno múltiple (tupla)
def estadisticas(nums):
    return sum(nums), max(nums), min(nums)

total, mayor, menor = estadisticas([10, 5, 8])
print(total, mayor, menor)
