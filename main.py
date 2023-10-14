'''
Compilador
Fase 1 y 2
10 de octubre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''
import sys
import analizadorLexico
import os, time
import analizadorSintactico

# Barra de progreso
def barra_progreso():
    time.sleep(0.50)
    banner = ["█", "██", "███","████","█████","██████","███████",\
        "████████","█████████","█████████", "███████████","█████████████","███████████████","100%"]
    L = len(banner)
    n = 1
    for j in range(0,n):
        for i in range(0,L):
            os.system("cls")
            print(banner[i])
            time.sleep(0.02)

# Crea el nombre del nuevo archivo
def nombre__crear_archivo():
    contador = 1
    while True:
        nombre_archivo = f"tokens_{contador}.txt"
        if not os.path.exists(nombre_archivo):
            break
        contador += 1
    return nombre_archivo

# Ejecuta el analizador léxico
def ejecutarALexico(entrada):
    tokensValidos = analizadorLexico.ejecutar(entrada)
    guardar_archivo = input("¿Desea almacenar los tokens válidos en un archivo? (Sí/No): ")
    if guardar_archivo.lower() == "si" or guardar_archivo.lower() == "s":
        nombre_archivo= nombre__crear_archivo()
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                for token in tokensValidos:
                    archivo.write(f"{token}\n")
                print(f"Los tokens se han almacenado en el archivo '{nombre_archivo}'.")
            archivo.close()
        except Exception as e:
            print(f"Ocurrió un error al almacenar los tokens en el archivo: {e}")
            
    imprimir = input("¿Desea ver los tokens válidos almacenados? (Si/No): ")
    if imprimir.lower() == "si" or imprimir.lower() == "s":
        for token in tokensValidos:
            print(token)

# Ejecuta el analizador sintáctico
def ejecutarASintactico(nombre_archivo):
    
    with open(nombre_archivo, 'r') as archivo:
        codigo = archivo.read()
        archivo.close()
        if not analizadorSintactico.Verificador_delimitadores.ejecutar_verificador(codigo):
            sys.exit(1)
    analizadorSintactico.call_Parse(codigo)

# Principal
def main():
    try:
        print('¡BIENVENIDO!')
        nombre_archivo = input("Ingresa el nombre del archivo de código que quieres analizar: ")
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            entrada = archivo.read()
            print("Ejecutando analizador léxico, espere un momento")
            #barra_progreso()
            ejecutarALexico(entrada)
        aSintactico = input("¿Desea ejecutar el analizador sintáctico?: (Si/No)")
        if aSintactico.lower() == "si" or aSintactico.lower() == "s":
            ejecutarASintactico(nombre_archivo)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"Ocurrió un error al analizar el archivo: {e}")


if __name__ == "__main__":
    main()



