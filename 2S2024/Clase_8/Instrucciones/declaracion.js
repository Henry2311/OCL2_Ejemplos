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
}