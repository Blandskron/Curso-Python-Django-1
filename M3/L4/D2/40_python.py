# 40) List comprehension para filtrar y transformar
palabras = ["python", "es", "potente"]
mayusculas = [p.upper() for p in palabras if len(p) > 2]
print(mayusculas)
