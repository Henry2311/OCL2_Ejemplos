import { parse } from "./calculadora.js";

const ast = (nodo) => {
    if(nodo.tipo === 'int') return nodo.valor
    if(nodo.tipo === 'boolean') return nodo.valor
    if(nodo.tipo === 'string') return nodo.valor
    if(nodo.tipo === 'parentesis') return ast(nodo.exp)
    if(nodo.tipo === 'print'){
        let exp_value = ast(nodo.exp)
        console.log(exp_value)
        return exp_value    
    }
        

    const left = (nodo.left && ast(nodo.left)) || 0
    const rigth = (nodo.rigth && ast(nodo.rigth)) || 0
    
    switch (nodo.tipo){
        case "+": return left + rigth
        case "-": return left - rigth
        case "*": return left * rigth
        case "/": {
            if(rigth===0){
                console.log("error")
                return 0
            }
            return left / rigth
        }
        case ">": return left > rigth
        case "<": return left < rigth
    }
}

document.getElementById("procesar").addEventListener("click", function(e) {
    let file = document.getElementById("entrada").value;
    const arbol = parse(file)
    console.log(arbol)
    //ocument.getElementById("salida").innerHTML = ast(arbol)
});