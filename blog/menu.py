# menu.py - Menú del blog y manejo de input()

from blog.datos import estados_post


def mostrar_menu():
    """Muestra el menú y retorna la opción elegida como número, o None si no es un número."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")
    try:
        opcion = int(input("Elegí una opción: "))
    except ValueError:
        print("Error: tenés que ingresar un número del 1 al 7.")
        return None
    return opcion


def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios; retorna None si quedó vacío."""
    texto = input(mensaje).strip()
    if texto == "":
        print("Error: no podés dejar este campo vacío.")
        return None
    return texto


def pedir_texto_obligatorio(mensaje):
    """Vuelve a pedir el texto hasta que el usuario escriba algo."""
    while True:
        texto = pedir_texto(mensaje)
        if texto is not None:
            return texto


def pedir_datos_post():
    """Pide por consola los datos de un post nuevo y los retorna en un diccionario."""
    print("\n--- NUEVO POST ---")
    titulo = pedir_texto_obligatorio("Título: ")
    contenido = pedir_texto_obligatorio("Contenido: ")

    # Los tags se escriben separados por coma, por ejemplo: Python, Web
    texto_tags = pedir_texto_obligatorio("Tags (separados por coma): ")
    tags = [tag.strip() for tag in texto_tags.split(",") if tag.strip() != ""]

    print(f"Estados posibles: {', '.join(estados_post)}")
    while True:
        estado = pedir_texto_obligatorio("Estado: ").lower()
        if estado in estados_post:
            break
        print("Error: ese estado no existe, elegí uno de la lista.")

    return {"titulo": titulo, "contenido": contenido, "tags": tags, "estado": estado}
