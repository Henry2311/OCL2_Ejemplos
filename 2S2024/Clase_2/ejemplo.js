import { parse } from "./parser.js";

let x;

document.getElementById("procesar").addEventListener("click", function(e) {
    x = document.getElementById("entrada").value;
    document.getElementById("salida").innerHTML = parse(x)
});