---
titulo: "Recuperación memoria USB dañada"
fecha: 2024-10-08
mensajes: 2
origen: ChatGPT
---

# Recuperación memoria USB dañada

### Usuario

Ahora quiero recuperar esta memoria USB ya que también me dice "no hay medios"
Que herramienta uso?
MPTOOLS NO LA RECONOCE 

Description: [D:] Dispositivo de almacenamiento USB (Generic USB SD Reader)
Device Type: Mass Storage Device
Protocal Version: USB 2.00
Current Speed: High Speed
al so
circuit
agina
Max Current: 500mA
USB Device ID: VID = 090C PID = 6200
Serial Number: 12345678901234567890
Device Vendor: Silicon Motion, Inc.
Device Name: Generic USB2.0 card
Device Revision: 0100
Manufacturer: Generic
Product Model: USB SD Reader
jetas
Product Revision: 1.00
SD
Laciona
Controller Vendor: SMI
Controller Part-Number: SM331~SM334

### Asistente

El mensaje "no hay medios" puede indicar un problema con la memoria USB, como una corrupción del controlador o una falla del hardware. Aquí te dejo algunas herramientas y pasos que podrías intentar para intentar recuperar la memoria USB:

### Herramientas recomendadas:

1. **ChipGenius**:
   - Es una herramienta que te ayuda a identificar el controlador interno de tu memoria USB. Con esta información, puedes buscar una herramienta específica para restaurar el firmware del controlador.
   - Si logras identificar exactamente el controlador (que parece ser de Silicon Motion), podrías buscar una herramienta de recuperación específica para ese modelo.

2. **SMI Mass Production Tool**:
   - Es una herramienta de producción masiva diseñada para unidades USB con controladores Silicon Motion. Ya que tu USB parece tener un controlador SM331~SM334, podrías intentar usar esta herramienta para restaurar el firmware.
   - Debes descargar la versión que sea compatible con el controlador específico de tu dispositivo. Dado que MPTools no la reconoce, asegúrate de tener la versión más reciente o una específica para el modelo SM331-SM334.

3. **HDD Low Level Format Tool**:
   - Esta herramienta puede realizar un formato a bajo nivel en tu memoria USB. Si el dispositivo sigue siendo reconocido por el sistema, esta herramienta podría solucionar el problema eliminando cualquier corrupción en el sistema de archivos.

4. **TestDisk**:
   - Esta herramienta es conocida por recuperar particiones y reparar sistemas de archivos dañados. Si el USB es detectado pero no muestra medios, TestDisk podría ser útil para intentar restaurar la partición dañada.

### Procedimientos:

1. **Verificar el controlador del USB** con ChipGenius para identificar si necesitas una versión más específica de una herramienta de recuperación.
2. **Intentar con SMI Mass Production Tool** si consigues la versión correcta para el controlador SM331~SM334.
3. **Utilizar HDD Low Level Format Tool** para realizar un formato a bajo nivel, lo que podría solucionar problemas de detección del medio de almacenamiento.
4. **Ejecutar TestDisk** para intentar recuperar o reparar el sistema de archivos si es que la unidad es detectada, pero no está accesible.

### Advertencia:
Recuperar una memoria USB con herramientas de reparación de firmware podría ocasionar la pérdida total de los datos almacenados. Si necesitas recuperar datos antes de restaurar el firmware, es recomendable intentar primero con herramientas de recuperación de datos como *Recuva* o *EaseUS Data Recovery*.

Si ninguno de estos métodos funciona, es probable que el dispositivo tenga un fallo físico irreparable.
