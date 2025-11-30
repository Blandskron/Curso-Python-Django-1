# 55) Filtrar claves de dict usando dict comprehension
config = {
    "modo": "oscuro",
    "debug": True,
    "max_users": 100,
}

solo_bool = {k: v for k, v in config.items() if isinstance(v, bool)}
print(solo_bool)
