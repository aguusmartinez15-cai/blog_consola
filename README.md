# Blog por consola - Módulo 5

Sistema de blog que funciona desde la consola. Permite ver los posts, buscarlos por título, filtrarlos por tag y validar que sus datos estén bien cargados.

En este módulo separé el código del Módulo 4, que estaba en un solo archivo, en varios módulos dentro de un paquete llamado `blog`.

## Cómo ejecutarlo

1. Abrí la terminal en la carpeta raíz del proyecto (donde está `main.py`).
2. Ejecutá:

```
python main.py
```

## Estructura del proyecto

```
blog_consola/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Qué hace cada archivo

- **main.py**: es el archivo que se ejecuta. Importa las funciones del paquete `blog` y coordina el menú.
- **blog/__init__.py**: hace que Python reconozca la carpeta `blog` como un paquete.
- **blog/datos.py**: tiene los datos base: `perfil_autor`, `estados_post`, `etiquetas_blog` y la lista `posts`. El autor es un diccionario anidado dentro de cada post.
- **blog/menu.py**: muestra el menú y maneja lo que escribe el usuario con `input()`.
- **blog/operaciones.py**: funciones para listar, buscar por título y filtrar por tag. Usan `.lower()` para ignorar mayúsculas.
- **blog/validaciones.py**: revisa que cada post sea un diccionario, tenga todas las claves, título y contenido no vacíos, autor como diccionario con nombre, tags como lista y un estado válido.

## Opciones del menú

1. Ver todos los posts (título, autor y estado)
2. Buscar por título
3. Filtrar por tag
4. Validar posts
5. Salir

Los posts 4 y 5 tienen errores a propósito para probar la validación.