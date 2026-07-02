---
titulo: "Prompt para perspectiva hombre"
fecha: 2026-06-19
mensajes: 14
origen: ChatGPT
---

# Prompt para perspectiva hombre

### Usuario

Necesito un prompt para forzar a gémini a qué me dé una imagen desde la perspectiva del hombre la imagen debe mostrar los brazos en el teclado, la computadora y el resto de la habitación sin cambiar ningún detalle más que la perspectiva. No quiero ver las gafas ni nada, solo una imagen para la continuidad de un vídeo

### Asistente

Prueba con un prompt extremadamente específico para evitar que Gemini invente elementos o cambie el escenario:

> Usa la imagen de referencia únicamente para reconstruir exactamente el mismo entorno y momento. La nueva imagen debe estar tomada desde la perspectiva en primera persona del hombre sentado frente al escritorio (POV realista). La cámara representa sus propios ojos.
>
> Deben verse únicamente sus antebrazos y manos apoyadas sobre el controlador MIDI y el escritorio, en posición natural de trabajo. No mostrar ninguna parte de su rostro, cabeza, gafas, reflejos, sombras faciales ni ninguna parte del cuerpo por encima de los hombros.
>
> Mantener absolutamente idénticos:
>
> - La computadora portátil abierta con la misma pantalla de producción musical.
> - El controlador MIDI.
> - Los auriculares sobre el escritorio.
> - Los cables.
> - El cuaderno.
> - Los monitores de audio.
> - La estantería del fondo.
> - La iluminación cálida y tenue.
> - La atmósfera con ligera neblina/humo ambiental.
> - La distribución exacta de todos los objetos.
> - La distancia entre objetos.
> - El encuadre cinematográfico.
>
> No agregar ni quitar objetos. No reorganizar la habitación. No modernizar el equipo. No cambiar colores, iluminación ni decoración.
>
> La imagen debe parecer el fotograma siguiente de una película, como si la cámara hubiera pasado de mostrar al hombre de perfil a mostrar exactamente lo que él está viendo en ese mismo instante.
>
> Fotografía hiperrealista, lente 35 mm, profundidad de campo natural, iluminación cinematográfica real, máxima coherencia espacial, continuidad visual perfecta entre planos, sin apariencia de IA, sin deformaciones, sin elementos nuevos, sin texto, sin marcas de agua.

Si Gemini sigue cambiando cosas, añade esta línea al final:

> PRIORIDAD ABSOLUTA: preservar la continuidad visual. El escenario debe ser reconocible como la misma habitación exacta vista un segundo después desde los ojos del protagonista. Cualquier cambio en objetos, decoración, iluminación o composición se considera un error.

### Usuario

Salió perfecto (casi) ahora como le pido esto (Quiero que generes un sutil movimiento en loop donde el hombre mira el cuaderno y luego la pantalla de la computadora, mientras teclea. Movimiento sutil sin mirar a camara y sin mover el cuerpo, solo mira su cuaderno y la PC ) para que en el movimiento solo gire la cámara sutilmente hacia la izquierda (cuaderno) y vuelva al centro (laptop)?

### Asistente

El problema es que si le dices "el hombre mira el cuaderno y luego la pantalla", Gemini puede intentar animar brazos, hombros, cabeza o incluso reconstruir partes del personaje. Como ya tienes un POV perfecto, conviene describirlo como movimiento de cámara subjetiva, no como movimiento de persona.

Prueba algo así:

> Genera una animación en bucle (loop seamless) basada en esta imagen POV.
>
> La cámara representa los ojos del protagonista sentado frente al escritorio.
>
> Movimiento extremadamente sutil y natural:
>
> 1. La cámara gira lentamente unos pocos grados hacia la izquierda para observar el cuaderno.
> 2. Hace una breve pausa.
> 3. La cámara regresa suavemente al centro enfocando nuevamente la pantalla de la laptop.
> 4. La animación termina exactamente en el mismo encuadre donde comenzó para crear un loop perfecto.
>
> Mantener completamente inmóviles:
>
> - Los brazos.
> - Las manos.
> - El controlador MIDI.
> - La laptop.
> - Los auriculares.
> - Los cables.
> - La iluminación.
> - La habitación.
> - Todos los objetos del fondo.
>
> No animar al personaje. No mover la cabeza. No generar movimientos corporales. No mover las manos. No simular respiración. No cambiar la profundidad de campo.
>
> El único movimiento permitido es una suave rotación horizontal de cámara (pan) hacia la izquierda y regreso al centro.
>
> Amplitud máxima del movimiento: 5 a 10 grados.
>
> Velocidad lenta, contemplativa y realista.
>
> Estilo cinematográfico, sin efecto de cámara en mano, sin sacudidas, sin zoom, sin parallax exagerado, sin apariencia de IA.
>
> Loop perfecto.

