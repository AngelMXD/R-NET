---
title: "Moderacion"
author:
  name: "[**Cooper**](https://discord.com/users/613098671503835164)"
  avatar: "/assets/imagen-autor.jpg"
date: 2026-02-08
visibility: 
tags:
  - Test

---


El módulo de Moderación de Sapphire es complejo, altamente personalizable y ofrece una amplia gama de comandos.

La siguiente página proporciona una **descripción general** de cómo funciona el **sistema de moderación** de Sapphire en su núcleo, qué características ofrece y **cómo configurarlo** a través del panel de control de Sapphire.

Puedes encontrar una lista de todos los comandos de moderación filtrándolos en la sección **Commands ➜ Default Commands** (Comandos ➜ Comandos Predeterminados) del panel de control de Sapphire.

### Casos

**Introducción**
El sistema de moderación de Sapphire utiliza **casos** para **almacenar la información de las sanciones**. Cada vez que se realiza una acción de sanción moderativa, Sapphire genera un ID de caso que sirve como un identificador único para esa sanción. Una **sanción se refiere a** un baneo (*ban*), silencio (*mute*), expulsión (*kick*) o advertencia (*warn*).

Un caso almacena su **ID de caso**, **tipo de sanción**, **ID de usuario**, **razón**, **duración**, **fecha de creación**, **autor**, **prueba**, **prueba verificada** y **notas del moderador**, junto con los **últimos cinco mensajes** del usuario sancionado por canal. Si está habilitado, Sapphire también muestra los mensajes eliminados de ese usuario de los últimos 30 minutos.

**Descripción General**
El módulo de **Casos** proporciona un resumen completo de todos los Casos de Moderación en un servidor. La información importante sobre la sanción es visible de un vistazo, y se pueden ver más detalles o acciones al hacer clic en cada caso.

En la página de resumen, es posible hacer lo siguiente:

* Filtrar por **tipo de sanción**, **estado abierto del caso** o **mostrar casos masivos**.
* Editar masivamente, **cerrar** o **eliminar** casos.
* Hacer clic en un caso para ver más detalles sobre el mismo y la sanción.


![](/assets/Mod-RC-1.webp)



**Viendo un caso**
Para ver más detalles de un caso específico, haz clic en él en la lista. Esto abre la página de detalles del caso.


**Detalles e Información**

| Nombre | Descripción |
| --- | --- |
| **ID** | Muestra el ID del caso. El ID del caso es el identificador único de ese caso específico y se puede usar para cerrar, eliminar o buscar un caso. |
| **State** (Estado) | Muestra el estado actual de apertura de ese caso. |
| **Type** (Tipo) | El tipo de sanción emitida contra el usuario. Tipos posibles: `WARN`, `MUTE`, `KICK`, `BAN`. |
| **User** (Usuario) | Muestra el nombre de usuario de Discord y el ID del usuario sancionado. |
| **Reason** (Razón) | Muestra la razón dada para la sanción. Una razón es una breve descripción establecida por el moderador de por qué el usuario fue sancionado. |
| **Duration** (Duración) | Muestra la duración de ese caso. Una vez que la duración expira, el usuario dejará de estar sancionado, siempre y cuando no haya otro caso abierto del mismo tipo. |
| **Created** (Creado) | Muestra la hora y fecha en que se creó el caso. |
| **Author** (Autor) | Muestra el nombre de usuario de Discord y el ID del usuario que ejecutó la sanción. El autor es la persona responsable de tomar la acción, por ejemplo, el moderador. |
| **Proof** (Prueba) | Muestra la prueba establecida por un moderador. Esto se puede establecer libremente, pero por lo general debería incluir una captura de pantalla o un enlace al mensaje del mal comportamiento del usuario. |
| **Verified proof** (Prueba verificada) | Muestra el contenido del último mensaje enviado por ese usuario, configurado automáticamente por Sapphire. |


