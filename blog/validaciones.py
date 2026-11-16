# validaciones.py - Reglas para validar los posts (ahora trabajan con objetos)

from blog.datos import estados_post
from blog.modelos import Autor, Post


def validar_post(post):
    """Verifica que un objeto Post tenga datos correctos.
    Retorna (True, mensaje) si es válido o (False, mensaje de error) si no lo es."""
    if not isinstance(post, Post):
        return False, "no es un objeto Post"

    if not isinstance(post.titulo, str) or post.titulo.strip() == "":
        return False, "el título está vacío"

    if not isinstance(post.contenido, str) or post.contenido.strip() == "":
        return False, "el contenido está vacío"

    if not isinstance(post.autor, Autor):
        return False, "el autor no es un objeto Autor"

    if not isinstance(post.autor.nombre, str) or post.autor.nombre.strip() == "":
        return False, "el autor no tiene nombre"

    if not isinstance(post.tags, list):
        return False, "los tags no son una lista"

    if post.estado not in estados_post:
        return False, f'el estado "{post.estado}" no está permitido'

    return True, "válido"

