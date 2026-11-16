# menu.py - Menú del blog y manejo de input()


def mostrar_menu():
    """Muestra el menú y retorna la opción elegida como número, o None si no es un número."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        opcion = int(input("Elegí una opción: "))
    except ValueError:
        print("Error: tenés que ingresar un número del 1 al 5.")
        return None
    return opcion


def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios; retorna None si quedó vacío."""
    texto = input(mensaje).strip()
    if texto == "":
        print("Error: no podés dejar este campo vacío.")
        return None
    return texto
