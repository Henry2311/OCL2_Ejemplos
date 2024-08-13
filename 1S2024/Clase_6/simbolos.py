from enum import Enum

class TIPO_DATO(Enum):
    ENTERO = 1
    STRING = 1
    FUNCION = 10

class Simbolos(): #VALOR - NODO
    
    def __init__(self, id, tipo, valor, instrucciones = [], parametros = [], props = {}):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.instrucciones = instrucciones
        self.parametros = parametros
        self.props = props

class TablaSimbolos():

    def __init__(self, simbolos = {}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print('Error variable no definida')
        else:
            return self.simbolos[id]
    
    def actualizar(self, id, valor):
        if not id in self.simbolos:
            print('Error variable no definida')
        else:
            self.simbolos[id].valor = valor