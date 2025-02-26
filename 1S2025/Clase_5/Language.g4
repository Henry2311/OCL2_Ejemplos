grammar Language;

program: dcl*;

dcl: expr ';' # ExprStmt 
    | 'print(' expr ')' ';' # PrintStmt
    | 'if (' expr ')' block ('else' block)? # IfStmt
	| 'for (' expr ')' block # WhileStmt
	| varAsign # AsignStmt
	| varDcl #VarDeclStmt;

block: '{' dcl* '}';

varDcl: 'var' ID ':' type '=' expr ';';

varAsign: ID '=' expr ';' ;

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
    | '(' expr ')'            # Parens;

type: 'Integer' | 'Double' | 'String' | 'Boolean';

INT: [0-9]+;
DOUBLE: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;
ID: [a-zA-Z_]+;
