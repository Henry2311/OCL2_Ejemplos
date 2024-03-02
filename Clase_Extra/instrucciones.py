class Instruccion:
    '''Clase abs de instrucciones'''


class Imprimir(Instruccion):

    def __init__(self,  cad) :
        self.cad = cad

class Declaracion(Instruccion):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

class Asignacion(Instruccion):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

class If(Instruccion):
    def __init__(self, expLogica, instrucciones = []):
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class IfElse(Instruccion):
    def __init__(self, expLogica, instrIfVerdadero = [], instrIfFalso = []):
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso

class Function(Instruccion):
    def __init__(self, id, parametros = [], instrucciones = []):
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones

class CallFunction(Instruccion):
    def __init__(self, id):
        self.id = id