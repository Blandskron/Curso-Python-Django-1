# 34) Conteo con Counter
from collections import Counter

frutas = ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]
conteo = Counter(frutas)

print(conteo)
print(conteo.most_common(2))
