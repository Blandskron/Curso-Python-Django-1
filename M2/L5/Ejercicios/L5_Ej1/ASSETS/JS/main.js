// Archivo JavaScript externo para Lección 5 - Ejercicio 1

console.log("main.js cargado correctamente (Ejercicio 1).");

const boton = document.getElementById("btnProbarJs");
const resultado = document.getElementById("resultado");

boton.addEventListener("click", function () {
  resultado.textContent = "El archivo main.js está funcionando correctamente.";
});
