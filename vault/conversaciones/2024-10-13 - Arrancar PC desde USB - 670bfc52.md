---
titulo: "Arrancar PC desde USB"
fecha: 2024-10-13
mensajes: 14
origen: ChatGPT
---

# Arrancar PC desde USB

### Usuario

Cómo puedo arrancar mi PC desde una unidad USB? Recuerdas que PC tengo verdad?

### Asistente

Sí, recuerdo que tu computadora tiene un procesador AMD A4-3300 APU. Para arrancar desde una unidad USB, sigue estos pasos:

1. **Inserta la unidad USB**: Conecta la unidad USB de arranque en uno de los puertos de tu computadora.

2. **Reinicia tu PC**: Apaga la computadora si está encendida y luego enciéndela de nuevo.

3. **Accede al BIOS o UEFI**:
   - Mientras la PC se está encendiendo, presiona repetidamente la tecla adecuada para ingresar al BIOS o al menú de arranque. Generalmente, en muchas PCs con procesadores AMD, puede ser una de las siguientes teclas: `Esc`, `F2`, `F10`, `F12`, o `Supr`.
   - Aparecerá un mensaje en pantalla que te indica qué tecla presionar, como "Press [key] to enter BIOS/Setup".

4. **Selecciona la unidad USB**:
   - Una vez dentro del BIOS, busca el apartado de "Boot" o "Boot Order" (Orden de Arranque).
   - Cambia el orden de arranque para que la unidad USB esté primero en la lista.
   - Si tu BIOS tiene una opción de "Boot Menu" (menú de arranque), puedes presionar esa tecla directamente y elegir la unidad USB sin cambiar el orden permanentemente.

5. **Guarda los cambios y reinicia**:
   - Guarda los cambios y reinicia tu computadora. Esto normalmente se hace presionando `F10` y luego confirmando con `Enter`.

Tu computadora debería arrancar desde la unidad USB si esta está configurada correctamente para ser booteable.

Si encuentras algún problema, avísame para que te pueda ayudar.

### Usuario

Cuál sería la opción correcta?

### Asistente

En la imagen que has compartido, la opción más adecuada para arrancar desde una unidad USB booteable es **USB-HDD**. Selecciona esa opción, presiona `Enter` para aceptar, y luego guarda los cambios y reinicia la PC.

Si la unidad USB está correctamente configurada para arrancar, el sistema debería iniciar desde allí.

### Usuario

Y ahora que debo hacer? Existe un problema?

### Asistente

En la imagen que has compartido, se ven varios mensajes de error relacionados con **ACPI** (Advanced Configuration and Power Interface), específicamente errores del tipo **AE_NOT_FOUND**, lo que significa que hay problemas al intentar resolver referencias de ACPI en tu sistema. Estos errores no siempre impiden que el sistema arranque, pero podrían afectar la compatibilidad con algunos componentes de hardware.

El sistema también está detectando un dispositivo Android TV en `/dev/sdb1`, lo que podría estar relacionado con el dispositivo USB que has conectado.

### Soluciones posibles:
1. **Ignorar temporalmente los errores de ACPI**: Si el sistema continúa arrancando después de estos mensajes, podrías intentar seguir adelante y ver si funciona bien, ya que a veces estos errores no impiden el funcionamiento del sistema.

2. **Desactivar ACPI al arrancar**:
   - Reinicia tu computadora y vuelve a acceder al BIOS.
   - Busca una opción relacionada con **ACPI** y prueba desactivarla temporalmente. Esta opción puede estar bajo "Power Management" o "Advanced".
   - Guarda los cambios y reinicia.
   
   Si el BIOS no tiene una opción para desactivar ACPI, puedes probar arrancar con una opción de kernel en la línea de comandos, como:
   - Al iniciar desde el USB, edita las opciones de arranque (normalmente presionando `e` en el menú de arranque) y agrega la línea:  
     ```bash
     acpi=off
     ```
   - Luego presiona `Ctrl + X` o `F10` para continuar el arranque con esa opción.

3. **Verificar la imagen de arranque**: Si los errores persisten y el sistema no avanza, puede haber un problema con la imagen que estás utilizando en el USB. Asegúrate de que el archivo ISO o la imagen de arranque se haya creado correctamente.

