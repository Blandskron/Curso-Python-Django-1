¿Cómo verlo en tu consola?

Abre un intérprete de Python y escribe:

```python
import this
```

Te va a mostrar el Zen de Python completo en inglés.

---

### Resumen del Zen de Python (explicado en simple)

Te lo traduzco y explico en versión “humana”:

1. **Bello es mejor que feo**

   Tu código debería ser legible y ordenado, no un enredo.
2. **Explícito es mejor que implícito**

   Que el código deje claro lo que hace, sin “magia oculta”.
3. **Simple es mejor que complejo**

   Si puedes resolver algo de forma simple, no lo compliques.
4. **Complejo es mejor que enmarañado**

   Si realmente tiene que ser complejo, al menos que no sea un caos imposible de entender.
5. **Plano es mejor que anidado**

   Evita demasiados niveles de `if`, `for`, funciones dentro de funciones, etc.
6. **Disperso es mejor que denso**

   Un poco de espacio y líneas en blanco ayuda a leer mejor el código.
7. **La legibilidad cuenta**

   Escribe código pensando en la persona que lo leerá (incluyéndote a ti en 6 meses).
8. **Los casos especiales no son lo suficientemente especiales como para romper las reglas**

   No inventes excepciones raras a tus propias convenciones por “esta única vez”.
9. **Aunque la practicidad le gana a la pureza**

   Está bien ser pragmático: si una solución no es 100% “perfecta” pero funciona y es clara, suele estar bien.
10. **Los errores nunca deberían pasar silenciosamente**

    Si algo falla, mejor saberlo (excepciones, logs, mensajes claros).
11. **A menos que se silencien explícitamente**

    Si decides ignorar un error, que sea una decisión consciente y clara.
12. **Frente a la ambigüedad, rechaza la tentación de adivinar**

    Si algo no está claro, mejor ser explícito, documentar o pedir más información.
13. **Debería haber una —y preferiblemente solo una— forma obvia de hacerlo**

    Favorecer una “forma estándar” de resolver cada problema en la comunidad.
14. **Aunque esa forma no sea obvia al principio a menos que seas holandés 😄**

    Chiste interno sobre Guido van Rossum (creador de Python, que es holandés).
15. **Ahora es mejor que nunca**

    Es mejor hacerlo que no hacerlo.
16. **Aunque nunca suele ser mejor que *justo ahora mismo***

    No hagas las cosas apuradas si eso arruina el diseño a futuro.
17. **Si la implementación es difícil de explicar, es una mala idea**

    Si ni tú puedes explicarla fácilmente, probablemente está mal diseñada.
18. **Si la implementación es fácil de explicar, puede ser una buena idea**

    La claridad suele ser una señal de buen diseño.
19. **Los espacios en blanco son importantes**

    En Python la indentación define bloques; respétala y úsala bien.


## 1️⃣ VARIABLES

### ❌ Anti-Zen (poco claro, confuso)

```python
x = 10
y = 5
z = x * y
```

### ✅ Pro-Zen (explícito y legible)

```python
precio = 10
cantidad = 5
total = precio * cantidad
```

👉 **Zen aplicado:** *La legibilidad cuenta*

---

## 2️⃣ IF / CONDICIONALES

### ❌ Anti-Zen (implícito, difícil de entender)

```python
if x > 7:
    a = True
else:
    a = False
```

### ✅ Pro-Zen (simple y directo)

```python
es_mayor = x > 7
```

👉 **Zen aplicado:** *Simple es mejor que complejo*

---

### ❌ Anti-Zen (anidación innecesaria)

```python
if edad >= 18:
    if edad < 65:
        print("Adulto")
```

### ✅ Pro-Zen (condición clara)

```python
if 18 <= edad < 65:
    print("Adulto")
```

👉 **Zen aplicado:** *Plano es mejor que anidado*

---

## 3️⃣ FOR

### ❌ Anti-Zen (poco pythonico)

```python
numeros = [1, 2, 3, 4, 5]
i = 0
for i in range(len(numeros)):
    print(numeros[i])
```

### ✅ Pro-Zen (forma directa)

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

👉 **Zen aplicado:** *Debería haber una forma obvia de hacerlo*

---

### ❌ Anti-Zen (todo en una línea ilegible)

```python
for i in range(5): print(i*i*i)
```

### ✅ Pro-Zen (claridad primero)

```python
for i in range(5):
    cubo = i ** 3
    print(cubo)
```

👉 **Zen aplicado:** *Disperso es mejor que denso*

---

## 4️⃣ WHILE

### ❌ Anti-Zen (riesgo de bucle infinito)

```python
contador = 0
while True:
    print(contador)
    contador += 1
```

### ✅ Pro-Zen (condición explícita)

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

👉 **Zen aplicado:** *Explícito es mejor que implícito*

---

## 5️⃣ FUNCIONES (`def`)

### ❌ Anti-Zen (hace muchas cosas)

```python
def f(a, b):
    c = a + b
    print(c)
    if c > 10:
        print("Grande")
    return c * 2
```

### ✅ Pro-Zen (una responsabilidad clara)

```python
def sumar(a, b):
    return a + b


def es_grande(numero):
    return numero > 10
```

👉 **Zen aplicado:** *Simple es mejor que complejo*

---

### ❌ Anti-Zen (difícil de explicar)

```python
def x(y):
    return y*y if y > 0 else y-1
```

### ✅ Pro-Zen (se entiende al leer)

```python
def calcular_valor(numero):
    if numero > 0:
        return numero ** 2
    return numero - 1
```

👉 **Zen aplicado:** *Si es difícil de explicar, es mala idea*

---

## 6️⃣ CLASES

### ❌ Anti-Zen (nombres confusos, poco claros)

```python
class A:
    def __init__(self, x):
        self.x = x

    def f(self):
        return self.x * 2
```

### ✅ Pro-Zen (intención clara)

```python
class Producto:
    def __init__(self, precio):
        self.precio = precio

    def calcular_precio_final(self):
        return self.precio * 2
```

👉 **Zen aplicado:** *Explícito es mejor que implícito*

---

### ❌ Anti-Zen (atributos mágicos)

```python
class User:
    def __init__(self, a, b):
        self.a = a
        self.b = b
```

### ✅ Pro-Zen (nombres claros)

```python
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

👉 **Zen aplicado:** *La legibilidad cuenta*

---

## 7️⃣ ERRORES

### ❌ Anti-Zen (error silencioso)

```python
try:
    resultado = 10 / 0
except:
    pass
```

### ✅ Pro-Zen (error visible)

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
```

👉 **Zen aplicado:** *Los errores nunca deberían pasar silenciosamente*

---

## 🔑 RESUMEN RÁPIDO

✅ Buen Python (Pro-Zen):

* Nombres claros
* Código corto y legible
* Una cosa bien hecha
* Fácil de explicar

❌ Mal Python (Anti-Zen):

* Variables `x`, `a`, `f`
* Mucha anidación
* Magia y trucos innecesarios
* Código imposible de leer
