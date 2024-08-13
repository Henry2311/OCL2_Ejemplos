from enum import Enum

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4

class OPERACION_LOGICA(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    NO_IGUAL = 4
    MENOR_IGUAL = 5

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionBinaria(ExpresionNumerica):

    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionLogica():
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNegativo(ExpresionNumerica) :
    def __init__(self, exp) :
        self.exp = exp

class ExpresionNumero(ExpresionNumerica):
    
    def __init__(self, val = 0) :
        self.val = val

class ExpresionID(ExpresionNumerica):
    def __init__(self, id) :
        self.id = id

class ExpresionAccesoInterface(ExpresionNumerica):
    def __init__(self, id, prop) :
        self.id = id
        self.prop = prop

class ExpresionCadena:
    ''' Clase abstracta para cadenas'''

class ExpresionDobleComilla(ExpresionCadena):

    def __init__(self, val) :
        self.val = val

class ExpresionInterface:
    
    def __init__(self, id, props):
        self.id = id
        self.props = props