import Expresion from "../Interfaces/expresiones.js"

export default class Relacional extends Expresion {

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
            case ">": return left > rigth
            case "<": return left < rigth
            case "==": return left == rigth
            case "!=": return left != rigth
            case ">=":return left >= rigth
            case "<=": return left <= rigth
        }
    }

    risc(env){
        let left = this.izquierda?.risc(env)
        let rigth = this.derecha?.risc(env)
        switch(this.op){
            case ">": {
                let etiqueta = `L${env.generateLabel()}`
                
                env.risc += `bgt ${left.valor}, ${rigth.valor}, ${etiqueta}\n`

                return etiqueta
            }
            case "<": {
                let etiqueta = `L${env.generateLabel()}`
                
                env.risc += `blt ${left.valor}, ${rigth.valor}, ${etiqueta}\n`

                return etiqueta
            }
        }
    }
}