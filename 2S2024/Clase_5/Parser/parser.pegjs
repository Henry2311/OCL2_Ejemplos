
{{
    import Aritmeticas from "../Expresiones/aritmeticas.js"
    import Relacional from  "../Expresiones/relacional.js"
    import Value from "../Expresiones/valor.js"
    import Identificador from "../Expresiones/identificador.js"
    import Print from "../Instrucciones/print.js"
    import Declaracion from "../Instrucciones/declaracion.js"

}}

S = Instrucciones

Instrucciones = Instruccion Instrucciones
            / Instruccion

Instruccion = Print
            / Declaracion

Print = "System.out.println"_"(" exp:Op_Aritmeticas ")"_ ";" {return new Print(exp)} 

Declaracion = "let"_ id:([a-zA-Z0-9_]+) _ "=" _ exp:Op_Aritmeticas _ ";" {return new Declaracion(id.join("") ,exp)} 

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
