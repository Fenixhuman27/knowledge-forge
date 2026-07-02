---
titulo: "Crear Game Stick USB"
fecha: 2025-02-02
mensajes: 10
origen: ChatGPT
---

# Crear Game Stick USB

### Usuario

Hace un tiempo salieron unos pendrive con juegos llamados Game stick con 20.000 juegos! Si bien hay tutoriales en Youtube de como hacerlo con un pendrive común y usarlo en la PC, prefiero que me expliques de una forma más sencilla como hacer mi propio Game stick con un pendrive común!

### Asistente

Para hacer tu propio *Game Stick* con un pendrive común y jugar en la PC de forma sencilla, lo mejor es instalar un sistema de emulación portátil. Te explico cómo hacerlo paso a paso sin complicaciones.  

### **Lo que necesitas**  
✅ Un pendrive de al menos **32GB** (mejor si es de 64GB o más).  
✅ Un PC con Windows.  
✅ Un software de emulación como **Batocera** o **RetroBat**.  
✅ Juegos (*ROMs*), que puedes buscar en internet (asegúrate de usar juegos de dominio público o respaldos de los que ya posees).  

---

### **Paso 1: Descargar Batocera o RetroBat**  
Puedes elegir entre dos opciones:  
🔹 **Batocera**: Se instala en el pendrive y funciona como un sistema operativo independiente.  
🔹 **RetroBat**: Se instala en Windows y permite jugar desde el pendrive sin necesidad de reiniciar la PC.  

