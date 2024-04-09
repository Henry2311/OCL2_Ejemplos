import gramatica as g
from simbolos import TablaSimbolos, Simbolos, TIPO_DATO
from expresiones import *
from instrucciones import *


def procesar_imprimir(instr, ts):
    exp, size = resolver_expresion(instr.cad, ts)

    if isinstance(instr.cad, ExpresionBinaria) :
        ts.salida += f'''la a1, {exp}
                     li a2, {size}
                     jal ra, console_log'''
    elif isinstance(instr.cad, ExpresionLogica):
        ts.salida += f'''la a1, {exp}
                     li a2, {size}
                     jal ra, console_log'''
    elif isinstance(instr.cad, ExpresionDobleComilla) :
        ts.salida += f'''la a1, {exp}
                         li a2, {size}
                         li a0, 1 
                         li a7, 64 
                         ecall\n'''
    elif isinstance(instr.cad, ExpresionID):
        temporal = ts.generateTemporal()
        ts.salida += f'''la t{temporal}, {exp}
                         lw a0, 0(t{temporal})
                         li a7, 1
                         ecall\n'''
    elif isinstance(instr.cad, ExpresionNumero):
        ts.salida += f'''la a0, {exp}
                         li a7, 1
                         ecall\n'''

def procesar_declaracion(instr, ts):
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    simbolo = Simbolos(id, TIPO_DATO.ENTERO, exp)
    ts.agregar(simbolo)
    ts.dato += f'{id}: .word 0\n'
    lasttemporal = ts.lastTemporal()
    temporal = ts.generateTemporal()
    ts.salida += f'la t{temporal}, {id}\n'
    ts.salida += f'sw t{lasttemporal}, 0(t{ts.lastTemporal()})\n'

def procesar_asignacion(instr, ts):
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    lasttemporal = ts.lastTemporal()
    temporal = ts.generateTemporal()
    ts.salida += f'la t{temporal}, {id}\n'
    ts.salida += f'sw t{lasttemporal}, 0(t{ts.lastTemporal()})\n'

def procesar_if(instr, ts):
    expLog = resolver_expresion_logica(instr.expLogica, ts)
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy()) 
        instr, tipo_instr = procesar_instrucciones(instr.instrucciones,TablaLocal)
        if isinstance(tipo_instr, ReturnInstr):
            return instr, tipo_instr
        elif isinstance(tipo_instr, BreakInstr):
            return None
        
def procesar_if_else(instr, ts):
    expLog = resolver_expresion_logica(instr.expLogica, ts)
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        instr, tipo_instr = procesar_instrucciones(instr.instrIfVerdadero,TablaLocal)
        if isinstance(tipo_instr, ReturnInstr):
            return instr, tipo_instr
    else:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        instr, tipo_instr = procesar_instrucciones(instr.instrIfFalso,TablaLocal)
        if isinstance(tipo_instr, ReturnInstr):
            return instr, tipo_instr

def resolver_expresion(expCad, ts) :
    if isinstance(expCad, ExpresionBinaria) :
        exp = resolver_expresion_aritmetica(expCad, ts)
        return exp
    elif isinstance(expCad, ExpresionLogica):
        exp = resolver_expresion_logica(expCad, ts)
        return exp
    elif isinstance(expCad, ExpresionDobleComilla) :
        msg = ts.generateMsg()
        cadena = expCad.val.replace('"','')
        ts.dato += f'msg{msg}: .asciz "{cadena}"\n'
        return f'msg{msg}', len(cadena)
    elif isinstance(expCad, ExpresionID):
        exp_id =  ts.obtener(expCad.id)
        if exp_id.valor is None:
            return exp_id.props

        return exp_id.id, 0
    elif isinstance(expCad, ExpresionAccesoInterface):
        exp_id =  ts.obtener(expCad.id)
        
        if expCad.prop in exp_id.props:
            return exp_id.props[expCad.prop]
    
        return None
    elif isinstance(expCad, CallFunction):
        exp = procesar_funcion(expCad, ts)
        if(isinstance(exp,tuple)):
            return exp[0]
        else:
            return exp
    elif isinstance(expCad, ExpresionNumero):
        temporal = f't{ts.generateTemporal()}'
        ts.salida += f'addi {temporal}, zero, {expCad.val}\n'
        return temporal
    else:
        print('Error: Expresión cadena no válida')

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)

        if expNum.operador == OPERACION_ARITMETICA.MAS : 
            temporal = f't{ts.generateTemporal()}'
            ts.salida += f'add {temporal}, {exp1}, {exp2}\n'
            return temporal
        if expNum.operador == OPERACION_ARITMETICA.MENOS : 
            temporal = f't{ts.generateTemporal()}'
            ts.salida += f'sub {temporal}, {exp1}, {exp2}\n'
            return temporal
        if expNum.operador == OPERACION_ARITMETICA.POR : 
            temporal = f't{ts.generateTemporal()}'
            ts.salida += f'mul {temporal}, {exp1}, {exp2}\n'
            return temporal
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO :
            temporal = f't{ts.generateTemporal()}'
            ts.salida += f'div {temporal}, {exp1}, {exp2}\n'
            return temporal
    elif isinstance(expNum, ExpresionNumero) :
        temporal = f't{ts.generateTemporal()}'
        ts.salida += f'addi {temporal}, zero, {expNum.val}\n'
        return temporal
    elif isinstance(expNum, ExpresionID):
        exp_id =  ts.obtener(expNum.id)
        return exp_id.valor
    elif isinstance(expNum, CallFunction):
        exp = procesar_funcion(expNum, ts)
        if(isinstance(exp,tuple)):
            return exp[0]
        else:
            return exp
    elif isinstance(expNum, ExpresionAccesoInterface):
        exp_id =  ts.obtener(expNum.id)
        
        if expNum.prop in exp_id.props:
            return exp_id.props[expNum.prop]
    
        return None

