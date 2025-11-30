# Ejemplo 13: Encadenamiento explícito con from

class ConfigError(Exception):
    pass

def obtener_clave(config: dict, clave: str) -> str:
    try:
        return config[clave]
    except KeyError as e:
        raise ConfigError(f"Clave faltante: {clave}") from e
