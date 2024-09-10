import Instrucciones from "../Interfaces/instrucciones.js"

export default class Print extends Instrucciones {

    constructor(expresiones){
        super();
        this.expresiones = expresiones
    }

    run(env){
        env.addConsole(this.expresiones.run(env))
    }
}