def resolver_expresion_logica(expLog, ts):
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)

    if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.NO_IGUAL : return exp1 != exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_IGUAL : return exp1 <= exp2

def procesar_funcion(instr, ts):
    fun_ = ts.obtener(instr.id).instrucciones
    params_ = ts.obtener(instr.id).parametros
    if len(fun_) > 0:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        for i in range(len(instr.params)):
            exp = resolver_expresion(instr.params[i], TablaLocal)
            TablaLocal.agregar(Simbolos(params_[i],TIPO_DATO.ENTERO, exp))
        
        instr, tipo_instr = procesar_instrucciones(fun_, TablaLocal)
        
        if isinstance(tipo_instr, ReturnInstr):
            return instr, tipo_instr

def procesar_retorno(instr, ts):
    return resolver_expresion(instr.exp, ts)

def procesar_break(instr,ts):
    return instr

def guardar_funcion(instr, ts):
    funcion_id = instr.id

    simbolo = Simbolos(funcion_id, TIPO_DATO.FUNCION, instr.parametros, instr.instrucciones, instr.parametros)
    ts.agregar(simbolo)

def guardar_interface(instr, ts):
    interface_id = instr.id

    props = instr.props
    keys = list(props.keys())
    values = list(props.values())

    for i in range(len(keys)):
        instr.props[keys[i]] = resolver_expresion(values[i], ts)

    simbolo = Simbolos(interface_id, TIPO_DATO.FUNCION, valor=None, props=instr.props)
    ts.agregar(simbolo)

def procesar_instrucciones(instrucciones, ts, save=False) :
    for instr in instrucciones :
        if not save:
            if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
            elif isinstance(instr, Declaracion): procesar_declaracion(instr, ts)
            elif isinstance(instr, Asignacion): procesar_asignacion(instr, ts)
            elif isinstance(instr, If): 
                ret_ = procesar_if(instr,ts)
                if ret_ is not None:
                    return ret_
            elif isinstance(instr,IfElse): 
                ret_ = procesar_if_else(instr, ts)
                if ret_ is not None:
                    return ret_
            elif isinstance(instr,CallFunction): return procesar_funcion(instr, ts)
            elif isinstance(instr,ReturnInstr): return procesar_retorno(instr, ts), instr
            elif isinstance(instr,BreakInstr): return procesar_break(instr, ts), instr
            elif isinstance(instr,Function): pass
            elif isinstance(instr,ExpresionInterface): pass
            else : print('Error: instrucción no válida', instr)
        else:
            '''OTRA VERIFICACION PARA LA CLASE FUNCION'''
            '''
                si tiene o no parametros
                lista_instruciones

                -> Primer recorrdio 
                    -> TS va a guardar ID -> {Valor}
            '''
            if isinstance(instr, Function): guardar_funcion(instr, ts)
            elif isinstance(instr, ExpresionInterface): guardar_interface(instr, ts)
           



if __name__ == '__main__':
    input_text = '''
                let a = (4+3)*(5+6);
                a = 23;
                /*
                addi t0, zero, 4
                addi t1, zero, 3
                add t2, t0, t1
                addi t3, zero, 5
                addi t4, zero, 6
                addi t5, t3, t4
                mul t6, t2, t5
                */

                console.log("Hola ");
                console.log("Esto es ");
                console.log("Una ");
                console.log("Prueba");
                console.log(a);
                '''
    

    instrucciones = g.parse(input_text)
    ts = TablaSimbolos()
    # try:
    #     procesar_instrucciones(instrucciones, ts, save=True)
    #     procesar_instrucciones(instrucciones, ts)
    # except Exception as e:
    #     print("Error", e)
    procesar_instrucciones(instrucciones, ts)

    print(f'''
    .data
          
    {ts.dato}

    .text
    .globl main
    main:

    {ts.salida}

    li a7, 10    
    ecall

    ''')