# 1) Variables como referencias (alias)
a = [1, 2, 3]
b = a          # b apunta a la MISMA lista
b.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