Si el problema continúa o deseas más detalles sobre cómo proceder, avísame y te guiaré.

### Usuario

No encontré en la BIOS nada relacionado con eso, estoy en este momento en la BIOS, que más puedo mejorar o optimizar en la BIOS?

### Asistente

Parece que estás en la sección de la BIOS que gestiona las configuraciones avanzadas de tu sistema. Aunque no ves una opción clara para **ACPI**, hay algunas configuraciones adicionales que puedes ajustar desde la BIOS para mejorar el rendimiento y resolver potenciales problemas de arranque:

### 1. **Optimizar características del BIOS**:
   - Entra en **Advanced BIOS Features** y verifica las siguientes configuraciones:
     - **First Boot Device**: Asegúrate de que esté configurado en **USB-HDD** (o la opción USB que funcionó antes). Esto garantizará que arranque primero desde la unidad USB.
     - **Quick Boot**: Habilita esta opción si aparece, ya que acelera el proceso de arranque al omitir algunas pruebas de hardware.
     - **USB Legacy Support**: Si encuentras esta opción en **Integrated Peripherals**, habilítala para asegurar que la unidad USB sea reconocida correctamente durante el arranque.

### 2. **Power Management Setup**:
   - Aquí podrías encontrar configuraciones relacionadas con la administración de energía que podrían afectar ACPI.
   - Busca opciones relacionadas con **ACPI Suspend Type** o **ACPI Function**:
     - Si hay una opción **ACPI Suspend Type**, configúrala en **S1 (POS)** o **S3 (STR)** dependiendo de las opciones disponibles. Esto puede mejorar la compatibilidad de ACPI.
     - Si hay una opción **ACPI Function**, asegúrate de que esté habilitada.

### 3. **Cargar valores predeterminados**:
   - Si has modificado varias configuraciones de la BIOS anteriormente y no estás seguro de los ajustes correctos, puedes intentar cargar los valores predeterminados. Esto puede corregir problemas de arranque si alguna configuración está interfiriendo con el hardware. Ve a **Load Optimized Defaults** y luego guarda los cambios.

### 4. **Revisar Periféricos Integrados**:
   - En **Integrated Peripherals**, asegúrate de que las configuraciones de **USB** estén habilitadas correctamente. Las opciones de soporte de USB 2.0 o USB 3.0 deben estar habilitadas para garantizar una mejor compatibilidad con unidades USB modernas.

### 5. **Verificar opciones de CPU y Memoria**:
   - Entra a **MB Intelligent Tweaker (M.I.T)** y asegúrate de que las configuraciones de la CPU y la memoria estén en modo **Auto**. Esto garantiza que no haya overclocking o configuraciones manuales que puedan causar inestabilidad.

Luego de ajustar estas configuraciones, intenta guardar los cambios y arrancar de nuevo desde la unidad USB. Si el problema persiste, es posible que necesitemos realizar pruebas adicionales con la configuración del kernel o la imagen de arranque.

### Usuario

Vamos por partes, esto es lo que tengo en power management setup

### Asistente

Viendo las opciones en el menú de **Power Management Setup**, te hago algunas sugerencias para optimizar el rendimiento o solucionar problemas relacionados con la energía:

### 1. **Soft-Off by Power Button**:
   - Mantén **Instant-Off**, lo que permite que el sistema se apague inmediatamente al presionar el botón de encendido. Si prefieres tener una pequeña demora antes del apagado para evitar apagados accidentales, puedes cambiarlo a **Delay 4 Sec**.

### 2. **USB Wake Up from S3**:
   - **Enabled** está bien si quieres poder despertar la computadora desde el estado de suspensión usando dispositivos USB. Esto es útil si conectas dispositivos como teclados o ratones USB y deseas que despierten el sistema. Si no utilizas esta función, puedes dejarla habilitada o deshabilitarla para un ligero ahorro de energía.

### 3. **Modem Ring Resume**:
   - **Disabled** es correcto, a menos que estés utilizando un módem antiguo que deba activar el sistema al recibir una llamada telefónica.

