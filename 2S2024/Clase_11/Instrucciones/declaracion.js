import Instrucciones from "../Interfaces/instrucciones.js"
import Symbol from "../Env/symbol.js"

export default class Declaracion extends Instrucciones {

    constructor(id,expresiones){
        super();
        this.id = id
        this.expresiones = expresiones
    }

    run(env){
        let valor = this.expresiones.run(env)
        let symbol = new Symbol('int', valor)
        env.setSymbol(this.id, symbol)
    }

    save(env){
        console.log("SAVE DECLARACION")
    }

    risc(env){
        let exp = this.expresiones.risc(env)

        env.dato += `${this.id}: .word 0`

        let lastTemp = env.lastTemp() //t0
        let temporal = env.generateTemp() //t1

        env.risc += `la t${temporal}, ${this.id}\n`
        env.risc += `sw t${lastTemp}, 0(t${env.lastTemp()})\n`

    }
}