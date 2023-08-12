#Programa que  lee un archivo de texto con código y muestra lista de con tokens identificados
#Realizado por Roberto Castillo y Yellsmy Toj

import re

def identificar_tokens(codigo):

    keywords = {'while', 'if', 'return', 'cout', 'cin'}
    operadores_aritmeticos = {'+', '-', '*', '/', '%'}
    operadores_logicos = {'&&', '||', '>', '<', '==', '!='}
    simbolos_especiales = {'(', ')', '[', ']', '{', '}'}
    
    tokens_palabras_clave = []
    tokens_identificadores =[]
    tokens_operadores = []
    tokens_operadores_lógicos = []
    tokens_simbolos_especiales = []

    lineas = codigo.split('\n')
    for linea in lineas:
        palabras = re.findall(r"[\w]+|[^\s\w]", linea)
        for palabra in palabras:
            if palabra in keywords:
                tokens_palabras_clave.append(palabra)
            elif re.match(r"^[a-zA-Z_]\w*$", palabra):
                tokens_identificadores.append(palabra)
            elif palabra in operadores_aritmeticos:
                tokens_operadores.append(palabra)
            elif palabra in operadores_logicos:
                tokens_operadores_lógicos.append(palabra)
            elif palabra in simbolos_especiales:
                tokens_simbolos_especiales.append(palabra)
    
    return tokens_palabras_clave, tokens_identificadores, tokens_operadores, tokens_operadores_lógicos, tokens_simbolos_especiales

if __name__ == "__main__":
    nombre_archivo = input("Ingresa el nombre del archivo de código: ")
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            entrada = archivo.read()

            palabras_claves, identificadores, operadores, operadores_logicos, simbolos_especiales  = identificar_tokens(entrada)

            print(f"Palabras Clave: {palabras_claves}")
            print(f"Identificadores: {identificadores}")
            print(f"Operadores Aritméticos: {operadores}")
            print(f"Operadores Lógicos: {operadores_logicos}")
            print(f"Símbolos Especiales: {simbolos_especiales}")
            

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
