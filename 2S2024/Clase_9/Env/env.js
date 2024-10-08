export default class Env {
    constructor(anterior){
        this.anterior = anterior
        this.tabla = {}
        this.console = ""
        this.errores = []

        this.temporal = -1
        this.msg = -1
        this.dato = ""
        this.risc = ""
    }

    addConsole(valor){
        this.console += valor + "\n"
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

    generateTemp(){
        this.temporal += 1

        if(this.temporal ==7){
            this.temporal = 0
        }
        return this.temporal
    }

    lastTemp(){
        return this.temporal
    }

    generateMsg(){
        this.msg +=1 
        return this.msg
    }

    lastMsg(){
        return this.msg
    }

}