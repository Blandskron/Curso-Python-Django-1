# 31_python.py
# ejemplo integrado: analizar lista de números

def analizar_numeros(lista_numeros):
    # separa positivos, negativos y ceros
    positivos = 0
    negativos = 0
    ceros = 0

    for n in lista_numeros:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        else:
            ceros += 1

    return {
        "positivos": positivos,
        "negativos": negativos,
        "ceros": ceros,
        "cantidad": len(lista_numeros),
        "suma": sum(lista_numeros),
    }


datos = [1, -2, 0, 5, -3, 0, 2]
resumen = analizar_numeros(datos)

print("Datos:", datos)
print("Resumen:", resumen)
