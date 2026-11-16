# main.py - Punto de entrada del blog por consola (Módulo 5)
# Este archivo solo coordina el programa: la lógica está en el paquete "blog".

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag, mostrar_resultados
from blog.validaciones import validar_todos


def iniciar():
    """Mantiene el menú activo hasta que el usuario elija salir."""
    while True:
        opcion = mostrar_menu()

        # Si ingresó texto, el menú ya mostró el error y se vuelve a pedir
        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_texto("Buscar por titulo: ")
            if termino is not None:
                print(f"\nResultados para '{termino}':")
                mostrar_resultados(buscar_por_titulo(posts, termino),
                                   "No se encontraron posts con ese título.")

        elif opcion == 3:
            tag = pedir_texto("Ingresá un tag: ")
            if tag is not None:
                print(f"\nPosts con el tag '{tag}':")
                mostrar_resultados(filtrar_por_tag(posts, tag),
                                   "No hay posts con ese tag.")

        elif opcion == 4:
            validar_todos(posts)

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    iniciar() 