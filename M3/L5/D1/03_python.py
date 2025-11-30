# 3) Copia profunda (deep copy) para listas anidadas
import copy

original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(original)

original[0].append(99)
print(original)        # [[1, 2, 99], [3, 4]]
print(copia_profunda)  # [[1, 2], [3, 4]]
