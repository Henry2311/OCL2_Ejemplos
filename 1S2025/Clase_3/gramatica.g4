grammar gramatica;

options { caseInsensitive = true; }

NEWLINE : [ \r\n\t]+ -> channel(HIDDEN);

start: instrucciones EOF ;

instrucciones: instruccion (instrucciones)* ;

instruccion: print;

print: 'fmt.println' '(' expr ')';

expr: expr ('*'|'/') expr   # MulDiv
    | expr ('+'|'-') expr   # AddSub
    | INT                   # Number
    | DECIMAL               # Decimal
    | CADENA                # Cadena
    | '(' expr ')'          # Parens
    ;

INT: [0-9]+;
DECIMAL: [0-9]+'.'[0-9]+;
CADENA : ('"'|'\'') (~["\r\n] | '""')* ('"'|'\'') ;