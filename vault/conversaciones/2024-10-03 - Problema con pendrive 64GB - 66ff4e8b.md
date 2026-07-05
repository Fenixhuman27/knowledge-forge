---
titulo: "Problema con pendrive 64GB"
fecha: 2024-10-03
mensajes: 24
origen: ChatGPT
---

# Problema con pendrive 64GB

### Usuario

Tengo un problema y necesito una solución! 
Compré un pendrive de 64 GB y funcionó muy bien, pero por algún motivo ahora mi PC me lo reconoce como disco d no hay medios. No me deja formatear ni verlo, tengo que buscar una solución que lo repare

### Asistente

El problema que estás enfrentando con el pendrive puede estar relacionado con un error de partición o corrupción del sistema de archivos. Te sugiero probar algunas soluciones para intentar repararlo:

### 1. **Usar el Administrador de Discos de Windows:**
   - Presiona `Win + X` y selecciona **Administración de discos**.
   - Busca el pendrive en la lista de discos (puede aparecer como "No hay medios").
   - Si lo encuentras, intenta:
     - Eliminar la partición existente (si es visible) haciendo clic derecho y seleccionando "Eliminar volumen".
     - Luego crea una nueva partición haciendo clic derecho en el espacio no asignado y seleccionando "Nuevo volumen simple".
     - Formatea el pendrive con el sistema de archivos FAT32 o NTFS.

### 2. **Usar la herramienta de **Diskpart**:
   - Abre **Símbolo del sistema** como administrador.
   - Escribe los siguientes comandos uno por uno:
     ```plaintext
     diskpart
     list disk
     select disk X (reemplaza X por el número de tu pendrive)
     clean
     create partition primary
     format fs=ntfs quick
     exit
     ```
   Esto intentará limpiar el pendrive y crear una nueva partición desde cero.

### 3. **Probar herramientas de terceros**:
   Si lo anterior no funciona, intenta con software de recuperación o formateo de discos como:
   - **HP USB Disk Storage Format Tool**.
   - **Rufus** (aunque es principalmente para crear USBs booteables, también puede formatear).
   - **MiniTool Partition Wizard**.

### 4. **Intentar en otra PC o puerto USB:**
   A veces, puede ser un problema de hardware (puerto USB dañado). Intenta conectar el pendrive en otra computadora o en un puerto diferente para descartar esta posibilidad.

Si después de estas pruebas no logras recuperarlo, es posible que el pendrive haya sufrido un daño físico y necesite ser reemplazado.

### Usuario

Dame más opciones de terceros

### Asistente

Aquí tienes más herramientas de terceros que pueden ayudarte a reparar y formatear tu pendrive:

