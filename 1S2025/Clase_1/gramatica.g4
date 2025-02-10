grammar gramatica;

options { caseInsensitive = true; }

NEWLINE : [ \r\n\t]+ -> channel(HIDDEN);

prog: expr EOF ;
expr: expr ('*'|'/') expr
    | expr ('+'|'-') expr
    | INT
    | '(' expr ')'
    ;

INT: [0-9]+;
