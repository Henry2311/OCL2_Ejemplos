
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDOrightUMENOSAND BREAK CADENA COMA COMMENTBLOCK CONSOLE DIVIDIDO DOSPUNTOS ELSE ENTERO FUNCTION ID IF IGUAL IGUALQUE INTERFACE LET LLAVDER LLAVIZQ LOG MAS MAYQUE MENORIGUAL MENOS MENQUE NIGUALQUE NUMBER OR PARDER PARIZQ POR PUNTO PUNTOCOMA RETURN STRING TIPONUMBER WHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion      : imprimir_instr\n                        | declaracion_instr\n                        | asignacion_instr\n                        | if_instr\n                        | if_else_instr\n                        | while_instr\n                        | funcion_instr\n                        | call_funcion_instr\n                        | interface_instr\n                        | return_instr\n                        | break_instr\n    break_instr     : BREAK PUNTOCOMAreturn_instr     : RETURN expresion PUNTOCOMA\n                        | RETURN PUNTOCOMAinterface_instr : INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDERinterface_params : interface_params PUNTOCOMA ID DOSPUNTOS expresion\n                        | ID DOSPUNTOS expresionimprimir_instr : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMAdeclaracion_instr : LET ID IGUAL expresion PUNTOCOMAasignacion_instr : ID IGUAL expresion PUNTOCOMAif_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAfuncion_instr      : FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAcall_funcion_instr      : ID PARIZQ expresion COMA expresion PARDER PUNTOCOMAif_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMAwhile_instr      : WHILE PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresionexpresion :  expresion AND expresion\n                  | expresion OR expresion\n                  | expresion MAYQUE expresion\n                  | expresion MENQUE expresion\n                  | expresion IGUALQUE expresion\n                  | expresion NIGUALQUE expresion\n                  | expresion MENORIGUAL expresionexpresion : MENOS expresion %prec UMENOSexpresion : PARIZQ expresion PARDERexpresion    : ENTEROexpresion    : CADENAexpresion    : ID\n                    | ID PUNTO ID\n                    | ID PARIZQ expresion COMA expresion PARDER'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,15,15,15,15,-18,-21,-26,-24,-28,15,15,15,15,-25,-27,]),'LET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,16,16,16,16,-18,-21,-26,-24,-28,16,16,16,16,-25,-27,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,20,21,22,24,27,28,29,30,34,35,36,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,65,67,68,89,91,92,93,94,95,96,99,100,104,106,107,111,113,115,116,118,119,120,123,124,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,26,31,32,39,-2,39,39,39,39,-17,39,39,-15,39,71,72,-16,39,39,39,39,39,39,39,39,39,39,39,86,39,39,-23,39,-22,17,17,101,39,103,39,17,17,-18,-21,-26,39,-24,-28,17,17,17,17,-25,-27,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,18,18,18,18,-18,-21,-26,-24,-28,18,18,18,18,-25,-27,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,19,19,19,19,-18,-21,-26,-24,-28,19,19,19,19,-25,-27,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,20,20,20,20,-18,-21,-26,-24,-28,20,20,20,20,-25,-27,]),'INTERFACE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,21,21,21,21,-18,-21,-26,-24,-28,21,21,21,21,-25,-27,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,22,22,22,22,-18,-21,-26,-24,-28,22,22,22,22,-25,-27,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,91,92,99,100,104,106,107,113,115,116,118,119,120,123,124,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,23,23,23,23,-18,-21,-26,-24,-28,23,23,23,23,-25,-27,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,104,106,107,113,115,123,124,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,-18,-21,-26,-24,-28,-25,-27,]),'LLAVDER':([3,4,5,6,7,8,9,10,11,12,13,14,24,34,40,49,67,89,95,99,100,104,106,107,113,115,119,120,123,124,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-2,-17,-15,-16,-23,-22,104,108,109,-18,-21,-26,-24,-28,121,122,-25,-27,]),'PUNTO':([15,39,],[25,63,]),'IGUAL':([17,26,],[27,42,]),'PARIZQ':([17,18,19,22,27,28,29,30,31,35,36,39,41,42,50,51,52,53,54,55,56,57,58,59,60,64,65,68,94,96,111,],[28,29,30,36,36,36,36,36,47,36,36,64,65,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'PUNTOCOMA':([22,23,33,37,38,39,43,61,66,73,74,75,76,77,78,79,80,81,82,83,84,85,86,97,98,102,108,109,112,117,121,122,],[34,40,49,-42,-43,-44,67,-40,89,95,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-41,-45,106,107,-20,113,115,-46,-19,123,124,]),'MENOS':([22,27,28,29,30,33,35,36,37,38,39,42,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,66,68,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,94,96,102,105,111,112,117,],[35,35,35,35,35,51,35,35,-42,-43,-44,35,51,51,51,51,35,35,35,35,35,35,35,35,35,35,35,-40,51,35,35,51,35,-29,-30,-31,-32,51,51,51,51,51,51,51,-41,-45,51,51,51,35,35,51,51,35,-46,51,]),'ENTERO':([22,27,28,29,30,35,36,42,50,51,52,53,54,55,56,57,58,59,60,64,65,68,94,96,111,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'CADENA':([22,27,28,29,30,35,36,42,50,51,52,53,54,55,56,57,58,59,60,64,65,68,94,96,111,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'LOG':([25,],[41,]),'LLAVIZQ':([32,69,70,110,114,],[48,91,92,116,118,]),'MAS':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[50,-42,-43,-44,50,50,50,50,-40,50,50,-29,-30,-31,-32,50,50,50,50,50,50,50,-41,-45,50,50,50,50,50,-46,50,]),'POR':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[52,-42,-43,-44,52,52,52,52,-40,52,52,52,52,-31,-32,52,52,52,52,52,52,52,-41,-45,52,52,52,52,52,-46,52,]),'DIVIDIDO':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[53,-42,-43,-44,53,53,53,53,-40,53,53,53,53,-31,-32,53,53,53,53,53,53,53,-41,-45,53,53,53,53,53,-46,53,]),'AND':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[54,-42,-43,-44,54,54,54,54,-40,54,54,-29,-30,-31,-32,54,54,54,54,54,54,54,-41,-45,54,54,54,54,54,-46,54,]),'OR':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[55,-42,-43,-44,55,55,55,55,-40,55,55,-29,-30,-31,-32,55,55,55,55,55,55,55,-41,-45,55,55,55,55,55,-46,55,]),'MAYQUE':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[56,-42,-43,-44,56,56,56,56,-40,56,56,-29,-30,-31,-32,56,56,56,56,56,56,56,-41,-45,56,56,56,56,56,-46,56,]),'MENQUE':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[57,-42,-43,-44,57,57,57,57,-40,57,57,-29,-30,-31,-32,57,57,57,57,57,57,57,-41,-45,57,57,57,57,57,-46,57,]),'IGUALQUE':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[58,-42,-43,-44,58,58,58,58,-40,58,58,-29,-30,-31,-32,58,58,58,58,58,58,58,-41,-45,58,58,58,58,58,-46,58,]),'NIGUALQUE':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[59,-42,-43,-44,59,59,59,59,-40,59,59,-29,-30,-31,-32,59,59,59,59,59,59,59,-41,-45,59,59,59,59,59,-46,59,]),'MENORIGUAL':([33,37,38,39,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,102,105,112,117,],[60,-42,-43,-44,60,60,60,60,-40,60,60,-29,-30,-31,-32,60,60,60,60,60,60,60,-41,-45,60,60,60,60,60,-46,60,]),'COMA':([37,38,39,44,61,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,112,],[-42,-43,-44,68,-40,93,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-41,-45,96,-46,]),'PARDER':([37,38,39,45,46,61,62,74,75,76,77,78,79,80,81,82,83,84,85,86,88,90,101,105,112,],[-42,-43,-44,69,70,-40,85,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-41,-45,97,98,110,112,-46,]),'DOSPUNTOS':([72,103,],[94,111,]),'ELSE':([108,],[114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,91,92,116,118,],[2,99,100,119,120,]),'instruccion':([0,2,91,92,99,100,116,118,119,120,],[3,24,3,3,24,24,3,3,24,24,]),'imprimir_instr':([0,2,91,92,99,100,116,118,119,120,],[4,4,4,4,4,4,4,4,4,4,]),'declaracion_instr':([0,2,91,92,99,100,116,118,119,120,],[5,5,5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,91,92,99,100,116,118,119,120,],[6,6,6,6,6,6,6,6,6,6,]),'if_instr':([0,2,91,92,99,100,116,118,119,120,],[7,7,7,7,7,7,7,7,7,7,]),'if_else_instr':([0,2,91,92,99,100,116,118,119,120,],[8,8,8,8,8,8,8,8,8,8,]),'while_instr':([0,2,91,92,99,100,116,118,119,120,],[9,9,9,9,9,9,9,9,9,9,]),'funcion_instr':([0,2,91,92,99,100,116,118,119,120,],[10,10,10,10,10,10,10,10,10,10,]),'call_funcion_instr':([0,2,91,92,99,100,116,118,119,120,],[11,11,11,11,11,11,11,11,11,11,]),'interface_instr':([0,2,91,92,99,100,116,118,119,120,],[12,12,12,12,12,12,12,12,12,12,]),'return_instr':([0,2,91,92,99,100,116,118,119,120,],[13,13,13,13,13,13,13,13,13,13,]),'break_instr':([0,2,91,92,99,100,116,118,119,120,],[14,14,14,14,14,14,14,14,14,14,]),'expresion':([22,27,28,29,30,35,36,42,50,51,52,53,54,55,56,57,58,59,60,64,65,68,94,96,111,],[33,43,44,45,46,61,62,66,74,75,76,77,78,79,80,81,82,83,84,87,88,90,102,105,117,]),'interface_params':([48,],[73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',125),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',129),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',134),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',138),
  ('instruccion -> declaracion_instr','instruccion',1,'p_instruccion','gramatica.py',139),
  ('instruccion -> asignacion_instr','instruccion',1,'p_instruccion','gramatica.py',140),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','gramatica.py',141),
  ('instruccion -> if_else_instr','instruccion',1,'p_instruccion','gramatica.py',142),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','gramatica.py',143),
  ('instruccion -> funcion_instr','instruccion',1,'p_instruccion','gramatica.py',144),
  ('instruccion -> call_funcion_instr','instruccion',1,'p_instruccion','gramatica.py',145),
  ('instruccion -> interface_instr','instruccion',1,'p_instruccion','gramatica.py',146),
  ('instruccion -> return_instr','instruccion',1,'p_instruccion','gramatica.py',147),
  ('instruccion -> break_instr','instruccion',1,'p_instruccion','gramatica.py',148),
  ('break_instr -> BREAK PUNTOCOMA','break_instr',2,'p_instruccion_break','gramatica.py',153),
  ('return_instr -> RETURN expresion PUNTOCOMA','return_instr',3,'p_instruccion_retorno','gramatica.py',157),
  ('return_instr -> RETURN PUNTOCOMA','return_instr',2,'p_instruccion_retorno','gramatica.py',158),
  ('interface_instr -> INTERFACE ID LLAVIZQ interface_params PUNTOCOMA LLAVDER','interface_instr',6,'p_instruccion_interface','gramatica.py',165),
  ('interface_params -> interface_params PUNTOCOMA ID DOSPUNTOS expresion','interface_params',5,'p_instruccion_interface_params','gramatica.py',169),
  ('interface_params -> ID DOSPUNTOS expresion','interface_params',3,'p_instruccion_interface_params','gramatica.py',170),
  ('imprimir_instr -> CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA','imprimir_instr',7,'p_instruccion_console','gramatica.py',188),
  ('declaracion_instr -> LET ID IGUAL expresion PUNTOCOMA','declaracion_instr',5,'p_instruccion_declaracion','gramatica.py',192),
  ('asignacion_instr -> ID IGUAL expresion PUNTOCOMA','asignacion_instr',4,'p_instruccion_asignacion','gramatica.py',196),
  ('if_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','if_instr',8,'p_if_instr','gramatica.py',200),
  ('funcion_instr -> FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','funcion_instr',11,'p_funcion_instr','gramatica.py',204),
  ('call_funcion_instr -> ID PARIZQ expresion COMA expresion PARDER PUNTOCOMA','call_funcion_instr',7,'p_call_funcion_instr','gramatica.py',209),
  ('if_else_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMA','if_else_instr',12,'p_if_else_instr','gramatica.py',214),
  ('while_instr -> WHILE PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','while_instr',8,'p_while_instr','gramatica.py',218),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',222),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',223),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',224),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','gramatica.py',225),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_logica','gramatica.py',232),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_logica','gramatica.py',233),
  ('expresion -> expresion MAYQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',234),
  ('expresion -> expresion MENQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',235),
  ('expresion -> expresion IGUALQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',236),
  ('expresion -> expresion NIGUALQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',237),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logica','gramatica.py',238),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','gramatica.py',248),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',252),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','gramatica.py',256),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',260),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',264),
  ('expresion -> ID PUNTO ID','expresion',3,'p_expresion_id','gramatica.py',265),
  ('expresion -> ID PARIZQ expresion COMA expresion PARDER','expresion',6,'p_expresion_id','gramatica.py',266),
]
