# 7.1 – Características principales de un VCS (Git)

Esta sección resume lo que hace que Git sea tan usado en el desarrollo front-end y back-end.

---

## 1. Historial completo y local

Git guarda **todo el historial en tu máquina**:

- Puedes ver commits sin internet.
- Puedes volver a versiones anteriores sin depender de servidores.
- Cuando sincronizas con GitHub, solo envías los cambios.

---

## 2. Trabajo con ramas

Las **ramas** permiten:

- Probar nuevas funcionalidades sin romper `main`.
- Tener varias versiones del proyecto (por ejemplo, versión de producción y versión de desarrollo).
- Hacer pruebas, prototipos, hotfixes, etc.

Ejemplo de nombres de ramas:

- `feature/login`
- `bugfix/navbar-responsive`
- `hotfix/logo-roto`

---

## 3. Mezcla de cambios (Merge)

Cuando una rama está lista:

- Se hace un **merge** hacia otra rama (por ejemplo, `feature/login` → `main`).
- Git intenta unir los cambios automáticamente.
- Si hay conflictos, te los muestra para que los resuelvas.

---

## 4. Restauración de archivos

Si borras un archivo sin querer o rompes algo:

- Puedes recuperar una versión anterior con Git.
- No necesitas tener 20 copias del mismo archivo con nombres distintos.

---

## 5. Integración con repositorios remotos (GitHub, GitLab, etc.)

- Git fue diseñado para trabajar tanto **local** como **remoto**.
- GitHub ofrece:
  - Copia de seguridad en la nube
  - Trabajo colaborativo
  - Pull Requests
  - Issues, Wiki, etc.

Git = motor de control de versiones.  
GitHub = plataforma para alojar y colaborar sobre repos Git.
