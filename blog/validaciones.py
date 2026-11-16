# validaciones.py - Reglas lógicas para validar los posts

from blog.datos import estados_post


def validar_post(post):
    """Verifica que un post cumpla las reglas.
    Retorna (True, mensaje) si es válido o (False, mensaje de error) si no lo es."""
    claves_obligatorias = ("id", "titulo", "contenido", "autor", "tags", "estado")

    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    if not isinstance(post["titulo"], str) or post["titulo"].strip() == "":
        return False, "el título está vacío"

    if not isinstance(post["contenido"], str) or post["contenido"].strip() == "":
        return False, "el contenido está vacío"

    if not isinstance(post["autor"], dict):
        return False, "el autor no es un diccionario"

    if "nombre" not in post["autor"]:
        return False, 'el autor no tiene la clave "nombre"'

    if not isinstance(post["tags"], list):
        return False, "los tags no son una lista"

    if post["estado"] not in estados_post:
        return False, f'el estado "{post["estado"]}" no está permitido'

    return True, "válido"


def validar_todos(lista):
    """Valida cada post de la lista y muestra cuáles son válidos y cuáles tienen errores."""
    print("\nResultado de la validación:")
    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        if es_valido:
            print(f"Post {numero}: válido")
        else:
            print(f"Post {numero}: error - {mensaje}")