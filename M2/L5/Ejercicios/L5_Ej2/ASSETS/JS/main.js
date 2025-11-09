// Lección 5 - Ejercicio 2
// Código para hacer smooth scroll al inicio al presionar el botón «Ir arriba»

console.log("main.js cargado correctamente (Ejercicio 2).");

const btnIrArriba = document.getElementById("btnIrArriba");

btnIrArriba.addEventListener("click", function () {
  // Opción 1: scroll hasta la parte superior de la ventana
  window.scrollTo({
    top: 0,
    behavior: "smooth" // aquí está el smooth scroll
  });

  // También podrías usar scroll hacia un elemento concreto:
  // document.getElementById("top").scrollIntoView({ behavior: "smooth" });
});
