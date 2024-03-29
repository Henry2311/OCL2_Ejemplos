
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDOrightUMENOSCADENA COMA COMMENTBLOCK CONSOLE DIVIDIDO DOSPUNTOS ELSE ENTERO FUNCTION ID IF IGUAL IGUALQUE LET LLAVDER LLAVIZQ LOG MAS MAYQUE MENOS MENQUE NIGUALQUE PARDER PARIZQ POR PUNTO PUNTOCOMA TIPONUMBERinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion      : imprimir_instr\n                        | declaracion_instr\n                        | asignacion_instr\n                        | if_instr\n                        | if_else_instr\n                        | funcion_instr\n                        | call_funcion_instr\n    imprimir_instr : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMAdeclaracion_instr : LET ID IGUAL expresion PUNTOCOMAasignacion_instr : ID IGUAL expresion PUNTOCOMAif_instr           : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAfuncion_instr      : FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMAcall_funcion_instr      : ID PARIZQ expresion COMA expresion PARDER PUNTOCOMAif_else_instr      : IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMAexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresionexpresion : expresion MAYQUE expresion\n                  | expresion MENQUE expresion\n                  | expresion IGUALQUE expresion\n                  | expresion NIGUALQUE expresionexpresion : MENOS expresion %prec UMENOSexpresion : PARIZQ expresion PARDERexpresion    : ENTEROexpresion    : CADENAexpresion    : ID'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,8,9,10,16,36,51,62,66,68,69,72,74,75,76,77,80,81,],[11,11,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-12,11,11,-11,-16,-14,11,11,11,11,-15,-17,]),'LET':([0,2,3,4,5,6,7,8,9,10,16,36,51,62,66,68,69,72,74,75,76,77,80,81,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-12,12,12,-11,-16,-14,12,12,12,12,-15,-17,]),'ID':([0,2,3,4,5,6,7,8,9,10,12,15,16,19,20,21,24,27,28,33,34,36,37,38,39,40,41,42,43,44,47,51,62,63,66,68,69,72,74,75,76,77,80,81,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,18,22,-2,25,25,25,25,25,25,49,25,-13,25,25,25,25,25,25,25,25,25,-12,13,67,13,-11,-16,-14,13,13,13,13,-15,-17,]),'IF':([0,2,3,4,5,6,7,8,9,10,16,36,51,62,66,68,69,72,74,75,76,77,80,81,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-12,14,14,-11,-16,-14,14,14,14,14,-15,-17,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,16,36,51,62,66,68,69,72,74,75,76,77,80,81,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-12,15,15,-11,-16,-14,15,15,15,15,-15,-17,]),'$end':([1,2,3,4,5,6,7,8,9,10,16,36,51,68,69,72,80,81,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-12,-11,-16,-14,-15,-17,]),'LLAVDER':([3,4,5,6,7,8,9,10,16,36,51,66,68,69,72,76,77,80,81,],[-3,-4,-5,-6,-7,-8,-9,-10,-2,-13,-12,70,-11,-16,-14,78,79,-15,-17,]),'PUNTO':([11,],[17,]),'IGUAL':([13,18,],[19,24,]),'PARIZQ':([13,14,19,20,21,22,23,24,27,28,34,37,38,39,40,41,42,43,44,47,],[20,21,28,28,28,33,34,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'LOG':([17,],[23,]),'MENOS':([19,20,21,24,25,26,27,28,29,30,31,32,34,35,37,38,39,40,41,42,43,44,45,46,47,50,52,53,54,55,56,57,58,59,60,61,],[27,27,27,27,-30,38,27,27,-28,-29,38,38,27,38,27,27,27,27,27,27,27,27,-26,38,27,38,-18,-19,-20,-21,38,38,38,38,-27,38,]),'ENTERO':([19,20,21,24,27,28,34,37,38,39,40,41,42,43,44,47,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'CADENA':([19,20,21,24,27,28,34,37,38,39,40,41,42,43,44,47,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'PUNTOCOMA':([25,26,29,30,35,45,52,53,54,55,56,57,58,59,60,64,65,70,78,79,],[-30,36,-28,-29,51,-26,-18,-19,-20,-21,-22,-23,-24,-25,-27,68,69,72,80,81,]),'MAS':([25,26,29,30,31,32,35,45,46,50,52,53,54,55,56,57,58,59,60,61,],[-30,37,-28,-29,37,37,37,-26,37,37,-18,-19,-20,-21,37,37,37,37,-27,37,]),'POR':([25,26,29,30,31,32,35,45,46,50,52,53,54,55,56,57,58,59,60,61,],[-30,39,-28,-29,39,39,39,-26,39,39,39,39,-20,-21,39,39,39,39,-27,39,]),'DIVIDIDO':([25,26,29,30,31,32,35,45,46,50,52,53,54,55,56,57,58,59,60,61,],[-30,40,-28,-29,40,40,40,-26,40,40,40,40,-20,-21,40,40,40,40,-27,40,]),'MAYQUE':([25,26,29,30,31,32,35,45,46,50,52,53,54,55,56,57,58,59,60,61,],[-30,41,-28,-29,41,41,41,-26,41,41,-18,-19,-20,-21,41,41,41,41,-27,41,]),'MENQUE':([25,26,29,30,31,32,35,45,46,50,52,53,54,55,56,57,58,59,60,61,],[-30,42,-28,-29,42,42,42,-26,42,42,-18,-19,-20,-21,42,42,42,42,-27,42,]),'IGUALQUE':([25,26,29,30,31,32,35,45,46,50,52,53,54,55,56,57,58,59,60,61,],[-30,43,-28,-29,43,43,43,-26,43,43,-18,-19,-20,-21,43,43,43,43,-27,43,]),'NIGUALQUE':([25,26,29,30,31,32,35,45,46,50,52,53,54,55,56,57,58,59,60,61,],[-30,44,-28,-29,44,44,44,-26,44,44,-18,-19,-20,-21,44,44,44,44,-27,44,]),'COMA':([25,29,30,31,45,49,52,53,54,55,56,57,58,59,60,],[-30,-28,-29,47,-26,63,-18,-19,-20,-21,-22,-23,-24,-25,-27,]),'PARDER':([25,29,30,32,45,46,50,52,53,54,55,56,57,58,59,60,61,67,],[-30,-28,-29,48,-26,60,64,-18,-19,-20,-21,-22,-23,-24,-25,-27,65,71,]),'LLAVIZQ':([48,71,73,],[62,74,75,]),'ELSE':([70,],[73,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,62,74,75,],[2,66,76,77,]),'instruccion':([0,2,62,66,74,75,76,77,],[3,16,3,16,3,3,16,16,]),'imprimir_instr':([0,2,62,66,74,75,76,77,],[4,4,4,4,4,4,4,4,]),'declaracion_instr':([0,2,62,66,74,75,76,77,],[5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,62,66,74,75,76,77,],[6,6,6,6,6,6,6,6,]),'if_instr':([0,2,62,66,74,75,76,77,],[7,7,7,7,7,7,7,7,]),'if_else_instr':([0,2,62,66,74,75,76,77,],[8,8,8,8,8,8,8,8,]),'funcion_instr':([0,2,62,66,74,75,76,77,],[9,9,9,9,9,9,9,9,]),'call_funcion_instr':([0,2,62,66,74,75,76,77,],[10,10,10,10,10,10,10,10,]),'expresion':([19,20,21,24,27,28,34,37,38,39,40,41,42,43,44,47,],[26,31,32,35,45,46,50,52,53,54,55,56,57,58,59,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',112),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',116),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',121),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',125),
  ('instruccion -> declaracion_instr','instruccion',1,'p_instruccion','gramatica.py',126),
  ('instruccion -> asignacion_instr','instruccion',1,'p_instruccion','gramatica.py',127),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','gramatica.py',128),
  ('instruccion -> if_else_instr','instruccion',1,'p_instruccion','gramatica.py',129),
  ('instruccion -> funcion_instr','instruccion',1,'p_instruccion','gramatica.py',130),
  ('instruccion -> call_funcion_instr','instruccion',1,'p_instruccion','gramatica.py',131),
  ('imprimir_instr -> CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA','imprimir_instr',7,'p_instruccion_console','gramatica.py',136),
  ('declaracion_instr -> LET ID IGUAL expresion PUNTOCOMA','declaracion_instr',5,'p_instruccion_declaracion','gramatica.py',140),
  ('asignacion_instr -> ID IGUAL expresion PUNTOCOMA','asignacion_instr',4,'p_instruccion_asignacion','gramatica.py',144),
  ('if_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','if_instr',8,'p_if_instr','gramatica.py',148),
  ('funcion_instr -> FUNCTION ID PARIZQ ID COMA ID PARDER LLAVIZQ instrucciones LLAVDER PUNTOCOMA','funcion_instr',11,'p_funcion_instr','gramatica.py',152),
  ('call_funcion_instr -> ID PARIZQ expresion COMA expresion PARDER PUNTOCOMA','call_funcion_instr',7,'p_call_funcion_instr','gramatica.py',157),
  ('if_else_instr -> IF PARIZQ expresion PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER PUNTOCOMA','if_else_instr',12,'p_if_else_instr','gramatica.py',161),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',165),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',166),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',167),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','gramatica.py',168),
  ('expresion -> expresion MAYQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',175),
  ('expresion -> expresion MENQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',176),
  ('expresion -> expresion IGUALQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',177),
  ('expresion -> expresion NIGUALQUE expresion','expresion',3,'p_expresion_logica','gramatica.py',178),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','gramatica.py',185),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','gramatica.py',189),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','gramatica.py',193),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',197),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',201),
]
