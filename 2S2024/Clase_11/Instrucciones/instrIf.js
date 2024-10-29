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

    risc(env){
        let exp = this.condicion.risc(env) //Etiqueta del True
        let else_ = `L${env.generateLabel()}`
        let exit_ = `L${env.generateLabel()}`


        env.risc += `${exp}:\n`
        let new_env = new Env(env)
        this.instrVerdaderas.forEach(instruccion => {
            instruccion.risc(new_env)
        });
        env.risc += new_env.risc
        env.dato += new_env.dato
        env.msg = new_env.msg
        env.temporal = new_env.temporal
        env.label = new_env.label
        env.risc += `j ${exit_}\n`


        console.log(env.msg)
        env.risc += `${else_}:\n`
        let new_env_false = new Env(env)
        new_env_false.msg = env.msg
        new_env_false.temporal = env.temporal
        new_env_false.label = env.label
        this.instrFalsas?.forEach(instruccion => {
            instruccion.risc(new_env_false)
        });
        env.risc += new_env_false.risc
        env.dato += new_env_false.dato
        env.msg = new_env_false.msg
        env.temporal = new_env_false.temporal
        env.label = new_env_false.label
        env.risc += `${exit_}:\n`
        /**
         * L1: 
         *   Instrucciones Verdaderas
         *   j L3
         * L2:
         *   Instrucciones Falsas
         * L3:
         */

    }
}