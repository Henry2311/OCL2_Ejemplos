{   
    import { Aritmeticas } from "./Expresiones/aritmeticas.js";
    let lista_ast = [] 

}



S = Instrucciones

Instrucciones = Instruccion Instrucciones
            / Instruccion

Instruccion = Op_Aritmeticas
            / Print

Print = "System.out.println"_"(" exp:Op_Aritmeticas ")"_ ";" {return {tipo:'print', exp}} 

Op_Aritmeticas = left:exp_aritmetica expansion:(
    op:(">" / "<") rigth:exp_aritmetica {return {tipo: op, rigth}}
)* { 
    return expansion.reduce(
        (before, current) => {
            const {tipo, rigth} = current
            return {tipo, left:before, rigth} 
        }, left
    );
}

exp_aritmetica = left:exp expansion:(
    op:("+" / "-") rigth:exp {return {tipo: op, rigth}}
)* { 
    return expansion.reduce(
        (before, current) => {
            const {tipo, rigth} = current
            return new Aritmeticas(tipo, before, rigth)
        }, left
    );
}

exp = left:exp_literal expansion:(
    op:("*"/"/") rigth:exp_literal {return {tipo: op, rigth}}
)*{ 
    return expansion.reduce(
        (before, current) => {
            const {tipo, rigth} = current
            return new Aritmeticas(tipo, before, rigth)
        }, left
    );
}

exp_literal = "-" num:Numero {return {tipo: "-", rigth: num } }
            / Numero
            / Boolean
            / StringLiteral

Numero = num:[0-9]+ {return {tipo: 'int', valor: parseInt(num.join(""),10)}}    
        / "(" exp:Op_Aritmeticas ")" {return {tipo: 'parentesis', exp}}

Boolean = bool:("True"/"False") {return {tipo: 'boolean', valor: bool==="True"?true:false}}

StringLiteral
  = "\"" chars:[^"]* "\"" {
      return {tipo:'string', valor:chars.join("")}
    }

_ "whitespace"
  = [ \t\n\r]*
