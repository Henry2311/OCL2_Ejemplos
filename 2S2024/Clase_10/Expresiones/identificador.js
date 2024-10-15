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
    return {'valor':this.id, 'tipo':'identificador'}
  }
}

export default Identificador;
