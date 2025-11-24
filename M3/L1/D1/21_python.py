# Ejemplo 21: Alcance de variables y regla LEGB con función anidada
x = "global"  # Variable global

def exterior():
    x = "enclosing"  # Variable de ámbito envolvente

    def interior():
        nonlocal x   # Usa la variable de la función exterior
        x = "modificada en interior"
        print("interior:", x)

    interior()
    print("exterior:", x)

exterior()
print("global:", x)