**Descargas:**  
- [Batocera](https://batocera.org/download)  
- [RetroBat](https://retrobat.org/download.html)  

---

### **Paso 2: Instalar el sistema en el pendrive**  
🔹 **Si elegiste Batocera:**  
1. Descarga Batocera y un programa llamado *Rufus* o *Balena Etcher*.  
2. Conéctate el pendrive y usa Rufus o Balena Etcher para "flashear" Batocera en él.  
3. Cuando termine, reinicia la PC y entra en la BIOS (presiona F2, F12 o Supr al encender).  
4. Selecciona arrancar desde el pendrive.  

🔹 **Si elegiste RetroBat:**  
1. Descarga RetroBat y descomprímelo directamente en el pendrive.  
2. Dentro del pendrive, abre la carpeta de RetroBat y ejecuta *retrobat.exe*.  

---

### **Paso 3: Añadir Juegos (ROMs)**  
1. En el pendrive, busca la carpeta **ROMs** dentro de Batocera o RetroBat.  
2. Copia los juegos (ROMs) en las carpetas correspondientes (Ej: juegos de SNES en *snes*, juegos de PS1 en *psx*).  
3. Si usas Batocera, al iniciar el sistema en el pendrive, este escaneará los juegos automáticamente.  
4. Si usas RetroBat, abre el programa y detectará los juegos de inmediato.  

---

### **Paso 4: Conectar y Jugar**  
1. Si usas Batocera, solo necesitas arrancar desde el pendrive en la BIOS.  
2. Si usas RetroBat, solo abre *retrobat.exe* y elige un juego.  
3. Conecta un joystick USB o usa el teclado.  

---

### **Extras**  
✅ Puedes mejorar la interfaz bajando carátulas y descripciones para los juegos dentro del menú de Batocera o RetroBat.  
✅ Si quieres jugar en una Smart TV, Batocera permite usarlo con una Raspberry Pi o mini PC.  
✅ También puedes instalar emuladores manualmente en el pendrive, pero Batocera y RetroBat ya traen muchos configurados.  

---

Esta es la forma más sencilla de hacer un *Game Stick* con un pendrive y usarlo en la PC sin complicaciones. ¿Quieres que te ayude con algo más?

### Usuario

Ya tengo en mi pendrive retrobat, como puedo usarlo en mi Xiaomi tv box?

### Asistente

Para usar **RetroBat** en tu **Xiaomi TV Box**, hay un problema: **RetroBat solo funciona en Windows** y los TV Box con Android no pueden ejecutarlo directamente. Pero hay una solución: instalar un emulador en el TV Box y usar el pendrive solo para almacenar los juegos.  

---

### **Opción 1: Instalar RetroArch en la Xiaomi TV Box** (Recomendada)  
1. **Descarga RetroArch** desde la Play Store de tu Xiaomi TV Box.  
2. **Conecta el pendrive** con RetroBat y los juegos a la TV Box.  
3. **Abre RetroArch** y ve a *Load Content (Cargar contenido)*.  
4. Busca el pendrive y selecciona el juego que quieras jugar.  
5. RetroArch usará el emulador adecuado automáticamente.  

🔹 **Ventajas**: Soporta muchos sistemas y es fácil de usar.  
🔹 **Desventaja**: No tiene la interfaz de RetroBat, pero sigue siendo funcional.  

---

### **Opción 2: Instalar un Launcher como Dig o Pegasus Frontend**  
Si quieres una interfaz parecida a RetroBat:  
1. **Instala DIG o Pegasus Frontend** desde la Play Store.  
2. **Configura la app** para que detecte las ROMs en el pendrive.  
3. **Asigna los emuladores** (puedes usar RetroArch o emuladores individuales como PPSSPP para PSP o Mupen64 para N64).  
4. **Explora y selecciona un juego** para jugar con una interfaz amigable.  

---

### **Opción 3: Usar Emuladores Individuales**  
Si prefieres no usar RetroArch, puedes instalar emuladores individuales para cada consola:  
- **NES, SNES, GBA** → Nostalgia.NES, SNES9x, My Boy!  
- **PlayStation 1** → ePSXe o DuckStation  
- **PlayStation 2** → AetherSX2  
- **Nintendo 64** → Mupen64Plus  
- **PSP** → PPSSPP  

Después, solo abre cada emulador y carga los juegos desde el pendrive.  

---

### **Conclusión**  
No puedes ejecutar **RetroBat directamente** en tu Xiaomi TV Box, pero puedes usar **RetroArch** o emuladores individuales para jugar los juegos del pendrive sin problemas.  

Si necesitas ayuda con la configuración de RetroArch o algún emulador en particular, dime y te guío paso a paso.

### Usuario

Existe alguna forma de jugar juegos arcade en mi tv box?

### Asistente

Sí, puedes jugar juegos arcade en tu **Xiaomi TV Box** sin problemas usando emuladores. La mejor opción es instalar **RetroArch** o **MAME4droid**, que están en la Play Store y son compatibles con la mayoría de los juegos arcade.  

---

### **Opción 1: Usar RetroArch (Recomendada)**  
**RetroArch** es un emulador todo-en-uno que puede correr juegos de arcade y muchas otras consolas.  

🔹 **Pasos para instalar y configurar RetroArch en la Xiaomi TV Box:**  
1. **Descarga RetroArch** desde la Play Store.  
2. **Conecta un pendrive o memoria USB** con tus juegos arcade (*ROMs*).  
3. **Abre RetroArch** y ve a *Load Core (Cargar núcleo)*.  
4. **Descarga el núcleo de MAME o FBNeo**, que son los que emulan juegos arcade.  
5. **Ve a Load Content (Cargar contenido)**, selecciona tu pendrive y elige un juego.  

🔹 **Ventajas**  
✔ Soporta muchos juegos arcade clásicos y modernos.  
✔ Puedes conectar un control Bluetooth.  
✔ Compatible con pantallas grandes y filtros gráficos.  

---

### **Opción 2: Usar MAME4droid (Más fácil)**  
Si solo quieres juegos arcade y sin tanta configuración, **MAME4droid** es una excelente opción.  

🔹 **Pasos para usar MAME4droid:**  
1. Descarga **MAME4droid** desde la Play Store.  
2. Conecta tu pendrive con los juegos arcade (*ROMs* en formato .zip).  
3. Abre MAME4droid y configura la carpeta de juegos (elige el pendrive).  
4. Selecciona un juego y empieza a jugar.  

🔹 **Ventajas**  
✔ Fácil de configurar.  
✔ Compatible con miles de juegos arcade.  
✔ Se puede jugar con control Bluetooth o teclado.  

---

### **Opción 3: Emuladores individuales para ciertos juegos**  
Si solo quieres jugar juegos específicos, hay emuladores independientes:  
- **FBNeo**: Más rápido que MAME para juegos de lucha como *Street Fighter II*.  
- **FinalBurn Alpha (FBA)**: Funciona bien con juegos de Neo Geo y Capcom.  

---

### **Conclusión**  
Si quieres la mejor experiencia con arcade en tu Xiaomi TV Box:  
✅ **RetroArch** si quieres un sistema completo.  
✅ **MAME4droid** si solo buscas arcade fácil y rápido.  
✅ **Emuladores individuales** si solo te interesan juegos específicos.  

Si quieres ayuda configurando uno de estos, dime y te guío paso a paso.

### Usuario

Tengo problemas para ejecutar algunos juegos en retrobat!

### Asistente

Si algunos juegos no funcionan en **RetroBat**, puede ser por varias razones. Aquí te dejo las causas más comunes y cómo solucionarlas.  

---

### **1️⃣ Verifica que las ROMs sean compatibles**  
🔹 Algunos emuladores requieren un **formato específico** de ROMs.  
🔹 Si estás usando juegos de arcade (MAME), muchas veces necesitan **archivos adicionales (BIOS o CHD)**.  

**Solución:**  
✅ **Busca ROMs compatibles** con el emulador que estás usando en RetroBat.  
✅ Para arcade, usa ROMs del **set de MAME correcto** (Ejemplo: si usas MAME 0.239, las ROMs deben ser de esa versión).  

---

### **2️⃣ Instala o actualiza las BIOS**  
Algunos juegos requieren **archivos BIOS** para funcionar (PS1, PS2, Dreamcast, etc.).  

**Solución:**  
✅ Busca las BIOS necesarias y colócalas en la carpeta:  
📂 `RetroBat/bios/`  

🔹 Algunos ejemplos de BIOS necesarias:  
- **PlayStation 1** → `scph1001.bin`  
- **PlayStation 2** → `PS2 BIOS`  
- **Sega Dreamcast** → `dc_boot.bin` y `dc_flash.bin`  

🔹 Luego, en RetroBat:  
- Ve a *Ajustes* → *Emulación* → *Ruta de BIOS* y verifica que las detecta.  

---

### **3️⃣ Cambia el emulador (Core) en RetroBat**  
A veces un emulador no es compatible con un juego en particular.  

**Solución:**  
✅ Prueba otro emulador (core) en RetroBat:  
1. Abre RetroBat.  
2. Ve a *Ajustes de juego* y selecciona el juego problemático.  
3. Cambia el núcleo (core) del emulador y prueba.  

🔹 Ejemplo:  
- Para **PlayStation 1**, prueba entre *DuckStation* o *Beetle PSX*.  
- Para **MAME (Arcade)**, prueba *MAME*, *FBNeo* o *FinalBurn Alpha*.  

---

### **4️⃣ Configura correctamente los controles**  
Algunos juegos pueden no responder porque el control no está bien configurado.  

**Solución:**  
✅ Ve a *Ajustes de controles* en RetroBat y verifica que tu mando está correctamente asignado.  

---

### **5️⃣ Verifica si la ROM está dañada**  
Si una ROM no arranca o se cierra, puede estar corrupta.  

**Solución:**  
✅ Prueba la misma ROM en otro emulador (como RetroArch) para ver si funciona.  
✅ Descarga la ROM desde otra fuente confiable.  

---

Si me dices qué juegos o sistemas te están dando problemas, te ayudo a solucionarlo más rápido.

### Usuario

Cuál es el mejor lugar para descargar roms para retrobat?

### Asistente

​Para disfrutar de tus juegos retro en **RetroBat**, es esencial obtener las ROMs de fuentes confiables y seguras. A continuación, te presento algunas de las mejores opciones:

:::contextList
【{"image_fetch": "Logo de WowRoms"}】
**WowRoms**  
Ofrece una amplia colección de ROMs para diversas consolas y sistemas. Destaca por su interfaz intuitiva y la ausencia de anuncios invasivos. Además, la página está completamente en español, facilitando la navegación. citeturn0search3
:::

:::contextList
【{"image_fetch": "Logo de Retrostic"}】
**Retrostic**  
Cuenta con más de 70,000 juegos para más de 40 consolas. Proporciona enlaces de descarga directa sin archivos ejecutables, virus ni anuncios molestos. Si no encuentras un juego específico, puedes solicitarlo y lo añadirán rápidamente. citeturn0search7
:::

:::contextList
【{"image_fetch": "Logo de CoolROM"}】
**CoolROM**  
Es una opción popular que ofrece una amplia gama de ROMs para diversas plataformas. Aunque la cantidad de anuncios puede ser molesta, su vasta colección y la presencia de emuladores en el sitio lo convierten en una opción completa. citeturn0search3
:::

:::contextList
【{"image_fetch": "Logo de Gamulator"}】
**Gamulator**  
Ofrece una amplia colección de ROMs y emuladores para diversas plataformas. Su interfaz es sencilla y eficaz, aunque contiene algunos anuncios no intrusivos. citeturn0search3
:::

:::contextList
【{"image_fetch": "Logo de Internet Archive"}】
**Internet Archive**  
Es una biblioteca digital que alberga una amplia gama de software antiguo, incluyendo ROMs de juegos retro. Aunque su navegación puede no ser tan intuitiva, es una fuente valiosa para preservar la historia digital. citeturn0search3
:::

**Nota Importante:** La descarga de ROMs debe realizarse de manera legal y ética. Asegúrate de poseer una copia física del juego o verificar que el juego sea de dominio público antes de descargarlo. La distribución no autorizada de ROMs puede infringir derechos de autor.

Si necesitas más información o ayuda adicional, no dudes en preguntar.
