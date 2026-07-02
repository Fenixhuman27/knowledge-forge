---
titulo: "Prompt para Meta IA"
fecha: 2026-05-06
mensajes: 11
origen: ChatGPT
---

# Prompt para Meta IA

### Asistente

Está bueno lo que querés hacer, pero hay un punto importante: ese tipo de IA (como Meta AI) suele ser bastante estricta con canciones con derechos de autor. Pedirle directamente que use *“Nocturne's Wake - Every Night Again”* puede ser justamente lo que te está generando el error.

La forma de sortear eso no es “forzar más el prompt”, sino hacerlo más inteligente: describir la canción sin nombrarla explícitamente, o indicar que sincronice labios con “audio proporcionado” o “canción cargada”.

Te dejo un prompt optimizado, listo para copiar y pegar, enfocado a lo que querés (máxima duración, realismo, lipsync y uso de imagen):

---

**PROMPT:**

"Use the provided reference image as the main subject. Animate the character into a highly realistic performance scene, maintaining facial identity and details.

Create a cinematic, emotionally intense singing performance. The character should be singing a melancholic alternative rock song with deep emotional expression, subtle head movement, natural breathing, and highly accurate lip synchronization.

Ensure ultra-realistic lip sync matching the vocals perfectly, including micro-expressions, jaw movement, and timing precision.

The scene should feel immersive and atmospheric, with soft dynamic lighting, slight camera movement, and a natural environment (concert stage or intimate setting).

Extend the animation for the maximum duration allowed.

Use the provided audio track for synchronization.

Prioritize realism, smooth motion, and emotional authenticity over stylization."

---

Si ves que todavía falla, podés probar una variante más directa:

- En vez de “use the provided audio track” → “sync lips to the uploaded audio”
- O incluso: “generate singing synchronized to background music”

Si querés, en el siguiente paso te hago una versión más agresiva todavía (tipo “hack prompt”) para empujar al modelo a que no falle, o una versión más artística según el estilo de tu banda.

### Usuario

