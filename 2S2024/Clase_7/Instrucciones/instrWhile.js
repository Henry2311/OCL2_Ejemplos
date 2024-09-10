import Instrucciones from "../Interfaces/instrucciones.js"
import Env from "../Env/env.js";

export default class InstrWhile extends Instrucciones {

    constructor(condicion, instrVerdaderas){
        super();
        this.condicion = condicion
        this.instrVerdaderas = instrVerdaderas
    }

    run(env){
        let condicion = this.condicion.run(env)
        while(condicion){
            let new_env = new Env(env)
            this.instrVerdaderas.forEach(instruccion => {
                instruccion.run(new_env)
            });
            condicion = this.condicion.run(env)
        }
    }
}