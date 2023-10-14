'''
Compiladores
Analizador Sintáctico
10 de octubre de 2023
Integrantes:
Roberto Alejandro Castillo
Yellsmy Lilibeth Toj García
'''

import ply.yacc as yacc
from analizadorLexico import tokens, lexer
import Verificador_delimitadores


#--------------- Definición de reglas -------------------#

# Reglas de producción para la estructura del programa
def p_program(p):
    """
    program : class_declaration
           | program class_declaration
    """
    
    p[0] = ("program: ",p[1:])
    


# Reglas de producción para declaración de la clase
def p_class_declaration(p):
    """
    class_declaration : CLASS ID LBRACE class_body RBRACE
    """
    
    p[0] = ("class: ",p[4])
    


# Reglas de producción para el cuerpo de la clase
def p_class_body(p):
    """
    class_body : statement main 
               | class_body statement
               | main
               | statement class_body
    """
    
    p[0] = ("body: ", p[1:])
    

# Reglas de producción para el método main
def p_main(p):
    ''' main : PUBLIC STATIC VOID MAIN LPAREN STRING LBRACKET RBRACKET ARGS RPAREN LBRACE statements RBRACE  '''
    
    p[0] = ("main: ", p[12])
    


# Reglas de producción para sentencias
def p_statement(p):
    '''statement : assignment
                | array_usage
                | print_statement
                | dcl_variable SEMI
                | for_statement
                | if_statement'''
    
    p[0] = ( p[1:]) 
    #print("statement: ", p[0])
    


# Reglas de producción para expresiones
def p_expression(p):
    """
    expression : ID
               | NUMBER
               | ID EQUALS propiedades
               | ID GT propiedades
               | ID GE propiedades
               | ID LE propiedades
               | ID LT propiedades
               | NOT expression
    """
    
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = (p[1])
    #print("expression: ", p[0])
    


# Reglas de producción para condiciones
def p_condicion(p):
    ''' condicion : ID EQUALS NUMBER
               | ID GT NUMBER
               | ID GE NUMBER
               | ID LE NUMBER
               | ID LT NUMBER
               | ID AND NUMBER
               | ID OR NUMBER
               | NUMBER EQUALS NUMBER
               | NUMBER GT NUMBER
               | NUMBER GE NUMBER
               | NUMBER LE NUMBER
               | NUMBER LT NUMBER
               | ID AND ID
               | ID OR ID
               | ID EQ ID 
               | ID EQ STRING_LITERAL '''
    
    p[0] = ("condicion: ", p[1], p[2], p[3])
    


# Reglas de producción para incrementos o decrementos
def p_increment_or_decrement(p):
    ''' increment_or_decrement : ID INCREMENT
                               | ID DECREMENT '''
    
    p[0] = ("increment or decrement: ", p[1], p[2])
    


# Reglas de producción para bucles for y for-each 
def p_for_statement(p):
    ''' for_statement : FOR LPAREN INT ID EQUALS NUMBER SEMI condicion SEMI increment_or_decrement RPAREN LBRACE statements RBRACE
                      | FOR LPAREN INT ID EQUALS NUMBER SEMI expression SEMI increment_or_decrement RPAREN LBRACE statements RBRACE
                      | FOR LPAREN tipo_palabra ID COLON ID RPAREN LBRACE statements RBRACE'''
    
    p[0] = ("for:", p[1:]) 
    #print("for: ", p[0])
    


# Reglas de producción para sentencias if
def p_if_statement(p):
    """
    if_statement : IF LPAREN condicion RPAREN LBRACE statements RBRACE
                | IF LPAREN condicion RPAREN LBRACE statements RBRACE ELSE statements 
                | IF LPAREN condicion RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    """
    
    p[0] = ( p[1:]) 
    #print("if_statement: ", p[0])
    


# Reglas de producción para varios argumentos
def p_args(p):
    """
    args : arg
         | args arg
    """
    
    if len(p) == 2:
        p[0] = ["args: ",p[1]]
    else:
        p[0] = p[1] + [p[2]]
    


# Reglas de producción de un argumento
def p_arg(p):
    """
    arg : ID
         | STRING_LITERAL
         | NUMBER
         | NOT arg
         | ID COMMA
         | STRING_LITERAL COMMA
         | NUMBER COMMA
    """
    
    p[0] = ("arg: ",p[1])
    