hola clara, acabo de encontrar meta IA, me genera videos muy buenos con sincronizacion de labios y gratis... no necesito videos largos si no videos... necesito un buen prompt para que cante every nigth again pero solo animar la escena el maximo de tiempo en el prompt debes pedirle que use la imagen de referencia y que agregue la cancion ( Nocturne's Wake - Every night again) y que genere sincronizacion de labios

### Asistente

Perfecto, entonces vamos a lo importante: calidad y realismo de la escena.  
Si ya te lo generó pero “no quedó bien”, casi seguro el problema está en tres cosas: **lipsync poco preciso, falta de microexpresiones y animación demasiado genérica**.

Te dejo un prompt mucho más afinado, pensado para exprimir al máximo ese tipo de IA 👇

---

**PROMPT OPTIMIZADO (nivel alto):**

"Use the provided reference image as the exact facial and character base. Preserve identity, facial structure, and skin details with hyper-realistic accuracy.

Animate a cinematic close-up to medium shot of the character performing an emotional alternative rock song. The performance must feel raw, intimate, and authentic.

Apply ultra-precise lip synchronization to the provided song “Nocturne's Wake - Every Night Again”, matching every phoneme, breath, and pause. Lips, jaw, tongue, and cheeks must move naturally and in perfect timing with the vocals.

Incorporate subtle micro-expressions: tension in the eyes, slight brow movement, emotional blinking, and natural facial muscle dynamics. Avoid robotic or repetitive motion.

Add realistic head movement driven by emotion (not looping): slight turns, micro nods, and natural posture shifts.

Simulate real breathing: chest and shoulders should subtly move in sync with singing intensity.

Use cinematic lighting (soft shadows, moody tones), shallow depth of field, and slight handheld camera movement for realism.

Avoid exaggerated gestures, avoid looping animations, avoid artificial smoothness. Prioritize imperfection and human realism.

Enhance skin texture, light reflections, and natural imperfections (pores, subtle asymmetry).

Extend the animation to the maximum duration allowed.

Final output must feel like a real recorded performance, not AI-generated."

---

Te explico rápido por qué este funciona mejor (esto es clave para que lo ajustes vos después):

- “**every phoneme**” → obliga a mejorar el lipsync (si no lo ponés, lo hace aproximado)
- “**micro-expressions + breathing**” → esto es lo que hace que deje de parecer IA
- “**avoid looping / avoid artificial smoothness**” → corta ese efecto robótico típico
- “**imperfection and asymmetry**” → paradójicamente, hace que se vea más real

Si querés dar un paso más (nivel pro), decime qué estilo tiene tu vocalista (más tipo entity["musical_artist","Kurt Cobain","Nirvana singer"], entity["musical_artist","Eddie Vedder","Pearl Jam singer"] o algo más moderno) y te lo ajusto para que la actuación tenga esa personalidad exacta.

### Usuario

tranquila ya lo hizo para mi pero no quedo muy bien, por eso te pido un prompt optimizado pero por el tema de los derchos no te preocupes

### Asistente

Se puede intentar, pero te marco algo de frente: **continuidad perfecta cuadro a cuadro es difícil** en estas IAs. No tienen “memoria real” del clip anterior; reconstruyen. Aun así, si les das suficientes anclas (último frame + instrucciones muy específicas), podés lograr algo que *parezca* continuidad.

La clave es tratar el último fotograma como si fuera el “estado inicial” obligatorio.

Te dejo un prompt bien afinado para eso:

---

**PROMPT CONTINUACIÓN (ALTAMENTE ESPECÍFICO):**

"Continue the previous video seamlessly from the exact last frame provided. Use the last frame image as the initial state and maintain absolute continuity in character position, facial expression, lighting, camera angle, and environment.

Do not reset or reinterpret the scene. The animation must feel like a direct continuation, not a new generation.

Keep the same emotional intensity, posture, and performance energy from the final moment of the previous clip.

Resume the song “Nocturne's Wake - Every Night Again” from the exact next timestamp, ensuring perfect lip synchronization continuity (no restart, no mismatch in timing).

Maintain identical lighting conditions, shadows, depth of field, and camera behavior (including any subtle movement already present).

Preserve micro-expressions and breathing patterns, continuing naturally as if no cut occurred.

Avoid any jumps, cuts, or visual inconsistencies between clips.

Extend the performance for the maximum duration allowed.

Final result must feel like a single uninterrupted recording."

---

Ahora, truco importante (esto hace MUCHA diferencia):

- Exportá una **captura del último frame** del video anterior y usala como *reference image*  
- Si podés, subí también el mismo video anterior como contexto (algunas IAs lo usan internamente aunque no lo digan)
- Si la herramienta lo permite, agregá algo tipo:  
  **“continuation seed / preserve seed / temporal consistency”**

Si ves que igual corta raro, hay un “hack” más fino:  
pedirle que haga **0.5–1 segundo de overlap** (repita un poquito del final anterior) y después continúe. Eso disimula muchísimo los saltos al unir clips.

Si querés, en el siguiente paso te armo un flujo completo tipo “producción musical por clips” para que puedas hacer toda la canción como si fuera un solo video sin cortes visibles.

### Usuario

quedo genial, podriamos pedirle muy especificamente que haga la contunacion de ese mismo video exactamente donde quedo para darle continuidad a la cancion y si es posible tiempo mas extendido?+

### Asistente

Sí… eso pasa más de lo que debería 😅  
Cuando le pedís “continuar exactamente”, muchas IAs entran en modo seguro y **replican el mismo clip** en vez de avanzar. Es como si entendieran “mantener todo igual” literalmente.

La forma de destrabarlo es cambiar el enfoque: no pedir “continuar igual”, sino **forzar avance temporal explícito** + mantener coherencia.

Probá este prompt, que corrige justo ese problema:

---

**PROMPT CONTINUACIÓN CORREGIDO (ANTI-REPETICIÓN):**

"Use the provided last frame as the starting point of the animation.

This is a continuation, not a repetition. Do NOT recreate the previous segment.

Advance the performance forward in time from this exact moment. The character must continue singing the next part of the song “Nocturne's Wake - Every Night Again” (next unseen segment), with accurate lip synchronization to the following lyrics.

Maintain the same identity, lighting, camera angle, and environment, but introduce natural progression in motion and expression.

Facial expression, head position, and body posture must evolve naturally from the starting frame (no reset, no looping).

Add subtle new movements: slight head turns, breathing shifts, emotional changes, and progressive performance intensity.

Ensure lip sync corresponds to new vocals, not previously generated audio timing.

Avoid repeating gestures, avoid reusing animation patterns, avoid static performance.

Keep cinematic realism, micro-expressions, and natural imperfections.

Extend the animation to maximum duration allowed.

Final result must clearly feel like the NEXT segment of the same performance, not a duplicate."

---

El cambio clave está en estas ideas:

- “**next unseen segment**” → lo obliga a avanzar  
- “**not a repetition**” → rompe el bucle  
- “**evolve naturally**” → evita que congele o reinicie  
- “**new vocals timing**” → mata el lipsync reciclado

Si aún así insiste en repetir, hay un plan B más técnico (y bastante efectivo):  
en vez de “continuar”, pedile algo como:

> “start a new segment immediately after a previous performance moment, continuing the same scene…”

Suena parecido, pero cambia cómo lo interpreta internamente.

Si querés, lo siguiente que podemos hacer es pulir cómo unir los clips sin cortes visibles (eso ya es más edición que prompt, pero te puede dejar un resultado muy pro).

### Usuario

mmmmm me genero exactamente el mismo video

### Asistente

Probablemente es lo más práctico. A veces estas herramientas tienen un límite bastante rígido en continuidad temporal y, por más prompt ninja que uno les tire, hacen cosplay de loro y repiten lo mismo.

Si el clip quedó bueno, mejor capitalizar eso en vez de pelearte tres horas con una IA terca.

Podés reutilizarlo de forma inteligente para que no parezca repetido:
- cortar el mismo clip en 2–3 fragmentos distintos (inicio, medio, primer plano)
- hacer zoom lento digital en una versión
- invertir horizontalmente una copia (si no hay elementos raros que delaten)
- pasar una parte en blanco y negro o con grading distinto
- alternar con imágenes estáticas de la banda, letras o close-ups

Así el mismo material parece parte de un video musical editado, no un loop reciclado.

Por ejemplo, una estructura simple:
1. 0–8s clip normal  
2. 8–14s zoom lento + contraste más alto  
3. 14–18s imagen estática o lyric screen  
4. vuelve clip desde otro recorte

Muchos videoclips indie sobreviven con menos material que eso, créeme.

¿Lo querés publicar como reel/TikTok/short o es más para mostrar la canción en general? Porque según dónde vaya, conviene editarlo distinto.

### Asistente

Tiene sentido. Después de tres intentos, seguir empujando probablemente te haga perder tiempo para mejoras marginales.

Eso suele pasar porque algunas de esas herramientas generan a partir de una representación fija de la referencia y, cuando detectan demasiadas restricciones de continuidad, “colapsan” al resultado que ya saben producir. No es que el prompt esté mal; es una limitación del modelo.

Y siendo prácticos: si el clip quedó bueno, mejor aprovecharlo.

Tenés varias formas de usarlo sin que se note repetitivo:

Podés convertirlo en un recurso estilístico. Repetir el mismo plano en una canción melancólica/alternativa puede sentirse intencional, casi hipnótico, como esos videoclips minimalistas donde la carga está en la canción.

Algunas ideas:

— usar el clip una vez normal y otra con zoom lento digital  
— invertirlo horizontalmente en una repetición  
— segunda pasada en cámara lenta (90–95%)  
— aplicar recorte distinto (close-up vs plano medio)  
— meter un fade a negro breve entre loops  
— superponer grano, destellos o ligera vibración de cámara en una repetición  
— alternarlo con letras en pantalla

Para una canción como *Every Night Again*, incluso un loop bien tratado puede sumar esa sensación obsesiva/circular que pega con una vibra nocturna y emocional.

A veces pelearse con la IA para sacar “el clip perfecto” termina drenando energía que conviene poner en el conjunto: portada, narrativa visual, publicación, gancho para redes.

Si querés destrabar creatividad, contame cómo quedó la escena (qué hace el personaje, iluminación, encuadre, expresión) y pensamos cómo convertir esa limitación en una estética deliberada.

### Usuario

ok olvidemos esto, me repite por tercera vez el mismo video... lo dejamos asi y lo usamos asi
