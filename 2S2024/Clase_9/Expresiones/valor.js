import Expresion from "../Interfaces/expresiones.js"

class Value extends Expresion {
  constructor(value) {
    super();
    this.value = value;
  }

  run(env) {
    return this.value
  }

  risc(env){

    if(typeof this.value == 'number'){
      let temporal = env.generateTemp()
      env.risc += `addi t${temporal}, zero, ${this.value}\n`
      return {'valor':`t${temporal}`, 'tipo':'number'}
    }else{

      let msg = env.generateMsg()
    
      env.dato += `msg${msg}: .asciz "${this.value}"\n`
      
      return {'valor':msg, 'size':this.value.length, 'tipo':'cadena'}
    }

  }
}

export default Value;
