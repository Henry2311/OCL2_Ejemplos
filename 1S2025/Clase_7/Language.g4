grammar Language;

program: dcl*;

dcl: 'print(' expr ')' ';' # PrintStmt
    | 'if (' expr ')' block ('else' block)? # IfStmt
	| 'for (' expr ')' block # WhileStmt
    | 'func' ID '(' parametros? ')' ':' type block # FuncDeclStmt
    | 'return' expr ';'   # ReturnStmt
    | varCall ';'  #FuncCallStmt
	| varAsign # AsignStmt
	| varDcl #VarDeclStmt
    | arrayDcl #ArryDclStmt
    | sliceDcl #SliceDclStmt
    | appendSlice #AppendSliceStmt
    | structDcl    #StructDclStmt
    ;

block: '{' dcl* '}';

varDcl: 'var' ID ':' type '=' expr ';';

varAsign: ID '=' expr ';' ;

varCall: ID '(' args? ')';

parametros: param (',' param)* ;
param: ID ':' type ;

args: expr (',' expr)* ;

sliceDcl: 'var' ID '['']' type ';' ;
appendSlice: ID '.append(' expr ')' ';' 

arrayDcl: ID '=' '[' ']' type '{' list_values '}' ';' ;

list_values : expr (',' expr)* ;

structDcl: 'struct' ID '{' atributos '}' ';' ;

atributos: atrib (',' atrib)* ;
atrib: ID ':' type;

struct Persona {
    nombre:String,
    edad:Integer
}

struct Nodo {
    valor: Integer,
    siguiente: Nodo
}

struct List {
    nodos: Nodo
}

Lisa.nodos.siguiente

expr:
    '-' expr                  # Negate
    | expr op = ('*' | '/') expr    # MulDiv
    | expr op = ('+' | '-') expr    # AddSub
    | expr op = ('<' | '>') expr    # Compare
    | expr op = ('&&' | '||') expr  # Logical
    | '!' expr                # Not
    | INT                     # Integer
    | DOUBLE                  # Double
    | STRING                  # String
    | BOOL                    # Boolean
    | ID                      # Identifier
    | varCall                 # FuncCallExpr
    | arrAccess               # ArrayAccessExpr
    | '(' expr ')'            # Parens;

type: 'Integer' | 'Double' | 'String' | 'Boolean' | 'Void';

arrAccess: ID '[' expr ']' ;

INT: [0-9]+;
DOUBLE: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;
ID: [a-zA-Z_]+;


