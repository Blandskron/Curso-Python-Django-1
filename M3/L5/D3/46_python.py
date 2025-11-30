# 46) Selección de estructura según requerimiento (ejemplo simple)
def coleccion_para(necesita_orden, necesita_unicidad):
    if necesita_orden and not necesita_unicidad:
        return []          # lista
    if not necesita_orden and necesita_unicidad:
        return set()       # set
    if necesita_orden and necesita_unicidad:
        return dict()      # claves únicas y orden de inserción
    return {}              # caso por defecto

estructura = coleccion_para(necesita_orden=True, necesita_unicidad=False)
