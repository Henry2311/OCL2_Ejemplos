
# Lista de tokens
tokens = (
    'CONSOLE',
    'LOG',
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PUNTO',
    'PUNTOCOMA',
    'CADENA',
    'ENTERO',
    'COMMENTBLOCK'
)

t_CONSOLE  = r'console'
t_LOG  = r'log'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PUNTO    = r'\.'
t_PUNTOCOMA    = r';'

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

def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''

def p_instruccion_console(t):
    '''instruccion : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA'''
    print(t[5])

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | CADENA'''
    t[0] = t[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")



import ply.lex as Lex
import ply.yacc as yacc

if __name__ == '__main__':
    input_text = '''
            //ESTE ES UN COMENTARIO DE LINEA
            /*
                ESTE ES UN 
                COMENTARIO
                DE BLOQUE
                */
            console.log("Esto es una suma");
            console.log(((5+5)*2)/5);
            '''
    lexer = Lex.lex()
    parser = yacc.yacc()

    result = parser.parse(input_text)
