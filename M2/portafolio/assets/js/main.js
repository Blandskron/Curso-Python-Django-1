// Clave para localStorage
const CART_COUNT_KEY = "cartCount";

// Leer valor actual del carrito desde localStorage (o 0 si no existe)
function getCartCount() {
  const stored = localStorage.getItem(CART_COUNT_KEY);
  return stored ? parseInt(stored, 10) : 0;
}

// Guardar el valor actual del carrito en localStorage
function setCartCount(value) {
  localStorage.setItem(CART_COUNT_KEY, String(value));
}

// Actualizar los elementos que muestran el contador (en navbar y en sección carro)
function updateCartCountUI() {
  const count = getCartCount();

  const cartCountSpans = document.querySelectorAll("#cart-count, #cart-count-detail");
  cartCountSpans.forEach(span => {
    span.textContent = count;
  });
}

// Manejar clic en botones "Agregar al carro"
function attachCartButtons() {
  const buttons = document.querySelectorAll(".btn-add-cart");
  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      const currentCount = getCartCount();
      const newCount = currentCount + 1;
      setCartCount(newCount);
      updateCartCountUI();
      alert("Producto agregado al carro. Total en carro: " + newCount);
    });
  });
}

// Inicializar cuando cargue la página
document.addEventListener("DOMContentLoaded", () => {
  updateCartCountUI();
  attachCartButtons();
});
