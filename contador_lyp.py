#Pragrama que nos devuelve el conteo de numero de lineas de un archivo y en listas las palabras, numeros y simbolos especiales.
#Realizado Lilibeth Garcia y Roberto Castillo
import string
import re

def contar_lineas_palabras_numeros_signos(contenido):
    palabras = []
    numeros = []
    signos = []

    lineas = contenido.count('\n') + 1

    # Expresión regular para detectar números enteros y decimales
    regex_numero = r"[-+]?\d*\.\d+|\d+"

    for palabra in contenido.split():
        palabra_limpia = palabra.strip(string.punctuation)
        if re.match(regex_numero, palabra_limpia):
            if '.' in palabra_limpia:  # Verificar si es decimal
                numeros.append(float(palabra_limpia))
            else:
                numeros.append(int(palabra_limpia))
        elif palabra_limpia:
            palabras.append(palabra_limpia)
        else:
            signos.append(palabra)

    return lineas, palabras, numeros, signos

if__name__== "__main__":
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
