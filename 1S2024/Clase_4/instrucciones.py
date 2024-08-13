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