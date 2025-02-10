grammar gramatica;

options { caseInsensitive = true; }

NEWLINE : [ \r\n\t]+ -> channel(HIDDEN);

start: expr EOF ;
expr: expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | INT
    | DECIMAL
    | CADENA
    | '(' expr ')'
    ;

INT: [0-9]+;
DECIMAL: [0-9]+'.'[0-9]+;
CADENA : ('"'|'\'') (~["\r\n] | '""')* ('"'|'\'') ;