![](/assets/Mod-RC-2.webp)

### Reportes de Usuarios (User Reports)

Los Reportes de Usuarios son una función de Moderación que permite a los usuarios enviar reportes sobre otros usuarios, con opciones personalizables para que los moderadores manejen y gestionen esos reportes.

Cuando se crea un reporte, envía un mensaje a un canal seleccionado que contiene los detalles del reporte y botones de acción. Los moderadores pueden aceptar o ignorar los reportes, y tomar acciones como ejecutar comandos, abrir casos de moderación o eliminar mensajes.

### Configuraciones de Sanciones (Punish Settings)

La categoría **Configuraciones de Sanciones** te permite cambiar lo que sucede cuando baneas, expulsas, silencias y adviertes, cambiar los valores predeterminados de estos tipos de sanciones y más.

**Todos los valores modificables**
*(Algunos de los siguientes campos pueden no estar disponibles para todas las sanciones).*

| Configuración | Descripción |
| --- | --- |
| **Default reason** (Razón predeterminada) | Establece una razón por defecto cuando el moderador no ha proporcionado ninguna. |
| **Internal reason** (Razón interna) | La razón que es visible en el Registro de Auditoría (Audit-log) de Discord y para otros bots. Variables: `${authorid}`, `${authortag}`, `${duration}`, `${reason}`, `${currentdate}` |
| **Default duration (when using command)** (Duración predeterminada) | Establece una duración por defecto cuando no se ha proporcionado ninguna. |
| **Actions on punish** (Acciones al sancionar) | Ejecuta automáticamente acciones adicionales al sancionar a los usuarios. |
| **Force reason (when using command)** (Forzar razón) | Si está habilitado, los moderadores no podrán sancionar a los usuarios sin dar un motivo. |
| **Always review** (Revisar siempre) | Si está habilitado, los moderadores deben revisar la sanción antes de ejecutarla (equivalente a agregar `-r` al final de los comandos). |
| **Delete proof message** (Eliminar mensaje de prueba) | Si está habilitado, el mensaje del usuario sancionado ("Prueba Verificada") se elimina automáticamente. 🔹 *Si el comando de sanción se usa como respuesta, el mensaje al que se responde se elimina.* |
| **Allow multiple mutes** (Permitir múltiples silencios) | Si está habilitado, los usuarios pueden tener varios casos de silencio (mute) activos. 🔹 *Si un silencio expira mientras otro sigue activo, no se produce ninguna acción de des-silenciar (unmute).* 🔹 *El comando `unmute` cierra todos los casos de silencio abiertos.* |
| **Link with timeouts** (Vincular con aislamientos/timeouts) | Si está habilitado, los usuarios reciben un aislamiento (timeout) de Discord cuando son silenciados usando Sapphire. |
| **Extend timeouts** (Extender aislamientos) | Dado que los aislamientos de Discord no pueden exceder los 28 días, Sapphire renovará automáticamente los aislamientos superiores a 28 días. 🔹 *Los usuarios estarán aislados continuamente.* |

**Más opciones**

| Opción | Descripción |
| --- | --- |
| **Reply to message to punish** (Responder al mensaje para sancionar) | Si está habilitado, responder al mensaje de un usuario con un comando de sanción lo sancionará. El contenido del mensaje del usuario se usará como Prueba Verificada. |
| **Confirm punishment when recent case exists** (Confirmar sanción cuando existe un caso reciente) | Si está habilitado, Sapphire pedirá confirmación antes de sancionar a un usuario si este tiene un caso abierto creado recientemente. 🔹 *Esto puede ser útil para evitar que diferentes moderadores emitan la misma sanción dos veces.* |
| **Log expired punishments if user is not in guild** (Registrar sanciones caducadas si el usuario no está en el servidor) | Si está habilitado, las sanciones que caducan seguirán enviando un mensaje de registro (log), incluso si el usuario no está en el servidor. |
| **Cache deleted messages** (Almacenar mensajes eliminados) | Si está habilitado, el contenido de todos los mensajes eliminados se almacenará durante 30 minutos para que puedan mostrarse en el historial de mensajes de un caso. |

