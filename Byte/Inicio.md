---
label: Inicio
icon: home
order: 100
---

# Byte, bot de Discord

!!!
**Propósito de la app:** Byte es un bot de Discord gratuito que ofrece entretenimiento (música, economía, niveles y minijuegos) y herramientas de moderación a los servidores de Reino Estelar. Usa Google Drive con un único fin: **guardar copias de seguridad de los datos del propio bot** en el Drive de su desarrollador. Esta página es pública y no requiere iniciar sesión.
!!!

**Byte** es un bot de Discord todo en uno para las comunidades de Reino Estelar: música, economía, niveles, minijuegos y herramientas de moderación en un solo bot.

Todos los comandos funcionan con barra (`/comando`) o con prefijo (`!comando`). Usa `/help` dentro de Discord para ver la ayuda por categorías.

## 🎵 Música

Reproduce música en tu canal de voz desde YouTube o enlaces de Spotify (canciones, álbumes y playlists).

| Comando | Qué hace |
|---|---|
| `/play <nombre o enlace>` | Busca y reproduce una canción, o la añade a la cola |
| `/pause` · `/resume` | Pausa o reanuda |
| `/skip` · `/stop` | Salta la canción o detiene la música |
| `/queue` · `/nowplaying` | Muestra la cola y la canción actual |
| `/loop` · `/shuffle` | Repite la canción o la cola, o la mezcla |
| `/volume <0-100>` · `/leave` | Ajusta el volumen o desconecta al bot |

## 💰 Economía

Cada servidor tiene sus propias monedas 🪙 para ganar, ahorrar, apostar y gastar.

| Comando | Qué hace |
|---|---|
| `/daily` | Recompensa diaria, que crece si mantienes la racha |
| `/trabajar` | Gana monedas una vez por hora |
| `/balance` | Muestra tu cartera y tu banco |
| `/depositar` · `/retirar` | Mueve monedas al banco, donde no te las pueden robar |
| `/pagar @usuario` | Regala monedas a otra persona |
| `/robar @usuario` | Intenta robar de su cartera (si te atrapan, pagas multa) |
| `/tienda` · `/comprar` · `/inventario` | Compra artículos o roles que venda el servidor |
| `/top-dinero` | Ranking de las personas más ricas |

## ⭐ Niveles

Gana experiencia participando en el chat y en los canales de voz.

| Comando | Qué hace |
|---|---|
| `/rank` | Tu nivel, experiencia y puesto en el ranking |
| `/top-niveles` | Las 10 personas con más nivel |
| `/niveles-recompensas` | Roles que se ganan al subir de nivel |

Cada nivel nuevo también da monedas, y los administradores pueden configurar roles de recompensa.

## 🎮 Minijuegos

Todos están dentro de `/jugar`, y la mayoría permite apostar monedas.

| Comando | Qué hace |
|---|---|
| `/jugar trivia` | Pregunta de cultura general con 4 opciones |
| `/jugar ahorcado` | Todo el canal adivina la palabra letra por letra |
| `/jugar adivina` | Adivina el número del 1 al 100 en 7 intentos |
| `/jugar tres-en-raya` | Contra otra persona o contra el bot |
| `/jugar conecta4` | Cuatro en línea contra otra persona |
| `/jugar ppt` · `/jugar moneda` · `/jugar tragamonedas` | Piedra, papel o tijera, cara o cruz y tragamonedas |

## 🎉 Comunidad

- **Sorteos** con botón para participar (`/sorteo`).
- **Anuncios** con formato, botones y programación (`/anuncio`).
- **Canales de voz temporales**: cada persona crea su propio canal y lo controla con un panel de botones.
- **Reportes**: los usuarios pueden avisar de errores o enviar sugerencias con `/reportar`.

## 🛡️ Moderación

- Expulsar, banear, silenciar y limpiar mensajes (`/kick`, `/ban`, `/timeout`, `/clear`).
- Advertencias que se guardan aunque el bot se reinicie (`/warn`, `/warnings`).
- Registro de actividad del servidor: mensajes editados o borrados, entradas, salidas y cambios.
- Copias de seguridad de la estructura del servidor para recuperarlo tras un borrado o un raid.

## 💾 Copias de seguridad con Google Drive

Para no perder la información del bot, Byte guarda copias de seguridad periódicas en el Google Drive del desarrollador. Usa el inicio de sesión de Google (OAuth) con un único permiso, `drive.file`, que solo le permite crear y acceder a los archivos que el propio bot sube. Los usuarios de Discord nunca inician sesión con Google.

## Documentos legales

- [Política de privacidad](privacidad.md)
- [Términos y condiciones](terminos.md)

## Contacto

Correo electrónico: coopercg121@gmail.com

---

## English summary

**Byte** is a free, all-in-one Discord bot for the Reino Estelar communities. It provides music playback, a virtual economy, experience levels, minigames, giveaways, announcements, temporary voice channels and moderation tools.

**Why Byte uses Google:** Byte uses Google OAuth with a single scope, `drive.file`, only so that the bot's developer can store **backups of the bot's own data** in their personal Google Drive. Discord users never sign in with Google, and the bot cannot read any Drive file it did not create.

- [Privacy Policy](privacidad.md)
- [Terms of Service](terminos.md)
