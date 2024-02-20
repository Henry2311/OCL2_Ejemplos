import gramatica as g
from simbolos import TablaSimbolos, Simbolos, TIPO_DATO
from expresiones import *
from instrucciones import *


def procesar_imprimir(instr, ts):
    print('>> ', resolver_expresion(instr.cad, ts))

def procesar_declaracion(instr, ts):
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    simbolo = Simbolos(id, TIPO_DATO.ENTERO, exp)
    ts.agregar(simbolo)

def procesar_asignacion(instr, ts):
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    ts.actualizar(id, exp)

def resolver_expresion(expCad, ts) :
    if isinstance(expCad, ExpresionBinaria) :
        exp = resolver_expresion_aritmetica(expCad, ts)
        return exp
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionID):
        return ts.obtener(expCad.id).valor
    elif isinstance(expCad, ExpresionNumero):
        return expCad.val
    else:
        print('Error: Expresión cadena no válida')

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)

        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionID):
        return ts.obtener(expNum.id).valor
    
def procesar_instrucciones(instrucciones, ts) :
    for instr in instrucciones :
        if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
        elif isinstance(instr, Declaracion): procesar_declaracion(instr, ts)
        elif isinstance(instr, Asignacion): procesar_asignacion(instr, ts)
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

                //console.log(exp);
                //exp -> exp op exp

                console.log((5+6));

                let var1 = (4+3)*(5+6);

                var1 = var1 / 11;

                console.log("Esta es una declaracion");
                console.log(var1);
                '''
    instrucciones = g.parse(input_text)
    ts = TablaSimbolos()
    procesar_instrucciones(instrucciones, ts)
