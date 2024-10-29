import Instrucciones from "../Interfaces/instrucciones.js"
import Env from "../Env/env.js";
import Symbol from "../Env/symbol.js";

export default class instrFunction extends Instrucciones {

    constructor(id, parametros, instrucciones){
        super();
        this.id = id
        this.parametros = parametros
        this.instrucciones = instrucciones
    }

    run(env){
        if(!this.instrucciones){
            let symbol = env.getSymbol(this.id)
            let new_env = new Env(env)

            if(this.parametros && this.parametros?.length == symbol.valor.params?.length){
                for (let index = 0; index < this.parametros.length; index++) {
                    let value = this.parametros[index].run(env);
                    let new_param = new Symbol('int', value)
                    new_env.setSymbol(symbol.valor.params[index], new_param)
                }
            }
            
            console.log("NEW ENV", new_env.tabla)

            symbol.valor.instr.forEach(instruccion => {
                instruccion.run(new_env)
            });
            env.addConsole(new_env.console)
        }
    }
    
    save(env){
        if(this.instrucciones){
            console.log(this.parametros)
            let symbol = new Symbol('void',{
                instr: this.instrucciones,
                params: this.parametros
            })
            env.setSymbol(this.id, symbol)
        }
    }

    risc(env){
        if(this.instrucciones){
            

            env.functions += `${this.id}:\n`        //hola_mundo:
            
            let symbol = env.getSymbol(this.id)

            if(this.parametros && this.parametros?.length == symbol.valor.params?.length){
            //      let contador_params = 1; //a1, a2, a3, a4
            //      for (let index = 0; index < this.parametros.length; index++) {
            //          let value = this.parametros[index].run(env);
            //          env.risc += `li a${contador_params} ${value}:\n` //li a1, 10
            //          contador_params +=1;
            //      }
                env.use_params = true;
            }

            let new_env = new Env(env)              // Instrucciones
            new_env.use_params = env.use_params
            this.instrucciones.forEach(instruccion => {
                instruccion.risc(new_env)
            });
            env.functions += new_env.risc
            env.functions += `ret\n`                // ret
            env.use_params = false;
            env.dato += new_env.dato
            env.msg = new_env.msg
        }else{
            let symbol = env.getSymbol(this.id)

            if(this.parametros && this.parametros?.length == symbol.valor.params?.length){
                let contador_params = 1; //a1, a2, a3, a4
                for (let index = 0; index < this.parametros.length; index++) {
                    let value = this.parametros[index].run(env);
                    env.risc += `li a${contador_params}, ${value}\n` //li a1, 10
                    contador_params +=1;
                }
            }

            env.risc += `jal ${this.id}\n`
        }
    }
}