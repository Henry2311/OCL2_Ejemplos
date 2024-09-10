
{{
    import Aritmeticas from "../Expresiones/aritmeticas.js"
    import Relacional from  "../Expresiones/relacional.js"
    import Value from "../Expresiones/valor.js"
    import Identificador from "../Expresiones/identificador.js"
    import Print from "../Instrucciones/print.js"
    import Declaracion from "../Instrucciones/declaracion.js"
    import InstruccionIf from "../Instrucciones/instrIf.js" 
}}

S = Instrucciones

Instrucciones
    = head:Instruccion _ tail:Instrucciones _{
        return [head].concat(tail);
    }
    / inst:Instruccion {return [inst]}

Instruccion = Print
            / Declaracion /*
            if(10>1){
System.out.println("Verdadero");
}else{
System.out.println("Falso");
}*/
            / InstrIf

Print = "System.out.println"_"(" exp:Op_Aritmeticas ")"_ ";" {return new Print(exp)} 

Declaracion = "let"_ id:([a-zA-Z0-9_]+) _ "=" _ exp:Op_Aritmeticas _ ";" {return new Declaracion(id.join("") ,exp)} 

InstrIf = "if" _ "(" _ exp:Op_Aritmeticas _ ")"_"{" _ instrTrue:Instrucciones _ "}" _ instrFalse:elseBranch? {
    return new InstruccionIf(exp,instrTrue, instrFalse !== null ? instrFalse : null);
}
elseBranch
  = "else" _ "{" _ instrFalse:Instrucciones _ "}" {
      return instrFalse;
    }
Op_Aritmeticas = left:exp_aritmetica expansion:(
    op:(">" / "<") rigth:exp_aritmetica)* { 
    return expansion.reduce(
        (izquierda, [op, derecha]) => {
            return new Relacional(op, izquierda, derecha)
        }, left
    );
}

exp_aritmetica = left:exp expansion:(
    op:("+" / "-") rigth:exp)* { 
    return expansion.reduce(
        (izquierda, [op, derecha]) => {
            return new Aritmeticas(op, izquierda, derecha)
        }, left
    );
}

exp = left:exp_literal expansion:(
    op:("*"/"/") rigth:exp_literal)*{ 
    return expansion.reduce(
        (izquierda, [op, derecha]) => {
            return new Aritmeticas(op, izquierda, derecha)
        }, left
    );
}

exp_literal = "-" num:Numero {return new Aritmeticas("-", null, num)}
            / Numero
            / Boolean
            / LiteralId
            / StringLiteral

Numero = num:[0-9]+ {return new Value(parseInt(num.join(""),10))}    
        / "(" exp:Op_Aritmeticas ")" {return exp}

Boolean = bool:("True"/"False") {return new Value(bool==="True"?true:false)}

StringLiteral
  = "\"" chars:[^"]* "\"" {
      return new Value(chars.join(""))
    }

LiteralId = _ id:([a-zA-Z0-9_]+) _ {return new Identificador(id.join(""))}

_ "whitespace"
  = [ \t\n\r]*