# Reglas de producción para propiedades de una objeto
def p_propiedades(p):
    ''' propiedades : ID PUNTO ID'''
    
    p[0] = ("propiedades", p[1], p[3])
    


# Producción statements:
#- Secuencia de declaraciónes que pueden consistir en una sola declaración 
#- Secuencia de declaracones compuesta por una secuencia existente de declaraciones seguida de una declaración adicional
def p_statements(p):
    '''statements : statement
                  | statements statement'''
    
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
    #print("statements: ", p[0])
    
    

# Reglas de producción de asignación de valores a variables
def p_assignment(p):
    '''assignment : ID EQUALS expression SEMI'''
    
    p[0] = (p[1], p[2], p[3], p[4])
    #print("assignment: ", p[0])
    


# Reglas de producción de declaración de variables:
#- Declaración de variales que contengan números
#- Declaración de variables que contengan cadena
#- Declaración de variables que contengan valor booleano
def p_dcl_variable(p):
    '''dcl_variable : tipo_number ID EQUALS NUMBER
                    | tipo_palabra ID EQUALS STRING_LITERAL
                    | tipo_booleano ID EQUALS valor_boolean'''
    
    p[0] = (p[1], p[2], p[4])
    #print("dcl_variable: ", p[0])
    


# Reglas de producción de tipo_booleano
def p_tipo_booleano(p):
    '''tipo_booleano : BOOLEAN'''
    
    p[0] = ("type_boolean: ", p[1])
    

# Reglas de producción de tipo_number
def p_tipo_number(p):
    '''tipo_number : INT
                    | DOUBLE'''
    
    p[0] = ("type_number: : ", p[1])
    

# Reglas de producción de tipo_booleano
def p_tipo_palabra(p):
    '''tipo_palabra : STRING'''
    
    p[0] = ("type_string: ", p[1])
    

# Reglas de producción de valores booleanos que puede ser True o False
def p_valor_boolean(p):
    '''valor_boolean : TRUE
                    | FALSE'''
    
    p[0] = ("boolean: ", p[1])
    

# Reglas de producción de creación de listas
def p_array_usage(p):
    '''array_usage : tipo_number LBRACKET RBRACKET ID EQUALS LBRACE args RBRACE SEMI
                    | tipo_palabra LBRACKET RBRACKET ID EQUALS LBRACE args RBRACE SEMI'''
    
    p[0] = ( "array_usage", p[1:])
    #print("array: ", p[0])
    

# Reglas de producción de impresión
def p_print_statement(p):
    '''print_statement : SYSTEM PUNTO OUT PUNTO PRINTLN LPAREN STRING_LITERAL RPAREN SEMI
                       | SYSTEM PUNTO OUT PUNTO PRINTLN LPAREN ID RPAREN SEMI
                       | SYSTEM PUNTO OUT PUNTO PRINTLN LPAREN ID LBRACKET ID RBRACKET RPAREN SEMI'''
    
    p[0] = ('print_statement', p[7])
    #print("print: ", p[0])
    

# Vacío
def p_empty(p):
    '''empty :'''
    pass

# Función de manejo de errores
def p_error(p):
    if p:
        print(f"Sintaxis incorrecta en la línea {p.lineno}: antes del token '{p.value}'")


#--------------- Construcción del analizador sintáctico -------------------#

# Crea el analizador
parser = yacc.yacc()

# Método para imprimir el árbol
def print_ast(node, level=0):
    indentation = " " * level * 2
    if isinstance(node, tuple):
        print(f"{indentation}{node[0]}")
        for child in node[1:]:
            print_ast(child, level + 1)
    elif isinstance(node, list):
        for child in node:
            print_ast(child, level + 1)
    else:
        print(f"{indentation}{node}")


def call_Parse(source_code):
    result = parser.parse(source_code)
    if result is not None:
        print("Análisis sintáctico exitoso")
        print_ast(result)
    else:
        print("Error de análisis sintáctico")
        

# Datos para prueba individual
data = """
class HelloWorld {
    public static void main(String[] args) {
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
        
        String palabra = "Hola mundo"
        
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
    }
}
"""

#call_Parse(data)
