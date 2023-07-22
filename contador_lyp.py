def contar_lineas_y_palabras_contenido(contenido):
    # Contar líneas
    lineas = contenido.count('\n') + 1

    # Contar palabras
    palabras = sum(1 for palabra in contenido.split() if palabra.strip())

    return lineas, palabras

if __name__ == "__main__":
    nombre_archivo = input("Ingresa el nombre del archivo de texto: ")

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            lineas, palabras = contar_lineas_y_palabras_contenido(contenido)
            print(f"El archivo '{nombre_archivo}' tiene {lineas} líneas y {palabras} palabras.")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
