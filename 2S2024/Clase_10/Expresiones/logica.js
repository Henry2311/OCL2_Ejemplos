import Expresion from "../Interfaces/expresiones.js"

export default class Logicas extends Expresion {

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
            case "&&": return left && rigth
            case "!": {
                if(!left){
                    return !rigth
                }    
                return rigth
            }
            case "||": return left || rigth
        }
    }


    risc(env){
        switch(this.op){
            case "&&": {
                let left = this.izquierda?.risc(env) //L1
                let etiqueta_left = `L${env.generateLabel()}`
                env.risc += `j L${etiqueta_left}:\n`
                env.risc += `${left}:\n`
                let rigth = this.derecha?.risc(env) //L2
                let etiqueta_rigth = `L${env.generateLabel()}`
                env.risc += `j L${etiqueta_rigth}:\n`

                return rigth
            }
            case "||": {
                let etiqueta = `L${env.generateLabel()}`
                
                env.risc += `blt ${left.valor}, ${rigth.valor}, ${etiqueta}\n`

                return etiqueta
            }
        }
    }      
    /**
     *  bgt t0,t1, L1
     *  j L2:
     *  -------
     *  L1: 
     *  blt t2, t3, L3
     *  j L4:
    * L1: 
    *   Instrucciones Verdaderas
    *   j L3
    * L2:
    *   Instrucciones Falsas
    * L3:
    */
}