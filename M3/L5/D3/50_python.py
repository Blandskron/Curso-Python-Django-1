# 50) Estructura de cola de tareas con deque y dict
from collections import deque

tareas = deque()
estado_tarea = {}  # id -> estado

def encolar_tarea(task_id):
    tareas.append(task_id)
    estado_tarea[task_id] = "pendiente"

def procesar():
    while tareas:
        t = tareas.popleft()
        estado_tarea[t] = "procesada"

encolar_tarea("T1")
encolar_tarea("T2")
procesar()
print(estado_tarea)
