# main.py - Punto de entrada del blog por consola (Módulo 6)
# Este archivo solo coordina el programa: la lógica está en las clases y módulos del paquete "blog".

from blog.modelos import Autor, Blog
from blog.datos import cargar_posts, guardar_posts, perfil_autor
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.operaciones import mostrar_posts, mostrar_validacion
from blog.validaciones import validar_post


def iniciar():
    """Carga los posts, crea el blog y mantiene el menú activo hasta salir."""
    # 1. Se cargan los posts desde posts.json (ya vienen como objetos Post)
    posts = cargar_posts()

    # 2. Se crea la instancia de Blog con esa lista de posts
    blog = Blog(posts)

    # 3. El autor de los posts nuevos es un objeto Autor
    autor = Autor.from_dict(perfil_autor)

    while True:
        opcion = mostrar_menu()

        # Si ingresó texto, el menú ya mostró el error y se vuelve a pedir
        if opcion is None:
            continue

        if opcion == 1:
            print("\nPosts disponibles:")
            mostrar_posts(blog.listar_posts(), "No hay posts para mostrar.")

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino is not None:
                print(f"\nResultados para '{termino}':")
                mostrar_posts(blog.buscar_por_titulo(termino),
                              "No se encontraron posts con ese título.")

        elif opcion == 3:
            tag = pedir_texto("Ingresá un tag: ")
            if tag is not None:
                print(f"\nPosts con el tag '{tag}':")
                mostrar_posts(blog.filtrar_por_tag(tag), "No hay posts con ese tag.")

        elif opcion == 4:
            datos = pedir_datos_post()
            nuevo = blog.crear_post(datos["titulo"], datos["contenido"], autor,
                                    datos["tags"], datos["estado"])
            print(f"Post creado con id {nuevo.id}. Acordate de guardarlo con la opción 6.")

        elif opcion == 5:
            mostrar_validacion(blog.validar_posts(validar_post))

        elif opcion == 6:
            if guardar_posts(blog.obtener_posts()):
                print("Posts guardados correctamente en posts.json.")

        elif opcion == 7:
            # Antes de salir se guarda automáticamente para no perder nada
            if guardar_posts(blog.obtener_posts()):
                print("Se guardaron los posts antes de salir.")
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    iniciar()
    