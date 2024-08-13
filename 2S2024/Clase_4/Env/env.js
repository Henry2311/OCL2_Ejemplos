class Env {
    constructor(anterior){
        this.anterior = anterior
        this.tabla = {}
    }

    setSymbol(id, symbol){
        if(id in this.tabla){
            console.log("La variable ya existe")
            return
        }
        this.tabla[id] = symbol
    }

    updateSymbol(id, symbol){
        if(id in this.tabla){
            this.tabla[id] = symbol
        }else{
            console.log("La variable no esta declarada")
            return
        }
    }

    getSymbol(id){
        if(id in this.tabla){
            return this.tabla[id]
        }else{
            console.log("La variable no esta declarada")
            return
        }
    }

}