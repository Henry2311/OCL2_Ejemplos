import gramatica as g
from expresiones import *
from instrucciones import *


def procesar_imprimir(instr):
    print('>> ', resolver_expresion(instr.cad))


def resolver_expresion(expCad) :
    if isinstance(expCad, ExpresionBinaria) :
        exp = resolver_expresion_aritmetica(expCad)
        return exp
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    else :
        print('Error: Expresión cadena no válida')

def resolver_expresion_aritmetica(expNum) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1)
        exp2 = resolver_expresion_aritmetica(expNum.exp2)

        #Validaciones de tipos, divida por 0



        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    
def procesar_instrucciones(instrucciones) :
    for instr in instrucciones :
        if isinstance(instr, Imprimir) : procesar_imprimir(instr)
        else : print('Error: instrucción no válida')



if __name__ == '__main__':
    input_text = '''
                //ESTE ES UN COMENTARIO DE LINEA
                /*
                    ESTE ES UN 
                    COMENTARIO
                    DE BLOQUE
                    */
                console.log("Hola Mundo :D");
                console.log((4+3)*(5+6));
                console.log((5+6));
                '''
    instrucciones = g.parse(input_text)
    procesar_instrucciones(instrucciones)
