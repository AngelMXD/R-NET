

## 📅 Actualización marzo 2026

### 🛠 Versión 5.0.0 — *22 de marzo, 2026*

**🆕 Novedades**

  - **Soporte PWA (Progressive Web App):** R-NET ahora es instalable como una aplicación nativa en dispositivos móviles y de escritorio, con iconografía propia y soporte offline básico.
  - **Control de Acceso Basado en Identidad:** Migración del sistema de seguridad de la `/guia-de-moderacion`,a **Cloudflare Zero Trust**, validando el ingreso mediante cuentas de Google autorizadas y sesiones con expiración automática para máxima protección.
  - **Protección CSP (Content Security Policy):** Despliegue de cabeceras de seguridad estrictas para blindar la intranet contra inyecciones de código malicioso y ataques XSS.
  - Implementación de un sistema de notificaciones para actualizaciones importantes. (Fase de prueba)

**✨ Mejoras**

  - **Enrutamiento Dinámico Fluido:** Resolución definitiva de los "errores 404 fantasma" y bloqueos 503; la navegación entre los menús y secciones ahora es instantánea gracias al manejo correcto del Service Worker.
  - Refactorización total del entorno de despliegue en Netlify, migrando a un entorno Linux puro y eliminando dependencias obsoletas que causaban cuellos de botella.
  - Optimización del rendimiento del sitio web, reduciendo los tiempos de carga en un 20%.

**🛠 Cambios**

  - Desactivación del sistema "Legacy Prerendering" a favor de un enrutamiento SPA (Single Page Application) moderno, optimizando la carga asíncrona de páginas.
  - Ajuste en el proceso de compilación (`build`) para inyectar dinámicamente las reglas de seguridad y caché (`_headers`) directamente en el servidor final.
  - Integración de nuevas funciones de búsqueda avanzada.
  - Corrección de errores tipográficos en varias secciones de la guía.
  - Actualización de enlaces y referencias a recursos externos.


==- Ver resumen técnico completo (DevOps & ST)

  - Limpieza profunda del árbol de dependencias de Git y Node (`package-lock.json`, `node_modules`).
  - Despliegue del script `protect.js` en Netlify Edge Functions para interceptar peticiones sin romper la carga en segundo plano (prefetch) del framework de Retype.
  - Relajación controlada de reglas de seguridad (CSP) para permitir el funcionamiento de métricas de diagnóstico (Cloudflare Insights).
  - Revisión de la API de despliegue y mejor práctica de caché.
  - Ajustes en la tabla de contenidos para la versión móvil.
===


