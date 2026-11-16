# datos.py - Estructuras de datos base del blog (vienen del Módulo 2 y 4)

# Diccionario con el perfil del autor
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

# Lista de posts: los 3 primeros son correctos y los 2 últimos tienen errores a propósito
posts = [
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
    },
    {
        # Post incompleto: le falta la clave "contenido"
        "id": 4,
        "titulo": "Post sin contenido",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "publicado"
    },
    {
        # Post incorrecto: título vacío, tags como texto y estado inexistente
        "id": 5,
        "titulo": "",
        "contenido": "Este post tiene varios datos mal cargados.",
        "autor": perfil_autor,
        "tags": "Python",
        "estado": "pendiente"
    }
]