La frase clave es:

> "El único movimiento permitido es una suave rotación horizontal de cámara (pan) hacia la izquierda y regreso al centro."

Eso obliga a Gemini a interpretar la acción como movimiento de cámara y no como movimiento del personaje.

### Usuario

No no, es a meta IA que le voy a pedir está nueva tarea

### Asistente

Para Meta AI conviene ser todavía más explícito porque suele interpretar "mirar" como mover cabeza, hombros o incluso generar una nueva escena.

Yo se lo pediría así:

:::writing{variant="standard" id="58427"}
Usa esta imagen como fotograma inicial.

Genera una animación breve en loop perfecto.

La cámara representa la vista en primera persona del protagonista sentado frente al escritorio.

NO animar al personaje.
NO mover brazos.
NO mover manos.
NO mover el cuerpo.
NO mover objetos.
NO cambiar la iluminación.
NO agregar elementos nuevos.

El único movimiento permitido es un suave giro horizontal de cámara (pan) hacia la izquierda, como si los ojos observaran brevemente el cuaderno sobre el escritorio.

Luego la cámara regresa suavemente al encuadre original centrado en la laptop.

Movimiento muy sutil: entre 5 y 10 grados de rotación horizontal.

Sin zoom.
Sin inclinación vertical.
Sin efecto handheld.
Sin vibraciones.
Sin parallax exagerado.

La animación debe terminar exactamente en el mismo encuadre en el que comienza para crear un loop continuo e imperceptible.

Mantener intacta toda la habitación, todos los objetos y la composición original.

Estilo cinematográfico realista, movimiento natural de observación, como una persona trabajando que desvía la vista un instante hacia su cuaderno y vuelve a la pantalla.
:::

Incluso eliminaría la frase "mira el cuaderno" y la reemplazaría por "la cámara gira hacia el cuaderno", porque Meta AI suele obedecer mejor instrucciones de movimiento de cámara que de comportamiento humano. Eso reduce mucho las probabilidades de que intente animar cabeza, torso o brazos.

### Usuario

Está es la imágen que generó Gémini, tu crees que este prompt (Usa esta imagen como fotograma inicial.

Genera una animación breve en loop perfecto.

La cámara representa la vista en primera persona del protagonista sentado frente al escritorio.

NO animar al personaje.
NO mover brazos.
NO mover manos.
NO mover el cuerpo.
NO mover objetos.
NO cambiar la iluminación.
NO agregar elementos nuevos.

El único movimiento permitido es un suave giro horizontal de cámara (pan) hacia la izquierda, como si los ojos observaran brevemente el cuaderno sobre el escritorio.

Luego la cámara regresa suavemente al encuadre original centrado en la laptop.

Movimiento muy sutil: entre 5 y 10 grados de rotación horizontal.

Sin zoom.
Sin inclinación vertical.
Sin efecto handheld.
Sin vibraciones.
Sin parallax exagerado.

La animación debe terminar exactamente en el mismo encuadre en el que comienza para crear un loop continuo e imperceptible.

Mantener intacta toda la habitación, todos los objetos y la composición original.

Estilo cinematográfico realista, movimiento natural de observación, como una persona trabajando que desvía la vista un instante hacia su cuaderno y vuelve a la pantalla.) servirá?

### Asistente

Sí, pero yo haría un ajuste importante.

La imagen que generó Gemini ya no es exactamente un POV humano puro. Es una especie de POV cinematográfico donde vemos parte de los brazos y las manos. Para un generador de video eso es bueno, porque le da referencias espaciales. El problema es que la frase:

> "como si los ojos observaran brevemente el cuaderno"

puede provocar que la IA intente simular una cabeza humana y aparezcan movimientos extraños en brazos o perspectiva.

Yo la reemplazaría por algo más técnico:

