
reservadas = {
    'console':'CONSOLE',
    'log':'LOG',
    'let':'LET',
    'if':'IF',
    'else' : 'ELSE'
}

# Lista de tokens
tokens = [
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'PUNTO',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'TIPONUMBER',
    'CADENA',
    'ENTERO',
    'COMMENTBLOCK',
    'ID',
    'IGUAL',
    'LLAVIZQ',
    'LLAVDER'
] + list(reservadas.values())

t_CONSOLE  = r'console'
t_LOG  = r'log'
t_LET  = r'let'
t_IF  = r'if'
t_TIPONUMBER = r'number'
t_DOSPUNTOS = r':'
t_IGUAL     = r'='
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='
t_PUNTO    = r'\.'
t_PUNTOCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_CADENA(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error %d", t.value)
        t.value = ''
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')  


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)


precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )


from expresiones import *
from instrucciones import *

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir_instr
                        | declaracion_instr
                        | asignacion_instr
                        | if_instr
                        | if_else_instr
    '''
    t[0] = t[1]

def p_instruccion_console(t):
    '''imprimir_instr : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA'''
    t[0] = Imprimir(t[5])

def p_instruccion_declaracion(t):
    '''declaracion_instr : LET ID IGUAL expresion PUNTOCOMA'''
    t[0] = Declaracion(t[2], t[4])

def p_instruccion_asignacion(t):
    '''asignacion_instr : ID IGUAL expresion PUNTOCOMA'''
    t[0] = Asignacion(t[1], t[3])

def p_if_instr(t) :
    'if_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA'
    t[0] = If(t[3], t[6])

def p_if_else_instr(t) :
    'if_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMA'
    t[0] = IfElse(t[3], t[6], t[10])

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

def p_expresion_logica(t):
    '''expresion : expresion MAYQUE expresion
                  | expresion MENQUE expresion
                  | expresion IGUALQUE expresion
                  | expresion NIGUALQUE expresion'''
    if t[2] == '>'  : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.NO_IGUAL)

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_cadena(t):
    '''expresion    : CADENA'''
    t[0] = ExpresionDobleComilla(t[1])

def p_expresion_id(t):
    '''expresion    : ID'''
    t[0] = ExpresionID(t[1])

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")

import ply.lex as Lex
import ply.yacc as yacc
lexer = Lex.lex()
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)