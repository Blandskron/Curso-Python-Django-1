// Lección 5 - Ejercicio 3
// Archivo JavaScript EXTERNO correctamente linkeado desde index.html

console.log("main.js cargado correctamente (Ejercicio 3).");

const btnIrArriba = document.getElementById("btnIrArriba");
const estadoJs = document.getElementById("estadoJs");

// Indicamos visualmente que el JS está cargado
estadoJs.textContent = "El archivo JS externo está cargado y funcionando.";

// Reutilizamos el mismo comportamiento de smooth scroll al inicio
btnIrArriba.addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
