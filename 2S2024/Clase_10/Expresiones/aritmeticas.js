import Expresion from "../Interfaces/expresiones.js"
export default class Aritmeticas extends Expresion {

    constructor(op, izquierda, derecha){
        super();
        this.op = op
        this.izquierda = izquierda
        this.derecha = derecha
    }

    run(env){

        let left = this.izquierda?.run(env)
        let rigth = this.derecha?.run(env)

        switch(this.op){
            case "+": return left + rigth
            case "-": {
                if(!left){
                    return -rigth
                }    
                return left - rigth
            }
            case "*": return left * rigth
            case "/": {
                if(rigth===0){
                    console.log("error")
                    return 0
                }
                return left / rigth
            }
        }
    }

    risc(env){
        let left = this.izquierda?.risc(env)
        let rigth = this.derecha?.risc(env)

        switch(this.op){
            case "+": {
                let temporal = env.generateTemp()
                env.risc += `add t${temporal}, ${left.valor}, ${rigth.valor}\n`

                return {'valor':`t${temporal}`, 'tipo':'number'}
            }
            case "-": {
                let temporal = env.generateTemp()
                env.risc += `sub t${temporal}, ${left.valor}, ${rigth.valor}\n`

                return {'valor':`t${temporal}`, 'tipo':'number'}
            }
            case "*": {
                let temporal = env.generateTemp()
                env.risc += `mul t${temporal}, ${left.valor}, ${rigth.valor}\n`

                return {'valor':`t${temporal}`, 'tipo':'number'}
            }
            case "/": {
                let temporal = env.generateTemp()
                env.risc += `siv t${temporal}, ${left.valor}, ${rigth.valor}\n`

                return {'valor':`t${temporal}`, 'tipo':'number'}
            }
        }
    }
}