# operaciones.py - Funciones principales del blog: listar, buscar y filtrar


def obtener_nombre_autor(post):
    """Retorna el nombre del autor de forma segura, sin generar KeyError."""
    autor = post.get("autor")
    if isinstance(autor, dict):
        return autor.get("nombre", "Autor desconocido")
    return "Autor desconocido"


def mostrar_post(post):
    """Muestra un post con su título, autor y estado."""
    if not isinstance(post, dict):
        print("- (post con formato inválido)")
        return
    titulo = post.get("titulo") or "(sin título)"
    estado = post.get("estado", "sin estado")
    print(f"- {titulo} | Autor: {obtener_nombre_autor(post)} | Estado: {estado}")


def listar_posts(lista):
    """Recorre la lista de posts y muestra cada uno."""
    if not lista:
        print("No hay posts para mostrar.")
        return
    print("\nPosts disponibles:")
    for post in lista:
        mostrar_post(post)


def buscar_por_titulo(lista, termino):
    """Retorna los posts cuyo título contiene el término, sin importar mayúsculas."""
    resultados = []
    termino = termino.lower()
    for post in lista:
        if isinstance(post, dict):
            titulo = post.get("titulo", "")
            if isinstance(titulo, str) and termino in titulo.lower():
                resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    """Retorna los posts que tienen ese tag, sin importar mayúsculas."""
    resultados = []
    tag = tag.lower()
    for post in lista:
        if not isinstance(post, dict):
            continue
        tags = post.get("tags", [])
        # Si tags no es una lista, el post se saltea para evitar errores
        if not isinstance(tags, list):
            continue
        for etiqueta in tags:
            if isinstance(etiqueta, str) and etiqueta.lower() == tag:
                resultados.append(post)
                break
    return resultados


def mostrar_resultados(resultados, mensaje_vacio):
    """Muestra los posts encontrados o un mensaje claro si no hay resultados."""
    if not resultados:
        print(mensaje_vacio)
        return
    for post in resultados:
        mostrar_post(post) 
        