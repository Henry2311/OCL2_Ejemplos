import Expresion from "../Interfaces/expresiones.js"

class Value extends Expresion {
  constructor(value) {
    super();
    this.value = value;
  }

  run(env) {
    return this.value
  }
}

export default Value;
