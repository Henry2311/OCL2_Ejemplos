import { parse } from "./Parser/calculadora.js"
import Env from "./Env/env.js";
import Symbol from "./Env/symbol.js";

document.getElementById("procesar").addEventListener("click", function(e) {
    let file = document.getElementById("entrada").value;
    const arbol = parse(file)
    console.log(arbol)
    let env = new Env(null)
    let symbol = new Symbol('int', 10)
    env.setSymbol("var1",symbol)
    arbol.run(env)
    console.log(env.tabla)
    document.getElementById("salida").innerHTML = env.console
});