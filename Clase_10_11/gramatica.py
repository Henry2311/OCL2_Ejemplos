
reservadas = {
    'console':'CONSOLE',
    'log':'LOG',
    'let':'LET',
    'number': 'NUMBER',
    'string': 'STRING',
    'if':'IF',
    'else' : 'ELSE',
    'function': 'FUNCTION',
    'interface': 'INTERFACE',
    'return': 'RETURN',
    'break': 'BREAK',
    'while': 'WHILE'
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
    'AND',
    'OR',
    'ID',
    'IGUAL',
    'LLAVIZQ',
    'LLAVDER',
    'COMA',
    'MENORIGUAL'
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
t_MENORIGUAL  = r'<='
t_NIGUALQUE = r'!='
t_PUNTO    = r'\.'
t_PUNTOCOMA    = r';'
t_AND   = r'&&'
t_OR    = r'\|\|'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_COMA   = r','

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
from simbolos import TIPO_DATO

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
                        | while_instr
                        | funcion_instr
                        | call_funcion_instr
                        | interface_instr
                        | return_instr
                        | break_instr
    '''
    t[0] = t[1]

def p_instruccion_break(t):
    '''break_instr     : BREAK PUNTOCOMA'''
    t[0] = BreakInstr()

def p_instruccion_retorno(t):
    '''return_instr     : RETURN expresion PUNTOCOMA
                        | RETURN PUNTOCOMA'''
    if len(t) == 4:
        t[0] = ReturnInstr(t[2])
    else:
        t[0] = ReturnInstr(None)

def p_instruccion_interface(t):
    '''interface_instr : INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDER'''
    t[0] = ExpresionInterface(t[2],t[4])

def p_instruccion_interface_params(t):
    '''interface_params : interface_params PUNTOCOMA ID DOSPUNTOS expresion
                        | ID DOSPUNTOS expresion'''

    if(len(t) == 4):
        t[0] = {t[1]: t[3]} 
    else:
        t[1][t[3]] = t[5]
        t[0] = t[1]

# def p_tipo_dato(p):
#     """ tipo_dato : STRING
#                 | NUMBER """
    
#     if p.slice[1].type == 'STRING':
#         p[0] = TIPO_DATO.STRING
#     elif p.slice[1].type == 'NUMBER':
#         p[0] = TIPO_DATO.ENTERO

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

def  p_funcion_instr(t) :
    'funcion_instr      : FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA' 
    params = [t[4], t[6]]
    t[0] = Function(t[2], parametros=params, instrucciones=t[9])

def  p_call_funcion_instr(t) :
    'call_funcion_instr      : ID PARIZQ expresion COMA expresion PARDER PUNTOCOMA'
    params = [t[3], t[5]]
    t[0] = CallFunction(t[1],params=params)

def p_if_else_instr(t) :
    'if_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMA'
    t[0] = IfElse(t[3], t[6], t[10])

def p_while_instr(t) :
    'while_instr      : WHILE PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA'
    t[0] = While(t[3], t[6])

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
    '''expresion :  expresion AND expresion
                  | expresion OR expresion
                  | expresion MAYQUE expresion
                  | expresion MENQUE expresion
                  | expresion IGUALQUE expresion
                  | expresion NIGUALQUE expresion
                  | expresion MENORIGUAL expresion'''
    if t[2] == '>'  : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.NO_IGUAL)
    elif t[2] == '<=': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_IGUAL)
    elif t[2] == '&&': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.AND)
    elif t[2] == '||': t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.OR)

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
    '''expresion    : ID
                    | ID PUNTO ID
                    | ID PARIZQ expresion COMA expresion PARDER'''
    if(len(t)==2):
        t[0] = ExpresionID(t[1])
    elif(len(t)==7):
        params = [t[3], t[5]]
        t[0] = CallFunction(t[1],params=params)
    else:
        t[0] = ExpresionAccesoInterface(t[1], t[3])

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