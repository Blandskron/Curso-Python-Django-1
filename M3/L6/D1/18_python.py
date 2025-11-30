# 18) Variable global (escritura con global)
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)
