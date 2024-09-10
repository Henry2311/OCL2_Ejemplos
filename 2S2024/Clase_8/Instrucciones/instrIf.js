import Instrucciones from "../Interfaces/instrucciones.js"
import Env from "../Env/env.js";

export default class InstrIf extends Instrucciones {

    constructor(condicion, instrVerdaderas, instrFalsas){
        super();
        this.condicion = condicion
        this.instrVerdaderas = instrVerdaderas
        this.instrFalsas = instrFalsas
    }

    run(env){
        let condicion = this.condicion.run(env)

        if(condicion){
            let new_env = new Env(env)
            this.instrVerdaderas.forEach(instruccion => {
                instruccion.run(new_env)
            });
            env.addConsole(new_env.console)
        }else{
            let new_env = new Env(env)
            this.instrFalsas?.forEach(instruccion => {
                instruccion.run(new_env)
            });
            env.addConsole(new_env.console)
        }
    }

    save(env){
        console.log("SAVE DECLARACION")
    }
}