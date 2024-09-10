import Instrucciones from "../Interfaces/instrucciones.js"
import Env from "../Env/env.js";

export default class InstruccionIf extends Instrucciones {

    constructor(condicion, instruciones_true, instruciones_false){
        super();
        this.condicion = condicion
        this.instruciones_true = instruciones_true
        this.instruciones_false = instruciones_false
    }

    run(env){
        let condicion = this.condicion.run(env)
        if(condicion){
            let new_env = new Env(env)
            this.instruciones_true.forEach(instruccion => {
                instruccion.run(new_env)
            });
            env.addConsole(new_env.console)
        }else{
            let new_env = new Env(env)
            this.instruciones_false.forEach(instruccion => {
                instruccion.run(new_env)
            });
            env.addConsole(new_env.console)
        }
    }
}