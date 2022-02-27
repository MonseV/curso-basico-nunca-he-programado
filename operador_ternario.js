// operador ternario  -> una condicion en una sola línea

//var usuario = "Uriel";
//var usuario = "Codigo Facilito";

// si usuario es Uriel entonces es el tutor, sino es un Alumno
//var referencia = (usuario == "Uriel") ? "Tutor" : "Alumno";

/*
if(usuario == "Uriel"){
    referencia = "Tutor";
}else{
    referencia = "Alumno";
}
*/

//console.log(referencia);


/*
function my_factorial(numero) {
  if (numero > 1) {
    return numero * my_factorial(numero - 1)
  }
  return 1;
}
console.log(my_factorial(5))
*/

function my_factorial(numero) {
  return (numero > 1) ? numero * my_factorial(numero - 1) : 1;
}

console.log(my_factorial(5))