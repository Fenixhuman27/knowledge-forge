---
titulo: "Revisión de prompt Genini"
fecha: 2026-06-10
mensajes: 5
origen: ChatGPT
---

# Revisión de prompt Genini

### Usuario

Hola Clara, en la app de Genini tengo mucha información dispersa entre conversaciones y quiero pedirle que me haga un resumen... Hice un prompt pero no estoy seguro si está bien hecho dime qué te parece
"Quiero que hagas una investigación profunda en todas nuestras conversaciones que mencionan a Nocturne's Wake y me generes un informe con: 
1) acciones concretas que hicimos en redes para el crecimiento de la banda
2) ideas con potencial que no sabemos si las realizamos o no. 
3) cualquier dato estadístico que tengas sobre avances en el proyecto
4) cualquier dato importante que debería tomar en consideración sobre este proyecto. "

### Asistente

El prompt no está mal, pero tiene dos problemas:

1. Le deja demasiado margen a Gemini para interpretar qué buscar.
2. No le obliga a consolidar información repetida, detectar contradicciones ni distinguir entre ideas ejecutadas y pendientes.

Si tienes muchas conversaciones dispersas, yo lo haría más parecido a una auditoría de proyecto que a una simple búsqueda.

Prueba con esto:

:::writing{variant="document" id="58241"}
Actúa como un analista de proyectos y realiza una auditoría completa de TODAS nuestras conversaciones relacionadas con Nocturne's Wake.

Tu tarea es revisar cada conversación donde se mencione el proyecto, la banda, las canciones, la estrategia de crecimiento, marketing, redes sociales, identidad visual, narrativa, videoclips, TikTok, YouTube, Spotify, imagen de marca o cualquier aspecto relacionado.

Genera un informe estructurado en las siguientes secciones:

1. ACCIONES EJECUTADAS
- Lista todas las acciones concretas que realizamos.
- Indica qué objetivo perseguía cada acción.
- Explica, si existe información disponible, qué resultados obtuvo.

2. IDEAS PENDIENTES O NO CONFIRMADAS
- Enumera todas las ideas propuestas.
- Clasifícalas por prioridad (Alta, Media, Baja).
- Indica si existe evidencia de que fueron ejecutadas o si permanecen pendientes.

3. DATOS Y MÉTRICAS DEL PROYECTO
- Reúne cualquier dato numérico, estadístico o indicador de crecimiento encontrado.
- Incluye seguidores, visualizaciones, interacciones, reproducciones, conversiones o cualquier otra métrica mencionada.
- Ordena los datos cronológicamente cuando sea posible.

4. ESTRATEGIA GENERAL IDENTIFICADA
- Resume la estrategia principal que hemos construido para el crecimiento de Nocturne's Wake.
- Identifica los pilares de contenido.
- Identifica los públicos objetivo.
- Identifica los mensajes emocionales clave.

5. ACTIVOS CREADOS
- Lista canciones, letras, historias, personajes, conceptos visuales, campañas, videos, imágenes, prompts, publicaciones y cualquier otro material desarrollado.

6. INFORMACIÓN IMPORTANTE PARA NO PERDER
- Señala decisiones estratégicas importantes.
- Señala aprendizajes obtenidos.
- Señala errores detectados.
- Señala oportunidades futuras.

7. CONTRADICCIONES O INCONSISTENCIAS
- Detecta ideas que se contradigan entre sí.
- Detecta cambios de dirección del proyecto.
- Explica cuáles parecen ser las decisiones más recientes y vigentes.

8. PLAN ACTUAL DEL PROYECTO
- Basándote en toda la información disponible, reconstruye cuál parece ser el estado actual de Nocturne's Wake.
- Indica claramente:
  • Qué ya está hecho.
  • Qué está en proceso.
  • Qué falta hacer.
  • Cuáles deberían ser los próximos pasos lógicos.

IMPORTANTE:
- No omitas información por considerarla repetida.
- Consolida elementos similares.
- Cuando tengas dudas, indica el nivel de confianza de tu conclusión.
- Prioriza la información más reciente cuando existan versiones diferentes de una misma idea.
- El objetivo es reconstruir la historia completa y el estado actual del proyecto como si estuvieras preparando un informe para un nuevo director creativo que tomará el control de Nocturne's Wake.
:::

Ese prompt tiene una ventaja importante: no solo te devuelve un resumen, sino un "estado de situación" del proyecto. Para un proyecto largo como Nocturne's Wake, eso suele ser mucho más útil que una lista de recuerdos dispersos.

### Usuario

:::writing{variant="document" id="58241"} esto es necesario ponerlo al principio? Y que significa?

### Asistente

No. Eso no forma parte del prompt.

