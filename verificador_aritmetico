'''
Compiladores
Operaciones Aritméticas
25 de septiembre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''

import re
import sys

def es_operador(caracter):
    return caracter in "+-*/"

def es_numero(caracter):
    return caracter.isdigit() or (caracter == '.')

def calcular_resultado(num_primero, signo, num_segundo):
    if signo == '+':
        return num_primero + num_segundo
    elif signo == '-':
        return num_primero - num_segundo
    elif signo == '*':
        return num_primero * num_segundo
    elif signo == '/':
        if num_segundo == 0:
            raise ValueError("Error: División por cero")
        return num_primero / num_segundo
    
def disparador_errores(expresion):
    if not re.match(r'^\s*[-+]?\d*\.?\d+\s*([-+*/]\s*[-+]?\d*\.?\d+\s*)*$', expresion):
        raise ValueError("ERROR. LA EXPRESIÓN NO ES VÁLIDA")

def operar_expresion(expresion):
    numeros = []
    operadores = []
    temp = ""
    disparador_errores(expresion)
    for caracter in expresion:
        if caracter == ' ':
            continue
        elif es_numero(caracter) or (caracter == '-' and not temp):
            temp += caracter
        elif es_operador(caracter):
            if temp:
                numeros.append(float(temp))
                print("Numeros: ", numeros)
                temp = ""
            while operadores and (caracter in "+-" or operadores[-1] in "*/"):
                print("Operadores", operadores)
                print("Caracter: ", caracter)
                num2 = numeros.pop()
                num1 = numeros.pop()
                operador = operadores.pop()
                resultado = calcular_resultado(num1, operador, num2)
                print("Resultado:", resultado)
                numeros.append(resultado)
            operadores.append(caracter)
        else:
            print(f'Caracter no válido: {caracter}')
            sys.exit(1)

    if temp:
        numeros.append(float(temp))

    while operadores:
        num2 = numeros.pop()
        num1 = numeros.pop()
        operador = operadores.pop()
        resultado = calcular_resultado(num1, operador, num2)
        numeros.append(resultado)

    if len(numeros) == 1:
        print('El resultado de la operación es:', numeros[0])
    else:
        print('Expresión no válida')


expresion = input("Ingresa una expresión aritmética: ")
try:
    operar_expresion(expresion)
except ValueError as e:
    print(e)
