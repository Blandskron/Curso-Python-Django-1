# 2) Copia superficial de lista (shallow copy)
import copy

original = [[1, 2], [3, 4]]
copia1 = original[:]          # slicing
copia2 = list(original)       # constructor
copia3 = copy.copy(original)  # copy superficial

original[0].append(99)
print(original)  # [[1, 2, 99], [3, 4]]
print(copia1)    # [[1, 2, 99], [3, 4]]  comparte sublistas
print(copia2)    # idem
print(copia3)    # idem
