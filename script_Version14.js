// script.js para macuEnvios

// --- Efecto glow del cursor ---
document.addEventListener("DOMContentLoaded", function() {
  const cursorGlow = document.getElementById('cursor-glow');
  if (cursorGlow) {
    document.addEventListener('mousemove', (e) => {
      cursorGlow.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
      cursorGlow.style.opacity = '0.32';
    });
    document.addEventListener('mouseleave', () => {
      cursorGlow.style.opacity = '0';
    });
    document.addEventListener('mouseenter', () => {
      cursorGlow.style.opacity = '0.32';
    });
  }

  // --- Cotizador de tarifas ---
  const cotizadorForm = document.getElementById("cotizador-form");
  const resultadoCotizador = document.getElementById("resultado-cotizador");
  if (cotizadorForm) {
    cotizadorForm.addEventListener("submit", function(e) {
      e.preventDefault();
      const peso = parseFloat(document.getElementById("peso").value);
      const delicadeza = document.getElementById("delicadeza").value;
      let tarifa = 0;
      if (peso <= 1) tarifa = 5;
      else if (peso <= 3) tarifa = 8;
      else if (peso <= 5) tarifa = 12;
      else tarifa = 12 + Math.ceil(peso - 5) * 3;

      if (delicadeza === "fragil") tarifa += 3;
      if (delicadeza === "muyfragil") tarifa += 5;

      resultadoCotizador.textContent = `Tarifa estimada: S/${tarifa}`;
    });
  }

  // --- Rastreo de paquetes (simulado) ---
  const rastreoForm = document.getElementById("rastreo-form");
  const resultadoRastreo = document.getElementById("resultado-rastreo");
  if (rastreoForm) {
    rastreoForm.addEventListener("submit", function(e) {
      e.preventDefault();
      const codigo = document.getElementById("codigo-rastreo").value.trim();
      if (!codigo) {
        resultadoRastreo.textContent = "Por favor ingresa tu código de rastreo.";
        return;
      }
      // Simulación de respuesta:
      resultadoRastreo.textContent = "⏳ Buscando...";

      setTimeout(() => {
        if (codigo.match(/^MACU[0-9]{4,}$/i)) {
          resultadoRastreo.textContent = `✅ Tu paquete con código ${codigo} está EN CAMINO.`;
        } else {
          resultadoRastreo.textContent = "❌ Código no encontrado. Verifica e inténtalo de nuevo.";
        }
      }, 1200);
    });
  }

  // --- Menú hamburguesa: Cierra el menú al hacer click en un enlace (en móvil) ---
  document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', () => {
      const navToggle = document.getElementById('nav-toggle');
      if (navToggle && window.innerWidth < 700) navToggle.checked = false;
    });
  });
});
