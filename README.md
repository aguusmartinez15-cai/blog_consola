# Blog por consola - Módulo 6

Sistema de blog que funciona desde la consola. Permite ver los posts, buscarlos por título, filtrarlos por tag, crear posts nuevos, validarlos y guardarlos en un archivo `posts.json` para que no se pierdan al cerrar el programa.

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
├── posts.json
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Clases principales (blog/modelos.py)

- **Autor**: representa a la persona que escribe. Tiene `nombre`, `bio`, `especialidad` y `redes_sociales`.
- **Post**: representa una publicación. Tiene `id`, `titulo`, `contenido`, `autor`, `tags` y `estado`. El `autor` es un objeto `Autor`, no un texto (composición).
- **Blog**: centraliza la lógica. Tiene una lista de objetos `Post` y métodos para listar, buscar por título, filtrar por tag, crear posts nuevos y validarlos.

## Qué hace cada archivo

- **main.py**: es el archivo que se ejecuta. Carga los posts, crea la instancia de `Blog` y conecta el menú con sus métodos.
- **blog/modelos.py**: tiene las clases `Autor`, `Post` y `Blog`.
- **blog/datos.py**: tiene los datos base y se encarga de cargar y guardar `posts.json`.
- **blog/menu.py**: muestra el menú y pide los datos al usuario con `input()`.
- **blog/operaciones.py**: muestra los posts y los resultados en la consola.
- **blog/validaciones.py**: revisa que cada post tenga título, contenido, autor con nombre, tags como lista y un estado válido.

## Cómo funciona la persistencia con JSON

JSON no puede guardar objetos de Python, por eso las clases se convierten a diccionarios:

- **Guardar**: cada `Post` se convierte a diccionario con `to_dict()`. El autor también se convierte con su propio `to_dict()`. Después la lista se guarda en `posts.json` con `json.dump()`.
- **Cargar**: al iniciar, el programa lee `posts.json` y convierte cada diccionario en un objeto con `Post.from_dict()`, que también arma el objeto `Autor`.

El programa no se cierra si `posts.json` no existe, está vacío o tiene contenido inválido: avisa con un mensaje y carga unos posts iniciales. Si un post del archivo está incompleto, avisa y lo saltea.

## Opciones del menú

1. Ver todos los posts (título, autor y estado)
2. Buscar por título (ignora mayúsculas)
3. Filtrar por tag (ignora mayúsculas)
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir (guarda automáticamente antes de cerrar)

El post 4 de `posts.json` tiene errores a propósito para probar la validación.

## Qué cambió respecto al Módulo 5

- Se agregó `blog/modelos.py` con las clases `Autor`, `Post` y `Blog`.
- Los posts ya no son diccionarios sueltos: son objetos `Post` con un objeto `Autor` adentro.
- La búsqueda y el filtrado ahora son métodos de la clase `Blog`.
- Se agregó la opción para crear posts nuevos desde la consola.
- Se agregó la persistencia: los posts se guardan y se cargan desde `posts.json`.
- `datos.py` ahora se encarga de leer y guardar el archivo JSON.