### 1. **AOMEI Partition Assistant**  
   - Es una herramienta potente para gestionar discos y particiones. Permite formatear, eliminar y crear particiones, e incluso reparar discos USB dañados.
   - Ofrece la opción de "Verificar disco" para corregir errores lógicos.
   - **Descarga**: [AOMEI Partition Assistant](https://www.aomeitech.com/)

### 2. **EaseUS Partition Master**  
   - Similar a AOMEI, esta herramienta te permite gestionar particiones y también tiene una función de recuperación de particiones para casos en los que el pendrive no es reconocido correctamente.
   - Puedes formatear el USB con facilidad, incluso si no es detectado en Windows.
   - **Descarga**: [EaseUS Partition Master](https://www.easeus.com/partition-manager/)

### 3. **USB Disk Storage Format Tool (por Ridgecrop Consultants)**  
   - Esta herramienta gratuita es conocida por su capacidad de formatear discos USB que no se pueden formatear de forma convencional en Windows. Permite formatear en FAT32, NTFS o exFAT y reparar sectores defectuosos.
   - Es ideal para cuando Windows te da el error de "No hay medios" o no permite formatear.
   - **Descarga**: [USB Disk Storage Format Tool](http://www.ridgecrop.demon.co.uk/index.htm?guiformat.htm)

### 4. **SD Formatter (SD Association)**  
   - Aunque está diseñado para formatear tarjetas SD, esta herramienta también puede funcionar con algunos pendrives. Tiene la ventaja de ofrecer un formateo seguro y eficiente, ideal para reparar sistemas de archivos dañados.
   - **Descarga**: [SD Formatter](https://www.sdcard.org/downloads/formatter/)

### 5. **HDD Low Level Format Tool**  
   - Esta herramienta realiza un formateo a bajo nivel, lo que borra absolutamente toda la información del dispositivo, incluidos los sistemas de archivos corruptos o los datos inservibles que impiden el uso del pendrive.
   - Debes tener en cuenta que es más lenta que otras herramientas, pero puede ser útil para casos difíciles.
   - **Descarga**: [HDD Low Level Format Tool](https://hddguru.com/software/HDD-LLF-Low-Level-Format-Tool/)

### 6. **RMPrepUSB**  
   - Es una herramienta avanzada con múltiples funciones. Permite formatear, crear particiones y arreglar dispositivos USB corruptos. Además, tiene opciones para testear la integridad del dispositivo y asegurarse de que no tiene defectos físicos.
   - **Descarga**: [RMPrepUSB](https://www.rmprepusb.com/)

### 7. **TestDisk y PhotoRec**  
   - Estas herramientas son más avanzadas y se utilizan principalmente para recuperar datos, pero también pueden ayudar a reparar dispositivos USB dañados. TestDisk puede reconstruir tablas de partición dañadas y PhotoRec recupera datos desde dispositivos que han perdido su sistema de archivos.
   - **Descarga**: [TestDisk & PhotoRec](https://www.cgsecurity.org/)

### 8. **DiskGenius**  
   - Una completa solución de gestión de discos que incluye la opción de reparar USB y discos dañados, formatear, y también recuperar datos. Tiene una opción especial para escanear y reparar sectores defectuosos en dispositivos USB.
   - **Descarga**: [DiskGenius](https://www.diskgenius.com/)

Con estas herramientas, tienes muchas opciones para intentar recuperar y formatear tu pendrive. Asegúrate de probarlas con cuidado y, si tienes datos importantes en el dispositivo, considera usar primero las opciones que incluyan recuperación de datos antes de formatear completamente.

### Usuario

Con HP USB storage me dice 
There si no media un the specified device

### Asistente

El mensaje "There is no media in the specified device" suele indicar que el pendrive no está siendo reconocido correctamente por el sistema, lo cual podría ser un problema más serio, como corrupción del firmware del pendrive o un fallo físico en el dispositivo.

A continuación, te ofrezco algunas opciones adicionales para intentar solucionarlo:

### 1. **Reinstalar el controlador USB**:
   A veces, los controladores USB pueden fallar. Para reinstalarlos:
   - Presiona `Win + X` y selecciona **Administrador de dispositivos**.
   - Busca **Controladoras de bus serie universal (USB)**.
   - Haz clic derecho sobre el dispositivo USB (pendrive) y selecciona **Desinstalar controlador**.
   - Desconecta el pendrive, reinicia tu PC y conéctalo de nuevo para que Windows reinstale el controlador automáticamente.

### 2. **Usar el comando CHKDSK**:
   Aunque el sistema dice que "No hay medios", puedes intentar usar el comando CHKDSK para intentar reparar sectores defectuosos:
   - Abre **Símbolo del sistema** como administrador.
   - Escribe el siguiente comando (cambia "X" por la letra asignada a tu pendrive):
     ```plaintext
     chkdsk X: /f /r
     ```
   Esto buscará errores en el disco y los corregirá si es posible. Si el pendrive está muy dañado, puede que este comando no lo detecte.

### 3. **Probar con software de recuperación de bajo nivel**:
   Dado que tu pendrive podría tener un error de bajo nivel, algunas herramientas más avanzadas podrían ayudarte:
   - **ChipGenius**: Este software te permite identificar el controlador del pendrive (chip interno) y obtener detalles que podrían ayudar a reparar el firmware. Puedes buscar una herramienta de reparación específica para el chip del pendrive después de usar ChipGenius.
     - **Descarga**: [ChipGenius](https://www.usbdev.ru/files/chipgenius/)
   
   - **Flash Drive Repair**: Si identificas el chip con ChipGenius, busca en línea una herramienta de reparación de firmware específica para ese controlador. Algunas herramientas de los fabricantes pueden restaurar completamente el dispositivo.

### 4. **Intentar un formateo de bajo nivel con HDD Low Level Format Tool**:
   Aunque ya mencioné esta herramienta, en casos de mensajes como "No hay medios", un formateo a bajo nivel puede eliminar todos los datos e intentar restaurar la funcionalidad:
   - **Descarga** la herramienta y ejecuta el formateo en modo bajo nivel. Esto puede demorar un tiempo, pero a veces ayuda a solucionar estos problemas.

### 5. **Cambiar de puerto USB o usar otra computadora**:
   Aunque parece básico, a veces el problema es la conexión en el puerto USB o algún problema específico con la computadora. Intenta:
   - Cambiar de puerto USB (usar uno diferente, preferiblemente uno en la parte trasera si es una PC de escritorio).
   - Probar el pendrive en otra computadora para descartar un problema de hardware en tu PC.

### 6. **Consultar garantía o reemplazo**:
   Si ninguna de estas opciones funciona, es probable que el pendrive tenga un problema de hardware irreparable. En ese caso, verifica si está en garantía y puedes solicitar un reemplazo al fabricante o al lugar donde lo compraste.

Si te interesa, puedo guiarte con más detalles en alguno de los pasos que te resulten más útiles.

### Usuario

Con CMD me aparece esto: El disco 1 es ahora el disco seleccionado.

DISKPART> clean

Error del Servicio de disco virtual: No hay medios en el dispositivo.

### Asistente

El error "No hay medios en el dispositivo" en **Diskpart** sugiere que tu pendrive no está siendo reconocido correctamente por el sistema operativo y, lamentablemente, puede indicar un problema físico grave, como una falla en el controlador del pendrive o un daño en la memoria interna del dispositivo. Sin embargo, aún hay algunas cosas que podrías intentar antes de concluir que el dispositivo es irrecuperable.

### Opciones adicionales para solucionar el problema:

#### 1. **Cambiar el puerto o probar en otro equipo**  
   Ya que algunos problemas de hardware son específicos de ciertos puertos USB o equipos, intenta conectar el pendrive en un puerto diferente (preferiblemente en la parte trasera de una PC de escritorio) o en otra computadora. Esto puede confirmar si el problema está en el dispositivo o en la computadora/puerto.

#### 2. **Usar ChipGenius o USBDeview para obtener información del controlador interno**  
   Dado que Diskpart y otras herramientas no pueden detectar correctamente el pendrive, puedes intentar usar **ChipGenius** o **USBDeview** para obtener más información sobre el chip controlador de tu pendrive. Estos programas te dirán si el chip interno del dispositivo está dañado o si es posible recuperar el pendrive mediante una herramienta específica del fabricante.
   - **ChipGenius** te dará detalles sobre el tipo de controlador de tu pendrive. Si tienes esa información, podrías buscar herramientas de reparación específicas para ese controlador.
   - **USBDeview** te mostrará todos los dispositivos USB conectados a tu computadora, e intentará obtener información adicional sobre el estado del pendrive.

   - **Descarga ChipGenius**: [ChipGenius](https://www.usbdev.ru/files/chipgenius/)
   - **Descarga USBDeview**: [USBDeview](https://www.nirsoft.net/utils/usb_devices_view.html)

#### 3. **Actualizar o reinstalar controladores USB**  
   A veces, un problema con los controladores USB puede impedir que el pendrive sea reconocido correctamente. Intenta actualizar o reinstalar los controladores USB de tu computadora:
   - Entra al **Administrador de dispositivos** (`Win + X` > Administrador de dispositivos).
   - Expande la categoría **Controladoras de bus serie universal (USB)**.
   - Haz clic derecho sobre cada controlador y selecciona **Desinstalar dispositivo**.
   - Reinicia la computadora para que Windows vuelva a instalar los controladores automáticamente.

#### 4. **Usar una herramienta de reparación de firmware**  
   Si logras identificar el chip del pendrive con **ChipGenius**, podrías intentar buscar una herramienta específica para reparar el firmware del dispositivo. Algunas veces, los fabricantes tienen herramientas para restaurar el firmware del pendrive cuando el sistema no puede reconocerlo correctamente. En este caso, necesitarías buscar por el fabricante del chip.

#### 5. **Intentar con Linux o una distribución en vivo**  
   A veces, Linux es más efectivo al interactuar con dispositivos USB problemáticos. Puedes intentar arrancar tu computadora con una distribución **Linux Live** (como Ubuntu o cualquier otra) desde un USB o CD, y ver si el sistema operativo puede reconocer y formatear el pendrive. Esto es útil cuando Windows no puede manejar bien dispositivos USB defectuosos.

#### 6. **Garantía o reemplazo**  
   Si nada funciona, es muy probable que el pendrive esté dañado físicamente. Si está en garantía, intenta reemplazarlo por uno nuevo.

Si decides probar alguna de estas soluciones y necesitas más ayuda en el proceso, no dudes en decírmelo.

### Usuario

Nada a funcionado y no tengo garantía, necesito formatear o forzar el formateo de este USB, tiene que existir herramientas más poderosas que lo hagan, puede buscar?

### Asistente

Para resolver el problema de "No hay medios en el dispositivo", existen algunas herramientas más potentes que puedes intentar:

1. **MiniTool Partition Wizard**: Esta herramienta puede ayudarte a reparar el MBR (Master Boot Record) del USB. Solo tienes que instalar la versión gratuita, conectar el pendrive, seleccionar la opción de "Rebuild MBR" y aplicar los cambios. Este software es muy efectivo cuando el MBR está dañado, lo que puede causar el error de "No Media"【17†source】【18†source】.

2. **Wondershare Recoverit**: Este programa ofrece diversas soluciones para corregir errores en dispositivos USB. Puedes usar la opción de escaneo y reparación de errores en el USB o utilizar el comando CHKDSK desde el propio programa. Recoverit también permite forzar un formateo cuando otros métodos no funcionan【17†source】.

3. **HDD Low Level Format Tool**: Esta herramienta realiza un formateo de bajo nivel en el pendrive, eliminando cualquier problema persistente. Es ideal para casos en los que otras utilidades no pueden formatear el dispositivo debido a errores como "No Media".

Antes de probar cualquier herramienta, asegúrate de verificar que no sea un problema físico del USB, como daños o una falsa capacidad en la unidad.

### Usuario

El USB es nuevo

### Asistente

Dado que el USB es nuevo, es posible que el problema esté relacionado con un defecto de fabricación o una incompatibilidad con el sistema. Aunque hayas probado varias soluciones, algunas herramientas avanzadas que podrían ayudarte a forzar el formateo incluyen:

1. **HDD Low Level Format Tool**: Esta utilidad es conocida por realizar un formateo de bajo nivel, lo que puede resolver problemas en dispositivos USB que no responden a métodos tradicionales. Puede ser efectiva en casos donde el USB es nuevo pero presenta errores. Asegúrate de seleccionar el pendrive correcto al usarla, ya que este tipo de formateo borra todos los datos de forma irreversible.

2. **AOMEI Partition Assistant**: Esta herramienta es otra opción que permite intentar varias reparaciones. Ofrece un método para "formatear fuerza", útil cuando el sistema no permite hacerlo por medios normales. Puedes probarla para borrar particiones corruptas o reparar errores en el pendrive.

3. **USB Flash Drive Online Recovery**: Algunos fabricantes de chips de USB tienen herramientas específicas para restaurar sus unidades. Usando programas como **ChipGenius** para identificar el controlador interno, podrías acceder a la herramienta específica del fabricante para restaurar tu USB.

Si ninguna de estas herramientas funciona, es posible que el problema sea un defecto de hardware en la unidad. Aunque el USB sea nuevo, podría estar dañado desde la fábrica, y si no tienes garantía, quizás quieras considerar reemplazarlo.

### Usuario

Ya me diste esas opciones

### Asistente

Dado que las soluciones anteriores no funcionaron y el USB es nuevo, es posible que el problema sea más complejo o requiera una herramienta aún más avanzada. Aquí tienes otras opciones que puedes probar para forzar el formateo o reparar el USB:

### 1. **USB Disk Storage Format Tool**
   - Esta herramienta gratuita puede realizar un formateo a bajo nivel en discos USB que muestran errores de "No Media". Tiene opciones para reparar errores del sistema de archivos y volver a habilitar el uso del pendrive. Puedes probar esta herramienta, ya que en algunos casos puede forzar el reconocimiento del dispositivo cuando otros métodos fallan.
   - [Descargar USB Disk Storage Format Tool](https://www.techspot.com/downloads/7245-usb-disk-storage-format-tool.html)

### 2. **TestDisk & PhotoRec**
   - **TestDisk** es una potente utilidad de recuperación de particiones que también puede ayudarte a reescribir el MBR y corregir problemas de detección. Es una opción avanzada que puede intentar reconstruir la estructura del pendrive.
   - **PhotoRec**, por otro lado, es su herramienta complementaria, útil si tienes archivos en el USB que deseas recuperar antes de forzar el formateo.
   - [Descargar TestDisk](https://www.cgsecurity.org/wiki/TestDisk_Download)

### 3. **Bootice**
   - **Bootice** es una herramienta avanzada que permite manipular particiones, MBR y PBR de discos extraíbles. Es útil para discos que presentan problemas para ser formateados. Con Bootice, podrías intentar reescribir el MBR o PBR y luego formatear el dispositivo desde ahí.
   - [Descargar Bootice](https://www.softpedia.com/get/System/Boot-Manager-Disk/Bootice.shtml)

### 4. **AlcorMP Tool**
   - Si identificaste el chip de tu pendrive con **ChipGenius** y este es fabricado por **Alcor**, puedes usar **AlcorMP Tool**, una herramienta específica del fabricante para reparar errores a nivel de firmware en unidades USB. Este tipo de herramientas está diseñada para reinstalar o reparar el firmware de unidades USB que presentan errores graves.
   - **Nota**: Si tu pendrive tiene un chip de otro fabricante, busca una herramienta específica basada en la información del chip.
   - [Descargar AlcorMP Tool](https://www.usbdev.ru/files/alcor/)

### 5. **Buscar en bases de datos de reparación de USB**  
   Existen varias bases de datos de herramientas de reparación USB según el controlador del pendrive. **Flash Drive Repair** y otras páginas recopilan herramientas específicas según el chip interno del USB. Si logras identificar el fabricante y tipo de controlador con **ChipGenius** o **USBDeview**, podrías encontrar una herramienta adecuada en estas bases de datos.

Si estas herramientas no funcionan, es muy probable que el pendrive esté dañado irreversiblemente a nivel físico, y la única solución viable sería reemplazarlo.

### Usuario

Mi pendrive es nand 
Modelo USB 2disk
Controlador firstchip
Controlador part number FC1178BC 
Flash ID code: 89d3ac32c204 Intel 1ce/single Channel [qlc]

### Asistente

Dado que tu pendrive tiene un controlador **FirstChip FC1178BC** y es una memoria **NAND** con **Flash ID Intel QLC**, puedes utilizar herramientas especializadas para ese controlador y flash en particular. Aquí te doy algunos pasos para proceder:

### Herramienta de reparación: **FC MpTool**
El controlador **FirstChip** tiene una herramienta específica llamada **FC MpTool** que está diseñada para formatear y reparar pendrives con ese chip. Es ideal para resolver problemas a nivel de firmware y controlador, que es lo que parece estar ocurriendo con tu unidad. 

#### Pasos para usar FC MpTool:
1. Descarga **FC MpTool** desde una página confiable, como [usbdev.ru](https://www.usbdev.ru/files/firstchip/fcmptool/), que ofrece versiones específicas para FirstChip.
2. Conecta tu pendrive a la PC.
3. Ejecuta la herramienta y permite que detecte automáticamente tu dispositivo.
4. Una vez detectado, sigue los pasos que la herramienta indique para reparar o formatear la unidad. A menudo, el software reinstala el firmware, resolviendo errores de "No Media".

### Consideraciones:
- **ChipGenius** y otras herramientas de identificación ya te han dado los datos correctos de tu pendrive. Usar la herramienta específica para FirstChip puede forzar el formateo, incluso si otros métodos han fallado.
- Es importante utilizar la versión correcta de la herramienta, según tu controlador (**FC1178BC**). Algunas versiones pueden no ser compatibles con todos los modelos, así que verifica que estés utilizando la adecuada.

Si esto no funciona, el problema puede estar a nivel físico de la memoria NAND, en cuyo caso sería difícil de reparar sin equipo especializado.

### Usuario

Estoy pensando, en teoría si elimino los drivers en Windows/system32 de este pendrive, cuando lo vuelva a conectar, debería buscar y reinstalarlos?

### Asistente

Eliminar manualmente los controladores de un pendrive desde **C:\Windows\System32** no suele ser una solución recomendada, ya que los drivers genéricos de dispositivos USB están integrados en Windows y eliminar archivos críticos podría causar problemas en otros dispositivos USB o en el sistema.

Sin embargo, puedes intentar desinstalar el controlador del dispositivo de manera más segura usando el **Administrador de dispositivos** de Windows. Esto forzará al sistema a reinstalar el controlador la próxima vez que conectes el pendrive. Aquí tienes cómo hacerlo:

### Pasos para desinstalar y reinstalar el controlador del pendrive:

1. Conecta el pendrive a tu computadora.
2. Haz clic derecho en el menú de inicio y selecciona **Administrador de dispositivos**.
3. Busca la sección **Unidades de disco** o **Controladoras de bus serie universal (USB)** y expándela.
4. Busca tu pendrive en la lista. Si aparece con un símbolo de advertencia o error, ese es el que debes seleccionar.
5. Haz clic derecho sobre el dispositivo y selecciona **Desinstalar dispositivo**.
6. Marca la casilla que dice **Eliminar el software de controlador para este dispositivo** si está disponible y confirma la acción.
7. Desconecta el pendrive de tu computadora.
8. Reinicia la computadora.
9. Conecta de nuevo el pendrive y Windows debería buscar e instalar los controladores automáticamente.

Este método es más seguro, ya que permite a Windows manejar la reinstalación de los controladores de manera controlada. Si el sistema sigue sin reconocerlo correctamente, es probable que el problema esté en el hardware del pendrive o en su firmware, no en los controladores de Windows.

Si decides hacerlo manualmente, asegúrate de que no eliminas ningún controlador crítico. Además, eliminar controladores USB genéricos puede afectar otros dispositivos conectados al puerto USB.

### Usuario

Logré reparar mi pendrive con firstchip mptools pero ahora mi pendrive de 64 GB me aparece como de 16 GB. Como recupero el almacenamiento que falta?

### Asistente

El hecho de que tu pendrive ahora aparezca con solo 16 GB después de usar **FirstChip MpTools** puede deberse a que el programa ha establecido una configuración incorrecta de particiones o capacidad, limitando el almacenamiento visible.

Para recuperar el espacio faltante, puedes intentar las siguientes soluciones:

### 1. **Reparticionar con Disk Management (Administración de discos)**:
   - Abre **Disk Management** en tu PC (haz clic derecho en el menú de inicio y selecciona "Administración de discos").
   - Localiza tu pendrive, que debería aparecer con una partición de 16 GB.
   - Si ves espacio "no asignado" en el pendrive, puedes expandir la partición actual o crear una nueva para usar el espacio restante:
     - Haz clic derecho en la partición de 16 GB y selecciona **Extender volumen** si la opción está disponible.
     - Si no puedes extender, puedes eliminar la partición actual (recuerda respaldar los datos) y crear una nueva que ocupe todo el espacio disponible (64 GB).

### 2. **Reparar usando MPTools**:
   - A veces, **FirstChip MpTools** puede haber aplicado un perfil incorrecto. Puedes volver a ejecutar el programa, pero esta vez asegúrate de elegir correctamente la capacidad de tu pendrive (64 GB) en los ajustes avanzados.
   - También es importante seleccionar el tipo de flash correcto para que la herramienta no reduzca el tamaño del almacenamiento.

### 3. **Formateo de bajo nivel**:
   - Usa una herramienta de formateo de bajo nivel como **HDD Low Level Format Tool** o **ChipGenius** para restablecer el pendrive a su capacidad completa. Esta opción reiniciará el estado de la memoria y puede corregir errores que limiten la capacidad.

### 4. **Herramientas del

### Usuario

La respuesta se cortó , vuelve a darme la respuesta desde el número 4 y explícame como hacer paso a paso la recuperación con el programa firstchip mptools

### Asistente

Aquí continúo la respuesta desde el número 4 y explico cómo recuperar el almacenamiento con **FirstChip MpTool**.

### 4. **Usar herramientas de recuperación de tamaño de disco**
   Algunas herramientas como **Flash Drive Recovery Tools** o **Chip Genius** pueden ayudar a restaurar la capacidad total del pendrive. Estas herramientas intentan reparar el firmware del controlador, similar a lo que hace **MpTools**, pero están diseñadas específicamente para problemas de capacidad incorrecta.

---

### **Recuperación del almacenamiento con FirstChip MpTool (paso a paso)**:

1. **Descarga y abre FirstChip MpTool**:
   - Descarga una versión confiable de **FirstChip MpTool** desde un sitio como **usbdev.ru** o algún otro repositorio que soporte tu modelo de controlador.
   - Extrae los archivos y ejecuta el programa como administrador (clic derecho en el archivo `.exe` y selecciona "Ejecutar como administrador").

2. **Conecta tu pendrive**:
   - Asegúrate de que el pendrive esté conectado a tu computadora. El programa debería detectarlo automáticamente.

3. **Verifica las opciones de configuración**:
   - En el menú principal de MpTool, busca una opción de configuración avanzada o ajustes (suele ser un botón marcado como **Settings** o **Config**).
   - Aquí debes seleccionar correctamente la **capacidad total** de tu pendrive (64 GB) y asegurarte de que el tipo de memoria flash (QLC, Intel) sea correcto. Esta información se puede verificar con **ChipGenius** si no estás seguro.
   
4. **Selecciona el perfil correcto**:
   - Algunos controladores FirstChip tienen múltiples perfiles de configuración. Debes seleccionar el que corresponda a la capacidad completa de tu dispositivo (64 GB en tu caso). Si el perfil predeterminado es incorrecto, busca una opción que se ajuste al almacenamiento correcto.

5. **Reiniciar el proceso de formateo**:
   - Haz clic en **Start** o **Run** para que MpTool comience el proceso de reparación y formateo. Esto debería reescribir el firmware y recuperar el espacio perdido en el pendrive.
   
6. **Verifica la capacidad**:
   - Una vez que el proceso finalice, desconecta y vuelve a conectar el pendrive. Verifica su capacidad en el **Explorador de archivos** o en **Administración de discos**. Debería mostrar los 64 GB completos.

Si después de seguir estos pasos el problema persiste, es posible que el firmware del dispositivo esté dañado de forma irreversible o que el dispositivo haya sido programado para una capacidad inferior. Si necesitas más ayuda con los perfiles o configuraciones específicas en MpTool, puedes buscar guías avanzadas sobre tu modelo en particular.

### Usuario

Recupere 62 GB de los 64 iniciales

### Asistente

¡Qué bueno que recuperaste casi todo el almacenamiento! Si te falta 1-2 GB de los 64 GB originales, esto es bastante normal. Muchos dispositivos de almacenamiento como pendrives y discos duros no muestran el total de capacidad nominal debido a cómo los sistemas operativos calculan el almacenamiento.

### Razones comunes de la diferencia en capacidad:
1. **Conversión entre gigabytes y gibibytes**:
   - Los fabricantes de dispositivos de almacenamiento suelen usar la medida decimal para los gigabytes (GB), donde 1 GB = 1,000,000,000 bytes.
   - Windows y otros sistemas operativos muestran la capacidad en gibibytes (GiB), donde 1 GiB = 1,073,741,824 bytes.
   - Por eso, un dispositivo de 64 GB se mostrará como 59-62 GiB aproximadamente en tu sistema.

2. **Espacio reservado por el sistema**:
   - Algunos controladores o sistemas reservan una pequeña porción del espacio para gestión de errores o almacenamiento seguro de archivos del sistema o de firmware.

En resumen, los 62 GB que ves están dentro de lo esperado, y no es un fallo en tu pendrive. ¡Parece que ya está completamente funcional!