### Roles Inmunes (Immune roles)

Los roles inmunes están exentos de acciones punitivas. Este módulo te permite definir roles que no pueden ser sancionados con Sapphire. Esto evita que los moderadores sancionen accidental o intencionalmente a los administradores u otros miembros con ciertos roles.

Los roles pueden ser inmunes a tipos específicos de acciones de moderación, agrupados en las siguientes categorías:

| Categoría | Descripción |
| --- | --- |
| **Global** | Los roles agregados aquí son inmunes a *todos* los tipos de acciones de moderación (baneos, expulsiones, silencios, advertencias). |
| **Bans** | El rol agregado será inmune a los baneos. |
| **Kicks** | El rol agregado será inmune a las expulsiones. |
| **Mutes** | El rol agregado será inmune a los silencios. |
| **Warns** | El rol agregado será inmune a las advertencias. |

Para agregar un rol, haz clic en el símbolo **+** dentro del tipo de sanción.

**Usar jerarquía de roles (Use role hierarchy)**

| Configuración | Descripción |
| --- | --- |
| **Enabled** (Habilitado) | Si está habilitado, los usuarios solo pueden tomar acciones de moderación (ej. sanciones) contra miembros con roles inferiores a su rol más alto en la jerarquía de roles del servidor. 🔹 *Esto asegura que los roles de mayor rango no puedan ser sancionados por usuarios de menor rango.* |
| **Disabled** (Deshabilitado) | Si está deshabilitado, puedes seleccionar manualmente qué roles deben ser inmunes a sanciones específicas, independientemente de su posición en la jerarquía de roles. |

### Notificaciones de usuario

Elige si deseas notificar a los usuarios por mensaje directo (DM) cuando son sancionados o cuando se les retira la sanción.

* **Notify users on punish** (Notificar a los usuarios al sancionar): Si está habilitado, los usuarios que sean sancionados recibirán un mensaje directo de Sapphire. Esto incluye las sanciones a través del AutoMod de Sapphire y mediante comandos.
* **Notify users on unpunish** (Notificar a los usuarios al retirar sanción): Si está habilitado, los usuarios a los que se les retire la sanción recibirán un mensaje directo de Sapphire. Esto incluye vencimientos (cuando acaba el tiempo) y retiros de sanciones por comando.
* **Notify users on punish by another user/bot** (Notificar al sancionar por otro usuario/bot): Si está habilitado, los usuarios que sean sancionados manualmente en Discord o por otro bot recibirán un mensaje directo de Sapphire.
* **Notify users on unpunish by another user/bot** (Notificar al retirar sanción por otro usuario/bot): Si está habilitado, los usuarios a los que se les retire la sanción manualmente en Discord o por otro bot recibirán un mensaje directo de Sapphire.

### Razones Predefinidas (Predefined Reasons)

La categoría de **Razones Predefinidas** de la función de moderación te permite preconfigurar motivos para las sanciones. Se pueden usar *alias* para mostrar la razón completa configurada en el panel de control.

Por ejemplo, si defines "Comportamiento inapropiado" como una razón predefinida con el alias `r1`, puedes escribir `mute @user r1`, y el caso de moderación resultante mostrará "Comportamiento inapropiado" como la razón completa.

### Bloqueo de Canales (Channel Locking)

Bloquea canales en un servidor usando los comandos `lock` y `unlock`. Bloquear canales evita que los usuarios envíen mensajes o se unan a canales de voz.

**Roles ignorados (Ignored roles)**
Los roles añadidos a esta lista **son ignorados por el sistema de bloqueo de canales** de Sapphire. Esto significa que Sapphire no modificará sus permisos al bloquear un canal. Sin embargo, si no existen anulaciones de permisos explícitas para estos roles, **aún pueden verse afectados** por el bloqueo, impidiéndoles enviar mensajes o unirse a canales de voz.