> Usa esta imagen como fotograma inicial.
>
> Genera una animación breve en loop perfecto.
>
> Mantén completamente inmóviles:
>
> - brazos
> - manos
> - controlador MIDI
> - laptop
> - cuaderno
> - auriculares
> - cables
> - parlantes
> - mobiliario
> - iluminación
> - humo ambiental
>
> El único movimiento permitido es un suave desplazamiento horizontal de cámara (pan).
>
> La cámara gira lentamente hacia la izquierda aproximadamente 5 grados, revelando un poco más del cuaderno.
>
> Luego regresa suavemente a la posición original centrada en la laptop.
>
> No animar personas.
> No mover manos.
> No mover dedos.
> No mover objetos.
> No generar respiración.
> No generar parpadeos.
> No generar movimiento corporal.
>
> Sin zoom.
> Sin inclinación vertical.
> Sin efecto handheld.
> Sin vibraciones.
> Sin cambios de enfoque.
>
> El último fotograma debe coincidir exactamente con el primero para crear un loop perfecto.
>
> Movimiento cinematográfico extremadamente sutil y natural.

La razón es simple: en esta escena el espectador ya entiende que está "mirando". No necesitas decirle a la IA que alguien mira algo. Cuanto menos comportamiento humano le describas y más movimiento de cámara le describas, más probabilidades hay de que Meta AI haga exactamente lo que buscas: un pequeño paneo al cuaderno y regreso a la laptop, sin inventar movimientos raros.

### Usuario

Necesito pedirle a gémini que me genere otra imagen desde la perspectiva del hombre como la anterior pero está vez viendo su cuaderno, dónde está escrito parte del texto de "Every Night Again" en formato imprenta escrito con bolígrafo de forma humana (no perfecta y bien centrada) en una estructura con indicaciones a los costados de los versos y tachones te dejo la letra para que la agregues a la indicación y la imágen de referencia para que le digas exactamente a gémini que es lo que queremos

### Asistente

Perfecto. Antes de escribir el prompt necesito que me pases la letra (o al menos el fragmento que quieres que aparezca escrito en el cuaderno).

La idea sería pedirle a Gemini algo muy específico para evitar tres problemas habituales:

1. Que escriba texto ilegible.
2. Que escriba la letra perfecta como si fuera una fuente digital.
3. Que convierta el cuaderno en una hoja limpia sin marcas de trabajo.

Cuando me pases la letra, te prepararé un prompt detallado para que Gemini genere algo así:

- Misma habitación exacta.
- Misma iluminación.
- Misma perspectiva POV del compositor.
- Cámara ligeramente inclinada hacia abajo mirando el cuaderno.
- Brazos y manos visibles igual que en la imagen anterior.
- Cuaderno ocupando gran parte del encuadre.
- Letra manuscrita con bolígrafo.
- Correcciones, flechas, palabras tachadas.
- Indicaciones tipo:
  - "Verse 1"
  - "Pre-Chorus"
  - "Chorus"
  - "más fuerte"
  - "doblar voz"
  - "armonía"
  - "guitarras aquí"
- Escritura humana imperfecta.
- Márgenes desordenados.
- Aspecto de una hoja de trabajo real de composición musical.

Envíame la letra de "Every Night Again" y te redacto el prompt completo optimizado para Gemini.

### Usuario

Velvet shadows on the floor
Candlelight behind your eyes
Every time you close that door
I forget what's wrong or right

Leather skin and broken halos
Whiskey breathing on your neck
You said nothing but I knew it
This was something to regret

Fingernails across my back
Like a promise made of fire
Every touch just pulling deeper
Into something like desire

I told myself this time I'd walk away

You are the poison I come back to
Every night again
Every scar you leave on my body
Pulls me in

You are the poison I come back to
And I know it's true

Every time I try to leave you
I fall into you

Six hours lost inside the darkness

Every warning slowly breaking
Every reason almost gone
Your voice moving through the shadows
Like a secret on my skin
Every time I think it's over
We begin again

It's hiding all the sins in fire.
Hiding all the sins in flame.
Like you and I are getting lighted again.
I fall into you.

### Asistente

Con esa letra, yo evitaría pedirle a Gemini que escriba TODA la canción. Los generadores de imágenes suelen cometer errores cuando hay mucho texto. Funciona mucho mejor si muestras una página de trabajo realista con fragmentos visibles, anotaciones y partes incompletas.

