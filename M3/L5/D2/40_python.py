# 40) Transformar lista de dicts en dict indexado por id
usuarios = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Luis"},
    {"id": 3, "nombre": "Marta"},
]

por_id = {u["id"]: u for u in usuarios}
print(por_id[2])
