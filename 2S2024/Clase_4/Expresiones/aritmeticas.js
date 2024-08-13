export class Aritmeticas extends Expresion {

    constructor(op, izquierda, derecha){
        this.op = op
        this.izquierda = izquierda
        this.derecha = derecha
    }

    run(ast, env, gen){
        console.log(env)
    }
}