### 4. **PME Event Wake Up**:
   - **Enabled** está bien, ya que permite que eventos en la red o dispositivos PCI (como tarjetas de red o sonido) puedan despertar el sistema. Es útil para encender el equipo remotamente (Wake on LAN).

### 5. **HPET Support**:
   - **Enabled** es lo correcto. El **HPET (High Precision Event Timer)** mejora la precisión de los temporizadores del sistema, lo que puede mejorar el rendimiento en algunos casos, especialmente en aplicaciones multimedia o juegos.

### 6. **Power On By Mouse / Keyboard**:
   - **Disabled** está bien si no planeas usar el ratón o teclado para encender la computadora. Si te gustaría habilitar esta función, puedes hacerlo, pero consume algo más de energía en estado de suspensión.

### 7. **AC Back Function**:
   - **Soft-Off** es la configuración típica. Esto significa que si hay un corte de energía, cuando vuelva la energía, el sistema permanecerá apagado. Si prefieres que se encienda automáticamente al volver la energía, puedes cambiarlo a **Full-On** o **Previous State** (retomará el último estado antes del corte).

### 8. **ErP Support**:
   - **Disabled** está bien, ya que esta opción se usa generalmente para reducir el consumo de energía en modo de espera (standby) de acuerdo con las regulaciones europeas. Solo habilítalo si estás buscando cumplir con esas regulaciones o deseas ahorrar la máxima cantidad de energía en reposo.

### 9. **KB Power ON Password** y **Power-On by Alarm**:
   - Puedes dejarlas deshabilitadas a menos que quieras encender la PC con una contraseña en el teclado o programar un encendido automático en un día/hora específicos.

---

Estas son las configuraciones más relevantes de este menú. Si te parece bien, podemos seguir revisando las otras secciones de la BIOS para ver si hay más configuraciones que optimizar.

### Usuario

Vamos a ver en mi BIOS las opciones de integrated peripherals

### Asistente

En la sección de **Integrated Peripherals** de la BIOS, veo varias opciones relacionadas con controladores de SATA, LAN, USB y puertos integrados. A continuación te dejo recomendaciones para algunas de las opciones:

### 1. **OnChip SATA Controller**:
   - **Enabled** está bien. Esto permite que el controlador SATA de la placa base maneje los dispositivos conectados a los puertos SATA (discos duros o SSDs).

### 2. **OnChip SATA Type**:
   - Actualmente está configurado en **Native IDE**. Si estás utilizando un sistema operativo moderno (Windows 7 o superior), te recomendaría cambiarlo a **AHCI** en lugar de **IDE**. **AHCI** proporciona mejor rendimiento en unidades SATA y permite características avanzadas como **NCQ** (Native Command Queuing) y hot-swapping.

   - *Nota:* Si cambias de **IDE** a **AHCI**, y tu sistema operativo fue instalado mientras estaba en **IDE**, es posible que tengas que hacer algunos cambios en los controladores antes del cambio para evitar errores de arranque.

### 3. **OnChip SATA Port as ESP**:
   - Esto se refiere a la asignación de un puerto SATA como puerto primario. Está configurado como **Pass Through** (BSP). Puedes dejarlo así si no hay problemas de arranque o funcionamiento con tus discos SATA.

### 4. **Onboard LAN Function**:
   - **Enabled** está bien si usas el puerto Ethernet integrado para conectarte a internet o a una red local. Si no lo usas, puedes deshabilitarlo.

### 5. **Onboard LAN Boot ROM**:
   - **Disabled** está bien, a menos que necesites arrancar tu sistema desde la red mediante PXE (generalmente usado en entornos empresariales). Mantenerlo deshabilitado ahorra tiempo de arranque.

### 6. **SMART LAN**:
   - Esta opción realiza pruebas en el cable de red conectado para determinar la longitud y posibles fallos. Puedes mantenerlo habilitado si necesitas esta función. De lo contrario, desactívalo para simplificar el arranque.

### 7. **Onboard Audio Function**:
   - **Enabled** está bien si usas el audio integrado de la placa base. Si tienes una tarjeta de sonido dedicada, puedes deshabilitar el audio integrado para evitar conflictos.