Cuando se desbloquea un canal, **todos los permisos vuelven a su estado anterior**, lo que significa que cualquier cambio realizado mientras el canal estaba bloqueado se descartará.

**Canales a bloquear al usar `lockall`**
Los canales añadidos a esta lista se bloquearán simultáneamente al ejecutar el comando `lockall`.

### Privacidad

La página de **Privacidad** te permite configurar qué **información de los casos es visible** para los usuarios.

**Detalles del mensaje de salida del comando**
Los detalles que se agregan en este campo serán visibles en todos los mensajes de salida de los comandos relacionados con la Moderación, por ejemplo, después de ejecutar un comando de sanción. Se pueden mostrar los siguientes detalles:

| Variable | Explicación |
| --- | --- |
| **Verified Proof** | Muestra la Prueba Verificada de un caso en el mensaje de salida. |
| **Author** | Muestra el ejecutor de la sanción en el mensaje de salida. |
| **Proof** | Muestra la Prueba de un caso en el mensaje de salida. |

**Detalles del mensaje directo (DM)**
Los detalles agregados a este campo serán visibles en todos los mensajes de notificación directos. Se pueden mostrar los mismos detalles (Prueba Verificada, Autor, Prueba).

**Purgar mensajes fijados (Purge pinned messages)**
Elige si los **mensajes fijados** en un canal deben ser **eliminados** al usar el comando `purge`.

---

### Resumen de comandos

*(Esta función también se puede configurar y gestionar a través del panel de control de Sapphire).*

**Crear sanciones**

| Comando | Descripción | Uso |
| --- | --- | --- |
| `ban` | Banea a un usuario del servidor. Añade `-r` para revisar la sanción en un menú modal. | `ban [usuario] [duración] [razón] [-r]` |
| `kick` | Expulsa a un usuario del servidor. Añade `-r` para revisar la sanción. | `kick [usuario] [razón] [-r]` |
| `mute` | Silencia a un usuario. Añade `-r` para revisar la sanción. | `mute [usuario] [duración] [razón] [-r]` |
| `warn` | Advierte a un usuario. Añade `-r` para revisar la sanción. | `warn [usuario] [duración] [razón] [-r]` |
| `massban` | Banea a múltiples usuarios a la vez (el tiempo y la razón se configuran después). | `massban [usuario2] …` |
| `masskick` | Expulsa a múltiples usuarios a la vez. | `masskick [usuario2] …` |
| `massmute` | Silencia a múltiples usuarios a la vez. | `massmute [usuario2] …` |
| `masswarn` | Advierte a múltiples usuarios a la vez. | `masswarn [usuario2] …` |
| `nameban` | Banea a todos los usuarios que tengan `<nombre>` en su usuario/apodo. Añade `-f` para buscar el nombre completo. | `nameban <nombre> [-f]` |
| `namekick` | Expulsa a todos los usuarios que tengan `<nombre>`. | `namekick <nombre> [-f]` |
| `namemute` | Silencia a todos los usuarios que tengan `<nombre>`. | `namemute <nombre> [-f]` |
| `namewarn` | Advierte a todos los usuarios que tengan `<nombre>`. | `namewarn <nombre> [-f]` |
| `timeban` | Banea a usuarios que crearon su cuenta hace `<tiempo>` o se unieron hace `<tiempo>`. | `timeban <created/joined> <tiempo> [duración] [razón]` |
| `timekick` | Expulsa a usuarios según creación de cuenta o unión. | `timekick <created/joined> <tiempo> [razón]` |
| `timemute` | Silencia a usuarios según creación de cuenta o unión. | `timemute <created/joined> <tiempo> [duración] [razón]` |
| `timewarn` | Advierte a usuarios según creación de cuenta o unión. | `timewarn <created/joined> <tiempo> [razón]` |

