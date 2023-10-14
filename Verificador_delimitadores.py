'''
Compiladores
Parte 1 Analizador Sintactico
22 de septiembre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''

def verificar_balance(texto):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in texto:
        if char in '([{':
            pila.append(char)
        elif char in ')]}':
            if not pila or pila.pop() != pares[char]:
                return False

    return len(pila) == 0

def ejecutar_verificador(codigo):
    if verificar_balance(codigo):
        print("DELIMITADORES CERRADOS")
        return True
    else:
        print("¡ERROR! Hay paréntesis, corchetes o llaves abiertos o sin cerrar")
        return False
