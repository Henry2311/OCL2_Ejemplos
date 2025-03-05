grammar Language;

program: dcl*;

dcl: 'print(' expr ')' ';' # PrintStmt
    | 'if (' expr ')' block ('else' block)? # IfStmt
	| 'for (' expr ')' block # WhileStmt
    | 'func' ID '(' parametros? ')' ':' type block # FuncDeclStmt
    | 'return' expr ';'   # ReturnStmt
    | varCall ';'  #FuncCallStmt
	| varAsign # AsignStmt
	| varDcl #VarDeclStmt;

block: '{' dcl* '}';

varDcl: 'var' ID ':' type '=' expr ';';

varAsign: ID '=' expr ';' ;

varCall: ID '(' args? ')';

parametros: param (',' param)* ;
param: ID ':' type ;

args: expr (',' expr)* ;

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
    | '(' expr ')'            # Parens;

type: 'Integer' | 'Double' | 'String' | 'Boolean' | 'Void';

INT: [0-9]+;
DOUBLE: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;
ID: [a-zA-Z_]+;
