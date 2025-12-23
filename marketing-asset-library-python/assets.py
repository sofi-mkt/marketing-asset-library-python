# Marketing Asset Library
# Proyecto base para automatización de marketing
# Autor: Sofia
# Nivel: fundamentos de Python

def show_phrases():
    # Para abrir el archivo en modo lectura
    file = open("phrases.txt", "r", encoding="utf-8")

    # Para leer todas las líneas y las guardamos en una lista
    phrases = file.readlines()

    # Cerramos el archivo (muy importante)
    file.close()

    print("\n--- FRASES DISPONIBLES ---")

    # Si el archivo está vacío
    if len(phrases) == 0:
        print("No hay frases cargadas todavía.")
    else:
        # Recorremos cada frase
        for phrase in phrases:
            # strip() elimina saltos de línea
            print("- " + phrase.strip())


def show_images():
    file = open("images.txt", "r", encoding="utf-8")
    images = file.readlines()
    file.close()

    print("\n--- IMÁGENES DISPONIBLES ---")

    if len(images) == 0:
        print("No hay imágenes cargadas todavía.")
    else:
        for img in images:
            print("- " + img.strip())


# Programa principal
while True:
    print("\n=== Marketing Asset Library ===")
    print("1. Ver frases de marketing")
    print("2. Ver imágenes para campañas")
    print("3. Salir")

    option = input("Elegí una opción: ")

    if option == "1":
        show_phrases()
    elif option == "2":
        show_images()
    elif option == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Probá de nuevo.")
