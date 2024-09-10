import { parse, SyntaxError } from "./Parser/calculadora.js"
import Env from "./Env/env.js";

document.getElementById("procesar").addEventListener("click", function(e) {
    let file = document.getElementById("entrada").value;
    let error = []
    try {
        const arbol = parse(file)
        let env = new Env(null)
        arbol.forEach(instruccion => {
            instruccion.save(env) //Guardaria mis funciones
        });

        console.log(env.tabla)

        arbol.forEach(instruccion => {
            instruccion.run(env)
        });
        error.concat(env.errores)
        console.log(env.tabla)
        document.getElementById("salida").innerHTML = env.console
    } catch (e) {
        if(e instanceof SyntaxError){
            if (isLexicalError(e)){
                error.push('Error Léxico: '+e.message)
            }else{
                error.push('Error Sintáctico: '+e.message)
            }
        }else{
            error.push('Error Sintáctico: '+e.message)
        }
    }

    console.log(error)
});

function isLexicalError(e) {
    const validIdentifier = /^[a-zA-Z_$][a-zA-Z0-9_$]*$/;
    const validInteger = /^[0-9]+$/;
    const validRegister = /^[a-zA-Z][0-9]+$/;
    const validCharacter = /^[a-zA-Z0-9_$,\[\]#"]$/;
    if (e.found) {
      if (!validIdentifier.test(e.found) && 
          !validInteger.test(e.found) &&
          !validRegister.test(e.found) &&
          !validCharacter.test(e.found)) {
        return true; // Error léxico
      }
    }
    return false; // Error sintáctico
}
