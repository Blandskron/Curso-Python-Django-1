# 23) Conjuntos para listas negras (blacklist)
ips_bloqueadas = {"10.0.0.1", "10.0.0.2"}
ip = "10.0.0.1"

if ip in ips_bloqueadas:
    print("Bloqueado")
else:
    print("Permitido")
