# 56) Estructura para logs: lista de dicts
logs = []
logs.append({"nivel": "INFO", "msg": "Inicio", "ts": 1})
logs.append({"nivel": "ERROR", "msg": "Fallo", "ts": 2})

errores = [log for log in logs if log["nivel"] == "ERROR"]
print(errores)