**Deshacer sanciones**

| Comando | Descripción | Uso |
| --- | --- | --- |
| `unban` | Desbanea a un usuario del servidor. | `unban [razón]` |
| `unmute` | Cierra todos los silencios de un usuario. | `unmute [razón]` |
| `unwarn` | Cierra todas las advertencias de un usuario. | `unwarn` |

**Gestionar casos de sanción**

| Comando | Descripción | Uso |
| --- | --- | --- |
| `casedelete` | Elimina un caso. | `casedelete` |
| `caseinfo` | Muestra información sobre un caso. | `caseinfo [ID del caso]` |
| `caselist` | Muestra una lista de los casos más nuevos (incluyendo los usuarios especificados). | `caselist [usuario] [usuario]` |
| `caseupdate` | Actualiza un caso específico. | `caseupdate [ID del caso] [razón/tiempo [razón]]` |
| `caseclose` | Cierra un caso específico. | `caseclose [razón]` |
| `setproof` | Establece la prueba (proof) para un caso. | `setproof [ID del caso]` |

**Moderación de canales**

| Comando | Descripción | Uso |
| --- | --- | --- |
| `lock` | Bloquea un canal de texto o voz. Al bloquear voz, todos son expulsados del canal. Añade `+v`, `+t` (o `+vt`) para revocar permisos de ver/hilos. Añade `+s` para bloquear silenciosamente. | `lock [canal] [razón] [+(v/t/s)]` |
| `lockall` | Bloquea todos los canales configurados en el panel de control. | `lockall [razón] [+(v/t/s)]` |
| `unlock` | Desbloquea un canal. Añade `+s` para hacerlo en silencio. | `unlock [canal] [razón] [+s]` |
| `unlockall` | Desbloquea todos los canales. Añade `+l` para solo desbloquear los bloqueados con *lockall*. | `unlockall [razón] [+l/s]` |
| `purge` | Elimina mensajes masivamente (por cantidad, por tiempo o entre dos mensajes). Opcionalmente de un solo usuario. | `purge <cantidad/tiempo/ID mensaje> [entre segundo ID/usuario] [usuario]` |
| `setslowmode` | Establece el modo lento (slowmode) de un canal. | `setslowmode [canal]` |

**Información del usuario**

| Comando | Descripción | Uso |
| --- | --- | --- |
| `userinfo` | Obtiene información sobre un usuario. | `userinfo [usuario]` |
| `roleinfo` | Obtiene información sobre todos los roles / un rol específico. | `roleinfo [rol]` |
| `warns` | Obtiene todas las advertencias sobre un usuario. | `warns [usuario]` |
| `usernotes` | Recibe todas las notas sobre un usuario o añade una. | `usernotes [nota a añadir]` |

**Moderación: Reportes de Usuarios (User Reports)**

| Comando | Descripción | Uso |
| --- | --- | --- |
| `report` | Denuncia a un usuario al equipo de moderación del servidor. | `report <usuario/url del mensaje> [comentario]` |
| `report-blacklist` | Bloquea a los usuarios para que no puedan usar el comando report. | `report-blacklist <show/add/remove> [ID del usuario]` |
| `report-ignoreall` | Ignora todos los reportes abiertos en tu servidor a la vez sin notificar. | `report-ignoreall` |
| `report-sendmissing` | Los mensajes informativos de los reportes no deben eliminarse. Ejecuta este comando para traer de vuelta mensajes eliminados de reportes. | `report-sendmissing` |

**Misceláneo (Miscellaneous)**

| Comando | Descripción | Uso |
| --- | --- | --- |
| `linkcaseview` | Vincula la vista de casos de este servidor con otro, para que ambos puedan ver los casos del otro. | `linkcaseview` |
| `predefinedreasons` | Gestiona las razones predefinidas para las sanciones. | `predefinedreasons` |

---



TS-1