Este prompt está pensado específicamente para mantener la continuidad con la imagen que ya generaste:

:::writing{variant="standard" id="58142"}
Usa como referencia la imagen POV anterior del estudio musical.

Genera una nueva imagen desde la misma perspectiva en primera persona del compositor sentado frente al escritorio.

La cámara ha bajado ligeramente y ahora está enfocando principalmente el cuaderno sobre la mesa.

Mantener exactamente el mismo estudio, la misma iluminación cálida, la misma laptop, el mismo controlador MIDI, los mismos cables, auriculares, monitores y fondo.

Deben verse los antebrazos y manos del compositor en una posición natural de trabajo.

El cuaderno debe ocupar una parte importante de la imagen.

En el cuaderno hay una hoja de trabajo real de composición musical escrita a mano con bolígrafo negro.

La escritura debe ser humana, imperfecta, ligeramente desalineada, con diferentes tamaños de letra, pequeños errores, palabras corregidas, flechas, notas al margen y algunos tachones.

NO debe parecer texto generado por computadora ni una tipografía perfecta.

Estructura visual de trabajo de composición:

[Verse 1]
Velvet shadows on the floor
Candlelight behind your eyes
Every time you close that door
I forget what's wrong or right

→ softer vocal
→ add reverb

[Verse 2]
Leather skin and broken halos
Whiskey breathing on your neck
You said nothing but I knew it
This was something to regret

↗ build tension

[Chorus]
You are the poison I come back to
Every night again
Every scar you leave on my body
Pulls me in

You are the poison I come back to
And I know it's true

Every time I try to leave you
I fall into you

★ stronger guitars
★ double vocal

Algunas líneas deben estar parcialmente tachadas.
Algunas palabras deben estar rodeadas con círculos.
Deben existir flechas conectando ideas y notas de producción en los márgenes.

Aspecto de cuaderno usado durante una sesión real de composición de rock alternativo.

Fotografía hiperrealista.
Profundidad de campo natural.
Sin apariencia de IA.
Sin texto perfectamente alineado.
Sin caligrafía artística.
Debe parecer una página auténtica escrita por un músico mientras trabaja en una canción.
:::

Si el objetivo es un video, incluso te recomendaría mostrar solamente el verso 1 y el estribillo. La IA tendrá muchas más probabilidades de escribirlo correctamente y el espectador no tendrá tiempo de leer una página completa de todos modos.

### Usuario

Ahora un prompt que le diga que con un movimiento sutil (sin cambiar nada) tache donde dice verso 1 solo eso en un movimiento leve y lento

### Asistente

Yo sería extremadamente específico para que el modelo no intente reescribir el cuaderno entero ni mover las manos.

:::writing{variant="standard" id="58491"}
Usa esta imagen como fotograma inicial.

Genera una animación corta y realista.

Mantén absolutamente inmóviles:

- la cámara
- las manos
- los brazos
- el bolígrafo
- el cuaderno
- la laptop
- el controlador MIDI
- los auriculares
- los cables
- la iluminación
- el fondo
- todos los objetos de la escena

NO cambiar el encuadre.
NO mover la cámara.
NO mover los dedos.
NO reescribir el texto.
NO modificar ninguna palabra existente.

La única acción permitida es la aparición gradual de una línea de bolígrafo negro que tacha lentamente el texto "[Verse 1]".

La línea debe dibujarse de forma natural, como si acabara de hacerse con el mismo bolígrafo que está en la escena.

Movimiento muy lento y sutil.

La línea comienza en el lado izquierdo de "[Verse 1]" y avanza suavemente hacia la derecha hasta completar el tachado.

No tachar ninguna otra palabra.

No agregar notas nuevas.

No eliminar texto.

No modificar el resto de la página.

Al finalizar la animación, solamente "[Verse 1]" debe quedar tachado con una única línea imperfecta de tinta negra.

Estilo hiperrealista, cinematográfico, sin artefactos de IA.
:::

Incluso añadiría una frase final muy importante:

> "La animación debe parecer una fotografía estática donde únicamente aparece una nueva marca de bolígrafo sobre el papel."

Eso suele ayudar mucho a que la IA no empiece a mover manos, cuaderno o cámara.
