# Documentación adicional del proyecto

## Objetivo
Este documento complementa la documentación existente del repositorio y resume decisiones editoriales aplicadas para mejorar la consistencia del material académico.

## Cambios realizados

### 1) Estandarización de contenido textual
- Se eliminaron caracteres emoji en archivos Markdown, HTML y Python.
- Se mantuvieron los textos originales en español y la estructura de cada archivo.
- Cuando un emoji formaba parte de una etiqueta visual (por ejemplo, títulos o mensajes), se conservó el contenido semántico sin iconografía.

### 2) Alcance de la limpieza
La revisión incluyó contenidos en:
- Documentación general del repositorio.
- Materiales por módulo (M2, M3, M4 y M5).
- Ejemplos de interfaz en HTML.
- Scripts y ejemplos educativos en Python.

## Criterio de edición aplicado
- Se priorizó la neutralidad visual para facilitar reutilización en contextos formales o institucionales.
- No se alteró la lógica de programas ni estructuras SQL.
- No se realizaron refactorizaciones funcionales fuera de la limpieza de caracteres.

## Recomendación para futuras contribuciones
Para mantener consistencia en el repositorio:
1. Evitar uso de emojis en encabezados, mensajes de consola y comentarios.
2. Preferir texto descriptivo y explícito en su lugar.
3. Verificar cambios con búsqueda por rango Unicode antes de hacer commit.

## Comando sugerido de verificación
```bash
rg -nP "[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]"
```

Si el comando no devuelve resultados, no hay emojis detectados en los rangos más comunes.
