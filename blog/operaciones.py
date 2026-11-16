# operaciones.py - Funciones para mostrar los resultados en la consola


def mostrar_post(post):
    """Muestra un post con su título, autor y estado."""
    titulo = post.titulo or "(sin título)"
    print(f"- {titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")


def mostrar_posts(lista, mensaje_vacio):
    """Muestra una lista de posts o un mensaje claro si está vacía."""
    if not lista:
        print(mensaje_vacio)
        return
    for post in lista:
        mostrar_post(post)


def mostrar_validacion(resultados):
    """Muestra el resultado de validar los posts."""
    print("\nResultado de la validación:")
    if not resultados:
        print("No hay posts para validar.")
        return
    for numero, es_valido, mensaje in resultados:
        if es_valido:
            print(f"Post {numero}: válido")
        else:
            print(f"Post {numero}: error - {mensaje}")

            