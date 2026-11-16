# datos.py - Datos base del blog y persistencia con JSON (Módulo 6)

import json
from pathlib import Path

from blog.modelos import Post

# Ruta del archivo posts.json (queda en la carpeta raíz, al lado de main.py)
RUTA_JSON = Path(__file__).parent.parent / "posts.json"

# Diccionario con el perfil del autor (viene de los módulos anteriores)
perfil_autor = {
    "nombre": "Agustín Martínez",
    "bio": "Estudiante de la diplomatura en IA",
    "especialidad": "Python y IA",
    "redes_sociales": ["@agustin_IA", "@programacionconia"]
}

# Tupla con los estados posibles de un post (datos fijos)
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas únicas ("Python" repetido se guarda una sola vez)
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Posts iniciales: se usan solo si posts.json no existe, está vacío o tiene errores
posts_iniciales = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    }
]


def convertir_a_objetos(lista_dicts):
    """Convierte una lista de diccionarios en objetos Post.
    Si un diccionario está incompleto, avisa y lo saltea."""
    posts = []
    for numero, datos in enumerate(lista_dicts, start=1):
        try:
            posts.append(Post.from_dict(datos))
        except (ValueError, TypeError) as error:
            print(f"Aviso: el post {numero} no se pudo cargar ({error}).")
    return posts


def cargar_posts():
    """Lee posts.json y retorna una lista de objetos Post.
    Si el archivo no existe, está vacío o es inválido, usa los posts iniciales."""
    if not RUTA_JSON.exists():
        print("Aviso: no se encontró posts.json. Se cargan los posts iniciales.")
        return convertir_a_objetos(posts_iniciales)

    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError:
        print("Error: no se pudo leer posts.json. Se cargan los posts iniciales.")
        return convertir_a_objetos(posts_iniciales)

    if contenido.strip() == "":
        print("Aviso: posts.json está vacío. Se cargan los posts iniciales.")
        return convertir_a_objetos(posts_iniciales)

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError:
        print("Error: posts.json tiene contenido inválido. Se cargan los posts iniciales.")
        return convertir_a_objetos(posts_iniciales)

    if not isinstance(datos, list):
        print("Error: posts.json no tiene una lista de posts. Se cargan los posts iniciales.")
        return convertir_a_objetos(posts_iniciales)

    return convertir_a_objetos(datos)


def guardar_posts(lista_posts):
    """Convierte los objetos Post a diccionarios y los guarda en posts.json.
    Retorna True si se guardó bien y False si hubo un error."""
    lista_dicts = []
    for post in lista_posts:
        # JSON no sabe guardar objetos: primero hay que convertirlos a diccionario
        if not isinstance(post, Post):
            print("Error: hay un elemento que no es un Post y no se puede convertir a diccionario.")
            return False
        lista_dicts.append(post.to_dict())

    try:
        with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
            json.dump(lista_dicts, archivo, indent=4, ensure_ascii=False)
    except TypeError:
        print("Error: algún dato no se puede guardar en JSON.")
        return False
    except OSError:
        print("Error: no se pudo escribir el archivo posts.json.")
        return False
    return True
