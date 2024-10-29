import Expresion from "../Interfaces/expresiones.js"

class Identificador extends Expresion {
  constructor(id) {
    super();
    this.id = id;
  }

  run(env) {
    let value = env.getSymbol(this.id)
    return value.valor
  }

  risc(env){

    let value = this.id
    if(env.use_params){
      env.contador_params += 1

      value = `a${env.contador_params}`
    }

    return {'valor':value, 'tipo':'identificador'}
  }
}

export default Identificador;
