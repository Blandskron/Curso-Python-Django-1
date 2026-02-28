#  E-commerce por Consola en Python

Proyecto educativo de  **e-commerce por consola** , desarrollado en Python, enfocado en  **buenas prácticas** , **arquitectura limpia** y  **separación de responsabilidades** .

Este proyecto implementa un sistema simple de tienda con roles **Administrador** y  **Cliente** , manejo de catálogo, carrito de compras y flujo de compra completo.

---

##  Objetivos del Proyecto

* Aplicar **PEP8** y el **Zen of Python**
* Diseñar una arquitectura clara y escalable
* Separar  **dominio** , **casos de uso** y **UI**
* Evitar lógica mezclada (sin prints en el dominio)
* Facilitar mantenimiento y futuras extensiones

---

##  Arquitectura General

El proyecto está dividido en  **capas claras** :

```
solucion/
│
├── main.py                  # Punto de entrada
│
├── models/                  # Dominio (sin UI)
│   ├── producto.py
│   ├── carrito.py
│   ├── user/
│   │   └── usuario.py
│   └── catalogo/
│       ├── catalogo.py
│       ├── inventario.py
│       ├── consultas.py
│       ├── errores.py
│       └── __init__.py
│
├── app/                     # Orquestación y casos de uso
│   ├── tienda.py
│   ├── seed.py
│   ├── menus.py
│   ├── admin_actions.py
│   └── cliente_actions.py
│
└── ui/                      # Presentación por consola
    └── catalogo_view.py
```

---

##  Separación de Responsabilidades

###  Dominio (`models/`)

* **No contiene `print()`**
* Solo reglas de negocio y datos
* Totalmente testeable
* Ejemplos:
  * `Catalogo`
  * `Producto`
  * `Carrito`

###  Casos de Uso (`app/`)

* Orquestan acciones del usuario
* Coordinan dominio + UI
* Ejemplos:
  * crear producto
  * agregar al carrito
  * confirmar compra

###  UI (`ui/`)

* Única capa que imprime en consola
* No contiene lógica de negocio

---

##  Roles del Sistema

###  Administrador

Puede:

* Listar catálogo
* Crear productos
* Actualizar productos
* Eliminar productos
* Sumar stock

###  Cliente

Puede:

* Ver catálogo
* Buscar productos
* Agregar productos al carrito
* Ver carrito y total
* Confirmar compra

---

## ▶ Cómo Ejecutar el Proyecto

### Requisitos

* Python **3.10+** (probado en 3.13)

### Ejecutar

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

---

##  Principios Aplicados

###  Zen of Python

* Simple es mejor que complejo
* Explícito es mejor que implícito
* Cada módulo hace una sola cosa

###  PEP8

* Nombres claros
* Imports explícitos
* Docstrings en módulos, clases y métodos

###  Diseño Pythonico

* Composición sobre herencia
* Funciones pequeñas
* Evita objetos innecesarios
* Dominio desacoplado de UI

---

##  Posibles Mejoras Futuras

* Persistencia en archivo (JSON / CSV)
* Tests unitarios (`pytest`)
* Descuentos e impuestos
* Autenticación real de usuarios
* Interfaz gráfica o web

---

##  Estado del Proyecto

 Funcional
 Arquitectura limpia
 Cumple estándares
 Apto para evaluación académica

---

##  Autor

Proyecto desarrollado como ejercicio formativo en Python, enfocado en  **buenas prácticas** , **arquitectura limpia** y  **pensamiento de diseño de software** .