`:::writing{variant="document" id="58241"}` es una marca interna de formato que apareció en mi respuesta. Gemini no la necesita y, de hecho, podría confundirla.

Lo que debes copiar es solamente el texto que empieza con:

"Actúa como un analista de proyectos y realiza una auditoría completa de TODAS nuestras conversaciones relacionadas con Nocturne's Wake..."

y termina en:

"...como si estuvieras preparando un informe para un nuevo director creativo que tomará el control de Nocturne's Wake."

Si quieres exprimir todavía más a Gemini, añadiría una última instrucción al final:

"Antes de generar el informe final, crea internamente una línea temporal cronológica de todos los eventos, decisiones, publicaciones, canciones, estrategias y cambios de dirección relacionados con Nocturne's Wake. Utiliza esa línea temporal para evitar omisiones y para detectar relaciones entre conversaciones separadas."

Esa frase suele mejorar mucho los resultados cuando la información está repartida entre muchos chats porque obliga al modelo a reconstruir la historia completa antes de resumirla.

En resumen: elimina la línea `:::writing{...}` y usa solo el contenido del informe. Esa línea no tiene ningún significado útil para Gemini ni para ti.

### Asistente

No. Eso no forma parte del prompt para Gemini.

`:::writing{variant="document" id="58241"}` es una instrucción interna que yo uso en ChatGPT para mostrar textos en un bloque editable especial. Gemini no entiende eso ni lo necesita.

Lo que debes copiar y pegar en Gemini es solamente esto:

"Actúa como un analista de proyectos y realiza una auditoría completa de TODAS nuestras conversaciones relacionadas con Nocturne's Wake.

Tu tarea es revisar cada conversación donde se mencione el proyecto, la banda, las canciones, la estrategia de crecimiento, marketing, redes sociales, identidad visual, narrativa, videoclips, TikTok, YouTube, Spotify, imagen de marca o cualquier aspecto relacionado.

Genera un informe estructurado en las siguientes secciones:

1. ACCIONES EJECUTADAS
- Lista todas las acciones concretas que realizamos.
- Indica qué objetivo perseguía cada acción.
- Explica, si existe información disponible, qué resultados obtuvo.

2. IDEAS PENDIENTES O NO CONFIRMADAS
- Enumera todas las ideas propuestas.
- Clasifícalas por prioridad (Alta, Media, Baja).
- Indica si existe evidencia de que fueron ejecutadas o si permanecen pendientes.

3. DATOS Y MÉTRICAS DEL PROYECTO
- Reúne cualquier dato numérico, estadístico o indicador de crecimiento encontrado.
- Incluye seguidores, visualizaciones, interacciones, reproducciones, conversiones o cualquier otra métrica mencionada.
- Ordena los datos cronológicamente cuando sea posible.

4. ESTRATEGIA GENERAL IDENTIFICADA
- Resume la estrategia principal que hemos construido para el crecimiento de Nocturne's Wake.
- Identifica los pilares de contenido.
- Identifica los públicos objetivo.
- Identifica los mensajes emocionales clave.

5. ACTIVOS CREADOS
- Lista canciones, letras, historias, personajes, conceptos visuales, campañas, videos, imágenes, prompts, publicaciones y cualquier otro material desarrollado.

6. INFORMACIÓN IMPORTANTE PARA NO PERDER
- Señala decisiones estratégicas importantes.
- Señala aprendizajes obtenidos.
- Señala errores detectados.
- Señala oportunidades futuras.

7. CONTRADICCIONES O INCONSISTENCIAS
- Detecta ideas que se contradigan entre sí.
- Detecta cambios de dirección del proyecto.
- Explica cuáles parecen ser las decisiones más recientes y vigentes.

8. PLAN ACTUAL DEL PROYECTO
- Basándote en toda la información disponible, reconstruye cuál parece ser el estado actual de Nocturne's Wake.
- Indica claramente:
• Qué ya está hecho.
• Qué está en proceso.
• Qué falta hacer.
• Cuáles deberían ser los próximos pasos lógicos.

IMPORTANTE:
- No omitas información por considerarla repetida.
- Consolida elementos similares.
- Cuando tengas dudas, indica el nivel de confianza de tu conclusión.
- Prioriza la información más reciente cuando existan versiones diferentes de una misma idea.
- El objetivo es reconstruir la historia completa y el estado actual del proyecto como si estuvieras preparando un informe para un nuevo director creativo que tomará el control de Nocturne's Wake."

Además, yo añadiría una última línea muy importante para Gemini:

"Si el informe supera el límite de respuesta, divídelo automáticamente en varias partes numeradas y continúa hasta finalizarlo."

Eso evita que te entregue un resumen recortado cuando encuentre mucha información.
