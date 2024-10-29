module.exports = {
    format: "es",
    input: "parser.pegjs",
    dependencies: {
        Aritmeticas: "../Expresiones/aritmeticas.js",
        Value: "../Expresiones/valor.js",
        Print: "../Instrucciones/print.js",
    },
}