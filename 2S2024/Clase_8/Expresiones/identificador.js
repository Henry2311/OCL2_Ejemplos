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
}

export default Identificador;
