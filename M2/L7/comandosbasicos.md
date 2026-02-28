
---

#  Guía Básica para Aprender a Usar GitHub

### *Usando únicamente los comandos esenciales que solicitaste*

GitHub es una plataforma que permite almacenar proyectos, colaborar con equipos y mantener un historial de cambios. Para trabajar con GitHub desde tu computadora, utilizamos Git, que es el sistema de control de versiones.

En esta guía aprenderás a moverte y trabajar con repositorios usando solo los siguientes comandos:

* `git add .`
* `git commit -m "comentario"`
* `git push origin nombrerama`
* `git pull origin nombredelarama`
* `git branch nombrerama`
* `git checkout nombrederama`

---

##  1. Crear o clonar un repositorio (concepto)

Antes de usar cualquier comando, debes tener un repositorio en tu computador.

Esto ocurre de dos formas:

1. **Lo creas en GitHub y luego lo clonas**
2. **Lo creas en tu computador y luego lo envías a GitHub**

*(No agrego comandos extras porque lo solicitaste, pero entendamos el concepto.)*

---

##  2. Crear una nueva rama

Una rama es una “línea de trabajo” separada.

Se usa para trabajar ordenadamente sin romper el código principal.

###  Crear una rama:

```
git branch nombrerama
```

> Ejemplo:
>
> `git branch founder/blandskron`

Esto solo **crea** la rama, pero no te mueve a ella.

---

##  3. Cambiarse a una rama

Para comenzar a trabajar en la rama recién creada:

```
git checkout nombrederama
```

> Ejemplo:
>
> `git checkout founder/blandskron`

Ahora todo lo que hagas quedará registrado en esa rama.

---

##  4. Preparar los archivos para subirlos

Cuando realizas cambios en tus archivos, Git no los sube automáticamente.

Primero debes  **prepararlos** .

###  Agregar todos los archivos modificados:

```
git add .
```

Esto toma **todos los archivos que cambiaron** y los deja listos para ser confirmados.

---

##  5. Crear un commit

Un *commit* es una “foto” del estado de tu trabajo, con un mensaje descriptivo.

```
git commit -m "comentario"
```

> Ejemplo:
>
> `git commit -m "Agregué la pantalla de login"`

El comentario debe explicar  **qué hiciste** .

---

##  6. Subir los cambios a GitHub

Una vez hecho el commit, debes enviar la rama con sus cambios al repositorio remoto en GitHub.

```
git push origin nombrerama
```

> Ejemplo:
>
> `git push origin founder/blandskron`

Esto sube los cambios a GitHub y actualiza la rama.

---

##  7. Traer cambios desde GitHub a tu computador

Si alguien más trabajó en la misma rama, o si volviste después de unos días, es importante actualizar tu copia local.

```
git pull origin nombredelarama
```

> Ejemplo:
>
> `git pull origin main`

Esto baja los cambios realizados por otros colaboradores para evitar conflictos.

---

#  Flujo básico de trabajo con GitHub (resumen)

Aquí tienes el flujo típico de uso siguiendo **solo tus comandos:**

1. **Crear una rama:**

   `git branch feature-login`
2. **Cambiarse a esa rama:**

   `git checkout feature-login`
3. **Hacer cambios en el proyecto.**
4. **Agregar los archivos modificados:**

   `git add .`
5. **Crear un commit con mensaje:**

   `git commit -m "Creación del login"`
6. **Subir los cambios a GitHub:**

   `git push origin feature-login`
7. **Si necesitas actualizar tu rama con cambios remotos:**

   `git pull origin feature-login`

---

#  Consejos finales

* Trabaja SIEMPRE en tu propia rama.
* Haz commits frecuentes con mensajes claros.
* Haz `git pull` antes de comenzar y antes de hacer `push`.
* No uses otros comandos hasta dominar completamente este flujo.
