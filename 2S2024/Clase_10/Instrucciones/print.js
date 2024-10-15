import Instrucciones from "../Interfaces/instrucciones.js"

export default class Print extends Instrucciones {

    constructor(expresiones){
        super();
        this.expresiones = expresiones
    }

    run(env){
        env.addConsole(this.expresiones.run(env))
    }
    
    save(env){
        console.log("SAVE DECLARACION")
    }

    risc(env){
        let exp = this.expresiones.risc(env)
        
        if(exp.tipo == 'cadena'){
            env.risc += `la a1, msg${exp.valor}
                         li a2, ${exp.size}
                         li a0, 1
                         li a7, 64
                         ecall\n`
        }else if(exp.tipo == 'number'){
            env.risc += `la a0, ${exp.valor}
                         li a7, 1
                         ecall\n`
        }else if(exp.tipo == 'identificador'){
            let temporal = env.generateTemp()
            env.risc += `la t${temporal}, ${exp.valor}
                         lw a0, 0(t${temporal})
                         li a7, 1
                         ecall\n`
        }

    }
}