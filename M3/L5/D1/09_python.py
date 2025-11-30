# 9) Cola eficiente con deque
from collections import deque

cola = deque()
cola.append("t1")    # enqueue
cola.append("t2")

primero = cola.popleft()  # dequeue O(1)
print(primero, list(cola))
