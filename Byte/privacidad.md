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

## 5. Cambios en esta política

Si esta política cambia, se actualizará esta página y la fecha de "Última actualización".

## 6. Contacto

Si tiene alguna pregunta sobre esta política de privacidad, puede escribirnos a: coopercg121@gmail.com
