import { parse, SyntaxError } from "./Parser/calculadora.js"
import Env from "./Env/env.js";

document.getElementById("procesar").addEventListener("click", function(e) {
    let file = document.getElementById("entrada").value;
    try {
        const arbol = parse(file)
        console.log(arbol)
        let env = new Env(null)

        arbol.forEach(instrccion => {   
            instrccion.run(env)
        });

        console.log(env.tabla)
        document.getElementById("salida").innerHTML = env.console
    } catch (e) {
        if (e instanceof SyntaxError) {
            if (isLexicalError(e)) {
                console.error('Error Léxico: ' + e.message);
            } else {
                console.error('Error Sintáctico: ' + e.message);
            }
        } else {
            console.error('Error desconocido:', e);
        }
    }
    
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
