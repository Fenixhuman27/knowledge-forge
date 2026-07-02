---
titulo: "Prompt para voz masculina"
fecha: 2026-05-06
mensajes: 6
origen: ChatGPT
---

# Prompt para voz masculina

### Usuario

Hola Clara, encontré la IA de meta que me generó estos vídeos (muy buenos) pero necesito un prompt que le exija que el que cante sea el hombre y no la mujer...

### Asistente

Hola Mario, ya vi por dónde viene el problema — esas IAs suelen “decidir” la voz por defecto según el estilo o el dataset, y muchas veces tiran voz femenina si no lo especificás con bastante firmeza.

La clave no es solo decir “voz masculina”, sino **forzarlo desde varios ángulos a la vez**: rol, timbre, registro, protagonista y exclusión explícita.

Te dejo un prompt ya optimizado para eso (lo podés copiar tal cual y adaptar):

---

**Prompt:**

“Music video featuring a **male lead vocalist** performing the song. The singer is a **man with a clearly masculine voice**, deep and resonant tone, expressive and emotional delivery. The **male voice is dominant and clearly audible**, leading the entire performance.

No female vocals, no female lead, no female harmonies. Only a **male singer as the main and exclusive vocalist**.

The performance should feel raw, authentic and intense, with the male singer emotionally connected to the lyrics. Cinematic lighting, realistic human expressions, and strong stage presence. The camera focuses primarily on the male vocalist while singing.”

---

Si ves que igual se “escapa” y mete voz femenina (pasa bastante), podés endurecerlo un poco más agregando al final:

“**Strict requirement: male voice only. Reject output if female voice is present.**”

---

Un detalle importante: algunas IAs responden mejor si además le marcás el tipo de voz, por ejemplo:
- “baritone male voice”
- “deep male rock voice”
- “gritty male vocal”

Eso reduce todavía más la ambigüedad.

Si querés, en el próximo paso puedo afinarte el prompt según el estilo de tu banda (tipo Nirvana / grunge / metal) para que no solo sea masculino, sino que tenga esa identidad que estás buscando.

### Usuario

No logro la escena que le pido, en la escena el está tratando de alejarse de ella (es una relación tóxica) ella lo sigue tratando de convencerlo de que se quede pero el mira hacia atrás levemente y sigue intentando alejarse (sin correr) solo como quien no quiere volver atrás... Ella lo sigue intentando convencerlo de que no se vaya!

### Asistente

Sí, te entiendo perfecto — acá el problema ya no es solo “qué” querés, sino **cómo la IA interpreta la intención emocional y la coreografía**. Si no lo guiás como si fuera dirección de cine, se queda en algo genérico tipo “discusión de pareja”.

Lo que necesitás es **bloquear la escena en acciones físicas concretas + intención emocional + comportamiento de cámara**.

Te dejo un prompt armado para forzar exactamente esa dinámica:

---

**Prompt optimizado (escena específica):**

“Cinematic scene of a toxic relationship. A man is slowly walking away from a woman, trying to leave her behind. He does not run, he walks with hesitation, as if emotionally conflicted but determined to leave.

The woman follows him closely, desperately trying to convince him to stay. She reaches toward him, talking, pleading, emotionally intense.

The man briefly turns his head slightly to look back at her, with a conflicted and pained expression, but he does not stop walking. After a short glance, he looks forward again and continues moving away.

Important: the man never turns fully around, never goes back, and never stops. His body language shows resistance and inner struggle, but clear intention to leave.

The woman becomes more emotional as she follows him, trying harder to stop him, but he keeps walking forward.

Slow pacing, realistic human behavior, subtle acting, cinematic lighting, dramatic mood. Camera follows from the side and slightly behind, capturing both characters and the emotional distance growing between them.”

---

Ahora, si querés que la IA no “rompa” la escena (que suele pasar), agregale este bloque de control:

“**Do not show reconciliation. Do not show the man stopping, hugging, or turning back. Maintain continuous forward movement away from the woman.**”

---

Un ajuste fino que suele marcar la diferencia:
Si ves que él se queda muy “duro”, podés sumar:
- “subtle hesitation in his steps”
- “slow, reluctant movement”
- “emotional restraint”

Eso le da ese aire de “me duele pero me voy igual”, que es exactamente lo que estás buscando.

---

Si querés, en el siguiente paso puedo integrarte esto con el prompt musical (voz masculina + estética grunge + narrativa) y te dejo uno solo listo para generar clips consistentes tipo videoclip profesional.

### Usuario

Por algun motivo me dice "se ha producido un error"

### Asistente

Sí, eso ya no suena a “interpretación creativa”… eso es más bien **la IA rechazando el prompt**. Y suele pasar por dos cosas:  
1) demasiado largo/estructurado  
2) palabras que el sistema interpreta como conflicto sensible (“toxic”, “desperate”, “pleading”, etc.)

Vamos a simplificarlo sin perder control.

Probá con esta versión más “amigable” para el sistema:

---

**Prompt limpio (más corto y estable):**

“Cinematic scene of a couple. A man slowly walks away from a woman. He looks slightly back at her for a moment, then continues walking forward without stopping.

The woman follows him, trying to convince him to stay, speaking emotionally and reaching toward him.

The man shows hesitation but keeps moving forward. He never turns around completely and never goes back.

Slow, realistic movement, emotional acting, natural behavior, cinematic lighting, dramatic mood. Camera follows both characters from the side.”

---

Si **igual tira error**, probá esta versión aún más neutra (esto casi siempre pasa filtros):

---

**Versión ultra segura:**

“Cinematic emotional scene. A man walks forward while a woman follows him. He briefly looks back at her, then keeps walking without stopping.

She tries to talk to him and reach him, but he continues moving away.

Natural acting, slow pacing, realistic human behavior, cinematic style.”

---

Un tip importante (esto suele ser EL problema oculto):  
👉 muchas IAs de video se rompen si das **demasiadas instrucciones negativas** (no hacer esto, no hacer aquello).  
Por eso en la segunda versión las saqué casi todas.

---

Si querés afinar más: decime qué IA de Meta estás usando (porque Meta tiene varias: Emu Video, Movie Gen, etc.), y te lo ajusto específicamente a cómo interpreta prompts ese modelo.
