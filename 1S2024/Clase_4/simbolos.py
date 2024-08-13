from enum import Enum

class TIPO_DATO(Enum):
    ENTERO = 1

class Simbolos(): #VALOR - NODO
    
    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.valor = valor

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