### 8. **USB Controllers**:
   - **Enabled** es correcto para usar dispositivos USB. Deshabilitarlo podría hacer que los puertos USB no funcionen.

### 9. **USB Legacy Function**:
   - **Enabled** te permite usar dispositivos USB (como teclados o ratones) en sistemas operativos antiguos o durante el arranque (antes de cargar el sistema operativo). Es recomendable dejarlo habilitado para asegurar compatibilidad con BIOS y sistemas antiguos.

### 10. **USB Storage Function**:
   - **Enabled** te permite arrancar desde unidades USB. Esto es útil si necesitas iniciar desde una memoria USB para instalar un sistema operativo o realizar otras tareas. Mantenerlo habilitado es recomendable.

### 11. **Onboard Serial Port**:
   - **Enabled** es correcto si utilizas el puerto serie para algún dispositivo. Si no usas ningún dispositivo que requiera puerto serie (muy poco común hoy en día), puedes deshabilitarlo para liberar recursos.

---

Si tienes alguna otra pregunta o si necesitas ajustar más configuraciones de la BIOS, dime y seguimos revisando.

### Usuario

Vamos con PC health status (no puedo mandarte fotos)

### Asistente

Perfecto, veamos qué tipo de opciones podrías encontrar en la sección **PC Health Status** de la BIOS y te puedo orientar con base en lo que normalmente aparece allí:

### Opciones Comunes en "PC Health Status":

1. **CPU Temperature**:
   - Aquí se muestra la temperatura actual del procesador. Si está demasiado alta (más de 80°C), podrías tener problemas de sobrecalentamiento. Asegúrate de que el ventilador de la CPU esté funcionando correctamente y que haya suficiente ventilación en el gabinete.

2. **System Temperature**:
   - Esto muestra la temperatura general de la placa base. Debería estar por debajo de los 60°C. Si está muy alta, también podría ser señal de problemas de ventilación.

3. **CPU Fan Speed**:
   - Indica la velocidad del ventilador del procesador en RPM (revoluciones por minuto). Si la velocidad es muy baja o 0, podría haber un problema con el ventilador, lo que afectaría la refrigeración.

4. **System Fan Speed**:
   - Esto es similar al anterior, pero para los ventiladores del gabinete u otros conectados a la placa base. De nuevo, si es 0 o demasiado bajo, revisa los ventiladores.

5. **VCore** (Voltage Core):
   - Esta es la tensión que recibe el procesador. Los valores normales suelen estar entre 1.0V y 1.3V, dependiendo del procesador. Si es demasiado alto o bajo, podría indicar problemas con la fuente de alimentación o con la configuración de overclocking.

6. **+3.3V, +5V, +12V**:
   - Estas son las tensiones que entrega la fuente de alimentación a la placa base. Valores significativamente fuera de los rangos pueden indicar problemas con la fuente de alimentación.
   - Normalmente deberían estar cerca de estos valores:
     - **+3.3V**: entre 3.2V y 3.4V
     - **+5V**: entre 4.8V y 5.2V
     - **+12V**: entre 11.8V y 12.2V

7. **Fan Fail Warning**:
   - Si esta opción está habilitada, la BIOS emitirá una advertencia si detecta que uno de los ventiladores deja de funcionar. Es recomendable mantenerlo habilitado para prevenir problemas de sobrecalentamiento.

8. **CPU Warning Temperature**:
   - Puedes configurar una temperatura máxima para la CPU. Si el procesador supera esta temperatura, se te notificará o la computadora se apagará automáticamente para evitar daños. Usualmente se configura entre 70°C y 80°C.

9. **Smart Fan Control**:
   - Si tu sistema soporta control de ventiladores inteligente, esta opción ajusta automáticamente la velocidad del ventilador en función de la temperatura. Es recomendable habilitarlo para mantener el sistema fresco sin hacer que los ventiladores trabajen innecesariamente a máxima velocidad.

---

Revisa si tienes alguna de estas opciones o algo diferente, y dime si necesitas más detalles o recomendaciones sobre alguna configuración específica.
