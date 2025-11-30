# 29) break en for: detener al encontrar número crítico
sensores = [1, 2, 3, 5, 2, 1]  # 5 = crítico
for lectura in sensores:
    if lectura == 5:
        print("¡Alerta crítica! Deteniendo recorrido.")
        break
    print("Lectura segura:", lectura)
