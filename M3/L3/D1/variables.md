
##  1. *snake_case* (  **RECOMENDADO en Python** )

 Es el estándar oficial según  **PEP 8** .

```python
numero_opcional = 10
total_usuarios = 250
fecha_creacion = "2025-11-27"
intentos_fallidos = 0
```

 **Uso:**

* Variables
* Funciones
* Argumentos

 **Mejor práctica en Python**

---

##  2. *camelCase* ( No recomendado en Python)

 Común en JavaScript, Java u otros lenguajes.

```python
numeroOpcional = 10
totalUsuarios = 250
fechaCreacion = "2025-11-27"
```

 **Uso:**

*  Evitar en Python
*  Aceptable solo si trabajas con código heredado o integraciones externas

---

##  3. *PascalCase* (Clases)

 Se usa  **exclusivamente para clases** .

```python
class Usuario:
    pass

class GestorDeArchivos:
    pass
```

 **Uso correcto:**

* Clases
* Modelos
* Excepciones personalizadas

---

##  4. *SCREAMING_SNAKE_CASE* (**Constantes** )

 Para valores que **no deben cambiar** durante la ejecución.

```python
MAX_INTENTOS_LOGIN = 3  # constante en SCREAMING_SNAKE_CASE
TIEMPO_EXPIRACION_TOKEN = 3600
IVA_CHILE = 0.19
```

 **Buena práctica clave**

* Define constantes al inicio del archivo o módulo
* Nunca las modifiques

---

##  5. Variables privadas (convención con guión bajo)

###  Un guión bajo (`_`)

 Uso interno o temporal

```python
_resultado_temporal = 42
```

---

###  Dos guiones bajos (`__`)

 *Name mangling* (clases)

```python
class Cuenta:
    def __init__(self):
        self.__saldo = 0
```

 Se transforma internamente en `_Cuenta__saldo`

---

##  6. Variables “débiles” (malas prácticas)

```python
x = 10          # poco descriptivo
data = 123      # ambiguo
var = "hola"    # sin contexto
```

 Evitar salvo en bucles muy cortos:

```python
for i in range(3):
    print(i)
```

---

##  Resumen rápido

| Caso                  | Formato                      | Recomendación |
| --------------------- | ---------------------------- | -------------- |
| Variables y funciones | `snake_case`               |  SI          |
| Constantes            | `SCREAMING_SNAKE_CASE`     |  SI          |
| Clases                | `PascalCase`               |  SI          |
| camelCase             | `camelCase`                |  NO          |
| Variables privadas    | `_variable`/`__variable` |  Convención |

---

  **Regla de oro en Python** :

 *Si no es una clase ni una constante → usa `snake_case`.*
