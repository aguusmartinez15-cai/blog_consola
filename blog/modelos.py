# modelos.py - Clases principales del blog (Módulo 6)


class Autor:
    """Representa a la persona que escribe en el blog."""

    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def to_dict(self):
        """Convierte el autor en un diccionario para poder guardarlo en JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un objeto Autor a partir de un diccionario."""
        if not isinstance(datos, dict) or "nombre" not in datos:
            raise ValueError('el autor está incompleto, falta "nombre"')
        return cls(
            datos["nombre"],
            datos.get("bio", ""),
            datos.get("especialidad", ""),
            datos.get("redes_sociales", [])
        )


class Post:
    """Representa una publicación del blog. El autor es un objeto Autor."""

    CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")

    def __init__(self, id, titulo, contenido, autor, tags, estado):
        # Composición: el post tiene adentro un objeto Autor, no un texto
        if not isinstance(autor, Autor):
            raise TypeError("el autor del post tiene que ser un objeto Autor")
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        """Convierte el post en un diccionario (el autor también se convierte)."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un objeto Post a partir de un diccionario cargado desde JSON."""
        if not isinstance(datos, dict):
            raise ValueError("el post no es un diccionario")
        faltan = [clave for clave in cls.CLAVES_OBLIGATORIAS if clave not in datos]
        if faltan:
            raise ValueError(f"el post está incompleto, falta: {', '.join(faltan)}")
        autor = Autor.from_dict(datos["autor"])
        return cls(datos["id"], datos["titulo"], datos["contenido"],
                   autor, datos["tags"], datos["estado"])


class Blog:
    """Centraliza la lógica del blog. Tiene una lista de objetos Post."""

    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def obtener_posts(self):
        """Retorna todos los posts cargados."""
        return self.posts

    def listar_posts(self):
        """Retorna la lista de posts para mostrarla en el menú."""
        return self.posts

    def buscar_por_titulo(self, termino):
        """Retorna los posts cuyo título contiene el término, sin importar mayúsculas."""
        termino = termino.lower()
        resultados = []
        for post in self.posts:
            if isinstance(post.titulo, str) and termino in post.titulo.lower():
                resultados.append(post)
        return resultados

    def filtrar_por_tag(self, tag):
        """Retorna los posts que tienen ese tag, sin importar mayúsculas."""
        tag = tag.lower()
        resultados = []
        for post in self.posts:
            # Si los tags no son una lista, el post se saltea para evitar errores
            if not isinstance(post.tags, list):
                continue
            for etiqueta in post.tags:
                if isinstance(etiqueta, str) and etiqueta.lower() == tag:
                    resultados.append(post)
                    break
        return resultados

    def siguiente_id(self):
        """Calcula el id del próximo post."""
        ids = [post.id for post in self.posts if isinstance(post.id, int)]
        return max(ids) + 1 if ids else 1

    def crear_post(self, titulo, contenido, autor, tags, estado):
        """Crea un objeto Post nuevo, lo agrega al blog y lo retorna."""
        nuevo_post = Post(self.siguiente_id(), titulo, contenido, autor, tags, estado)
        self.posts.append(nuevo_post)
        return nuevo_post

    def validar_posts(self, funcion_validar):
        """Valida cada post con la función recibida.
        Retorna una lista de tuplas (numero, es_valido, mensaje)."""
        resultados = []
        for numero, post in enumerate(self.posts, start=1):
            es_valido, mensaje = funcion_validar(post)
            resultados.append((numero, es_valido, mensaje))
        return resultados

    def to_list(self):
        """Convierte todos los posts del blog en una lista de diccionarios."""
        return [post.to_dict() for post in self.posts]
