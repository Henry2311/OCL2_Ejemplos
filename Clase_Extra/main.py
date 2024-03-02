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

def procesar_if(instr, ts):
    expLog = resolver_expresion_logica(instr.expLogica, ts)
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy()) 
        procesar_instrucciones(instr.instrucciones,TablaLocal)

def procesar_if_else(instr, ts):
    expLog = resolver_expresion_logica(instr.expLogica, ts)
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        procesar_instrucciones(instr.instrIfVerdadero,TablaLocal)
    else:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        procesar_instrucciones(instr.instrIfFalso,TablaLocal)

def resolver_expresion(expCad, ts) :
    if isinstance(expCad, ExpresionBinaria) :
        exp = resolver_expresion_aritmetica(expCad, ts)
        return exp
    elif isinstance(expCad, ExpresionLogica):
        exp = resolver_expresion_logica(expCad, ts)
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

def resolver_expresion_logica(expLog, ts):
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)

    if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.NO_IGUAL : return exp1 != exp2

def procesar_funcion(instr, ts):
    fun_ = ts.obtener(instr.id).instrucciones
    
    if len(fun_) > 0:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())

    # for params in instr.params:
    #     exp = resolver_expresion(params.exp)
    #     TablaLocal.agregar(Simbolos(params.id, TIPO_DATO.ENTERO, exp))

        procesar_instrucciones(fun_,TablaLocal)


def guardar_funcion(instr, ts):
    id = instr.id
    simbolo = Simbolos(id, TIPO_DATO.FUNCION, None, instr.instrucciones, instr.parametros)
    ts.agregar(simbolo)

def procesar_instrucciones(instrucciones, ts, save=False) :
    for instr in instrucciones :
        if not save:
            if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
            elif isinstance(instr, Declaracion): procesar_declaracion(instr, ts)
            elif isinstance(instr, Asignacion): procesar_asignacion(instr, ts)
            elif isinstance(instr, If): procesar_if(instr,ts)
            elif isinstance(instr,IfElse): procesar_if_else(instr, ts)
            elif isinstance(instr,CallFunction): procesar_funcion(instr, ts)
            elif isinstance(instr,Function): pass
            else : print('Error: instrucción no válida')
        else:
            '''OTRA VERIFICACION PARA LA CLASE FUNCION'''
            '''
                si tiene o no parametros
                lista_instruciones

                -> Primer recorrdio 
                    -> TS va a guardar ID -> {Valor}
            '''
            if isinstance(instr, Function): guardar_funcion(instr, ts)
           



if __name__ == '__main__':
    input_text = '''
                //ESTE ES UN COMENTARIO DE LINEA
                /*
                    ESTE ES UN 
                    COMENTARIO
                    DE BLOQUE
                    */

                function imprimir(){
                    console.log("HOLA, PRUEBA DE FUNCION");
                };

                let a = 10;

                if(a > 5){
                    imprimir();
                }else{
                    console.log("A no es mayor que 5");
                };

                '''
    

    instrucciones = g.parse(input_text)
    ts = TablaSimbolos()
    try:
        procesar_instrucciones(instrucciones, ts, save=True)
        procesar_instrucciones(instrucciones, ts)
    except Exception as e:
        print("Error", e)
