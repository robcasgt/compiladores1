'''
Compiladores
Analizador Léxico
25 de septiembre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''

import sys
import ply.lex as lex
resultado_lexema = []

# Nombres de tokens
tokens = [

     # Tipos de valores o literales
    'ID', 'NUMBER', 'TYPEID', 'INTEGER', 'STRING_LITERAL', 'CHARACTER',

    # Operadores
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Operadores de asignación
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Operadores de incremento o decremento
    'INCREMENT', 'DECREMENT',

    # Operador de ternario 
    'TERNARY',

    # Delimitadores
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PUNTO', 'SEMI', 'COLON',
]

# Palabras reservadas
reserved = {
    "int": "INT",
    "char": "CHAR",
    "float": "FLOAT",
    "if": "IF",
    "else": "ELSE",
    "do": "DO",
    "while": "WHILE",
    "return": "RETURN",
    "void": "VOID",
    "#include": "INCLUDE",
    "String": "STRING",
    "args": "ARGS",
    "public": "PUBLIC",
    "static": "STATIC",
    "main": "MAIN",
    "class": "CLASS",
    "System": "SYSTEM",
    "out": "OUT",
    "println": "PRINTLN",
    "true": "TRUE",
    "false": "FALSE",
    "boolean": "BOOLEAN",
    "double": "DOUBLE",
    "for": "FOR",
    "True": "TRUE",
    "False": "FALSE",
    "package": "PACKAGE",
}


# Se agrega a la lista de tokens las palabras reservadas
tokens += list(reserved.values())


# Expresiones regualres para tokens simples

# Operadores
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'%'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LSHIFT           = r'<<'
t_RSHIFT           = r'>>'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

# Operadores de asiganción

t_EQUALS        = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='
t_LSHIFTEQUAL      = r'<<='
t_RSHIFTEQUAL      = r'>>='
t_ANDEQUAL         = r'&='
t_OREQUAL          = r'\|='
t_XOREQUAL         = r'\^='

# Operadores de incremento o decremento
t_INCREMENT        = r'\+\+'
t_DECREMENT        = r'--'

# ?
t_TERNARY          = r'\?'

# Delimitadores
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_PUNTO           = r'\.'
t_SEMI             = r';'
t_COLON            = r':'
t_STRING_LITERAL = r'"[^"]*"'



# Expresión regular para identificadores insensibles a mayúsculas y minúsculas
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "ID")  
    return t



# Expresión regular para números enteros y decimales


def t_INVALID_NUMBER(t):
    r"\d+\.\d+\.\d+"
    print(f"Error: Número inválido '{t.value}'")
    sys.exit(1)
    #t.lexer.skip(1)

def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.type = "NUMBER"
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t
   
# Expresión reglar para ignorar comentarios
def t_COMMENT(t):
    r"\/\/.*"
    pass

# Expresión regular paraignorar comentarios de bloque
def t_COMMENTBLOCK(t):
    r"\/\*(.|\n)*\*\/"
    pass


# Manejo de saltos de línea para hacer un seguimiento del número de línea actual en el código fuente
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #global lineno
    #lineno += len(t.value)  # Actualiza el número de línea


# Ignorar espacios en blanco o tabulaciones
t_ignore = " \t"

# Manejo de errores 
def t_error(t):
    print("Caracter inválido '%s'" % t.value[0])
    sys.exit(1)
    #t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

def ejecutar(data):
    global resultado_lexema
    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Tipo {:4} Valor {:16} Linea {:16} Posicion {:4}".format(str(tok.type),str(tok.value) ,str(tok.lineno), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

def tokenize():
    data = """
    if (puntaje >= 90) {
        System.out.println("Excelente puntaje.");
    } else if (puntaje >= 70) {
        System.out.println("Buen puntaje.");
    } else {
        System.out.println("Puntaje regular.");
    }
    """
    lexer.input(data)
    for token in lexer:
        print(f"Token: {token}")
data = """
    for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}

for (String color : colores) {
    System.out.println(color);
}

for (int i = 0; i < numeros.length; i++) {
    System.out.println(numeros[i]);
}

int puntaje = 85;

boolean isTrue = True;

String palabra = "Hola mundo";

double precio = 3.99;

String[] colores = {"azul", "morado", "rosa", "amarillo"};

int[] numeros = {1, 2, 3, 4, 5};

int[] objetos_cocina = {mesa, silla, estufa, cuchillo};

if (puntaje >= 90) {
    System.out.println("Excelente puntaje.");
} else if (puntaje >= 70) {
    System.out.println("Buen puntaje.");
} else {
    System.out.println("Puntaje regular.");
}

    """

#lista = ejecutar(data)
#for l in lista:
    #print(l)

#tokenize()
