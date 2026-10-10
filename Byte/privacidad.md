---
label: Política de privacidad
icon: shield-lock
order: 90
---

# Política de privacidad de Byte

Última actualización: 10 de octubre de 2026

Byte es un bot de Discord de entretenimiento, música y moderación. Esta política explica qué información trata el bot y, en particular, cómo usa los servicios de Google (OAuth y Google Drive) para guardar copias de seguridad.

## 1. Información que recopilamos

**Acceso a Google (OAuth).** El inicio de sesión con Google lo realiza únicamente el desarrollador del bot, con su propia cuenta, para autorizar la subida de copias de seguridad. Los usuarios de Discord nunca inician sesión con Google ni comparten datos de su cuenta de Google con el bot.

El bot solicita un único permiso de Google:

- **Google Drive, `drive.file`**: permite crear archivos en el Drive del desarrollador y acceder solo a los archivos que el propio bot ha creado. El bot **no puede ver, leer ni modificar ningún otro archivo** de Google Drive.

El bot no solicita ni almacena el correo electrónico, el nombre, la foto de perfil ni ningún otro dato personal de la cuenta de Google.

**Datos de Discord.** Para funcionar dentro de los servidores de Discord, el bot guarda:

- Identificadores numéricos de usuarios, servidores, canales y roles de Discord.
- Datos de los módulos del bot: advertencias de moderación, sorteos, tickets de soporte, configuración de registros y de canales de voz temporales, monedas de la economía y niveles de experiencia.
- Copias de la estructura de un servidor, solo si un administrador las solicita: roles, categorías, canales, permisos y qué roles tenía cada miembro.

El bot no guarda el contenido de los mensajes de chat, salvo lo necesario para registrar mensajes editados o borrados en los canales de registro que un administrador haya configurado.

## 2. Cómo utilizamos la información

Usamos estos datos únicamente para:

- Hacer funcionar las funciones del bot dentro de los servidores de Discord.
- Crear copias de seguridad periódicas de los datos del bot y guardarlas en el Google Drive del desarrollador, para poder recuperarlas si se pierde o daña la información del bot.

**No vendemos, alquilamos ni compartimos datos con terceros bajo ningún concepto.**

El uso y la transferencia de la información recibida de las APIs de Google cumplen la [Política de Datos de Usuario de los Servicios de API de Google](https://developers.google.com/terms/api-services-user-data-policy), incluidos los requisitos de Uso Limitado.

## 3. Seguridad de los datos

- Las credenciales de Google se guardan solo en el servidor del bot y nunca se incluyen en las copias de seguridad.
- Las copias se guardan en una carpeta privada del Google Drive del desarrollador, a la que solo él tiene acceso.
- La comunicación con Google se realiza mediante conexiones cifradas (HTTPS).

## 4. Retención y eliminación de datos

- Las copias guardadas en el servidor del bot se rotan automáticamente: se conservan las 10 más recientes. Las copias de Google Drive las elimina el desarrollador manualmente.
- Los datos de un servidor de Discord se mantienen mientras el bot siga en ese servidor.
- Cualquier usuario o administrador puede pedir que se eliminen sus datos escribiendo al correo de contacto. Atenderemos la solicitud en un plazo máximo de 30 días.
- El acceso del bot a Google Drive puede revocarse en cualquier momento desde <https://myaccount.google.com/permissions>.

## 5. Datos de usuario de Google

| | |
|---|---|
| **Datos a los que accede** | Solo los archivos de copia de seguridad que el propio bot crea en el Google Drive del desarrollador (permiso `drive.file`). Ningún otro archivo, ni correo, nombre o foto de perfil. |
| **Para qué los usa** | Subir y guardar copias de seguridad de los datos del bot. |
| **Dónde se guardan** | En el Google Drive del desarrollador. El token de acceso se guarda solo en el servidor del bot. |
| **Con quién se comparten** | Con nadie. No se venden, no se transfieren a terceros y no se usan para publicidad ni para entrenar modelos de inteligencia artificial. |
| **Cuánto tiempo se conservan** | Hasta que el desarrollador borra las copias o revoca el acceso. |
| **Cómo eliminarlos** | Revocando el acceso en <https://myaccount.google.com/permissions> y borrando los archivos de Drive, o escribiendo al correo de contacto. |

## 6. Cambios en esta política

Si esta política cambia, se actualizará esta página y la fecha de "Última actualización".

## 7. Contacto

Si tiene alguna pregunta sobre esta política de privacidad, puede escribirnos a: [Tu correo electrónico de soporte]

---

## English version

**Byte Privacy Policy** (last updated: October 10, 2026)

Byte is a free Discord bot for entertainment, music and moderation. This policy explains what data Byte processes and how it uses Google services.

**1. Google user data accessed.** Only the bot's developer signs in with Google, to authorize backups. Byte requests a single scope, `https://www.googleapis.com/auth/drive.file`, which only allows it to create files in the developer's Google Drive and access the files it created. Byte cannot see, read or modify any other Drive file, and it does not request the user's email address, name or profile picture.

**2. How Google user data is used.** Exclusively to upload and store backups of the bot's own data, so it can be restored if lost or damaged.

**3. Sharing.** Google user data is not sold, shared with or transferred to third parties, and it is not used for advertising or to train AI models.

**4. Storage and protection.** The OAuth token is stored only on the bot's server and is never included in backups. Backups are stored in a private folder of the developer's Google Drive. All communication with Google uses HTTPS.

**5. Retention and deletion.** Backups stay in Drive until the developer deletes them. Access can be revoked at any time at <https://myaccount.google.com/permissions>. Anyone can request deletion of their data by email; requests are handled within 30 days.

**6. Discord data.** To work in Discord servers, Byte stores Discord user, server, channel and role IDs, and data from its modules (moderation warnings, giveaways, support tickets, log and temporary voice channel settings, virtual coins and levels). Server structure snapshots are created only when an administrator requests them.

**7. Limited Use.** Byte's use and transfer of information received from Google APIs to any other app will adhere to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

**8. Contact.** coopercg121@gmail.com
