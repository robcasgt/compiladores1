#Pragrama que nos devuelve el conteo de numero de lineas de un archivo y en listas las palabras, numeros y simbolos especiales.
#Realizado Lilibeth Garcia y Roberto Castillo
import string

def contar_lineas_palabras_numeros_signos(contenido):
    # Inicializar listas para guardar las palabras, números y signos
    palabras = []
    numeros = []
    signos = []

    lineas = contenido.count('\n') + 1

    # Aquí separa las palabras, números y signos
    for palabra in contenido.split():
        palabra_limpia = palabra.strip(string.punctuation)  # Eliminar signos de puntuación de la palabra
        if palabra_limpia.isnumeric():
            numeros.append(palabra_limpia)
        elif palabra_limpia:
            palabras.append(palabra_limpia)
        else:
            signos.append(palabra)

    return lineas, palabras, numeros, signos

if __name__ == "__main__":
    nombre_archivo = input("Ingresa el nombre del archivo de texto: ")

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

            lineas, palabras, numeros, signos = contar_lineas_palabras_numeros_signos(contenido)

            print(f"El archivo '{nombre_archivo}' tiene {lineas} líneas.")
            print(f"Palabras encontradas: {palabras}")
            print(f"Números encontrados: {numeros}")
            print(f"Signos encontrados: {signos}")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
