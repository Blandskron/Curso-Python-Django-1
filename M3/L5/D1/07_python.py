# 7) Lista como pila (stack LIFO)
pila = []
pila.append("A")
pila.append("B")
pila.append("C")

while pila:
    elemento = pila.pop()
    print("Sacando:", elemento)
