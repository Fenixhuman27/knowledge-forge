"""
Content Classifier (Bibliotecario)

Plugin del Knowledge Cognition Engine (KCE).
Lee el CONTENIDO completo de una conversacion (no solo el titulo) y
usa IA local (Ollama) para determinar que tipo(s) de contenido
valioso contiene, sin importar de que empezo hablando la conversacion.

Categorias:
  - letra_cancion: contiene letras o borradores de canciones
  - prompt_imagen: contiene prompts para generar imagenes con IA
  - arte_conceptual: describe conceptos visuales, estilos, portadas
  - estrategia: contiene planes o estrategias (marketing, crecimiento, etc.)
  - borrador: contiene un texto/documento en construccion (no cancion)
  - musica_general: relacionado a musica pero no entra en las anteriores
  - otro: no tiene relacion con el proyecto musical
"""

from src.kce.pipeline import Plugin
from src.kce.schema import NormalizedConversation, AnalysisResult
from src.kce.ollama_client import preguntar_a_ollama

CATEGORIAS = [
    "letra_cancion",
    "prompt_imagen",
    "arte_conceptual",
    "estrategia",
    "borrador",
    "musica_general",
    "otro",
]

LONGITUD_MAXIMA_TEXTO = 3000

PROMPT_BASE = """Vas a leer el contenido de una conversacion entre una persona
y un asistente de IA. Tu tarea es clasificar el contenido segun estas categorias
posibles (puede aplicar mas de una, o ninguna):

- letra_cancion: contiene letras o borradores de canciones
- prompt_imagen: contiene prompts para generar imagenes con IA
- arte_conceptual: describe conceptos visuales, estilos, portadas de disco
- estrategia: contiene planes o estrategias (marketing, crecimiento, redes)
- borrador: contiene un texto o documento en construccion (no cancion)
- musica_general: relacionado a musica o a una banda, pero no entra en las anteriores
- otro: no tiene relacion con un proyecto musical

Responde UNICAMENTE con los nombres de categoria que apliquen, separados por
coma, sin explicaciones. Ejemplo de respuesta valida: letra_cancion, musica_general

Titulo: {titulo}

Contenido:
{contenido}

Categorias:"""


class ContentClassifier(Plugin):
    nombre = "content_classifier"

    def _construir_texto(self, conversacion: NormalizedConversation) -> str:
        texto = "\n".join(m.texto for m in conversacion.mensajes if m.autor == "user")
        return texto[:LONGITUD_MAXIMA_TEXTO]

    def analizar(self, conversacion: NormalizedConversation) -> AnalysisResult:
        contenido = self._construir_texto(conversacion)

        if not contenido.strip():
            return AnalysisResult(plugin=self.nombre, conversacion_id=conversacion.id, hallazgos=[])

        prompt = PROMPT_BASE.format(titulo=conversacion.titulo, contenido=contenido)

        try:
            respuesta = preguntar_a_ollama(prompt)
        except Exception as e:
            print(f"ERROR clasificando '{conversacion.titulo}': {e}")
            return AnalysisResult(plugin=self.nombre, conversacion_id=conversacion.id, hallazgos=[])

        categorias_detectadas = [
            c.strip().lower() for c in respuesta.split(",")
            if c.strip().lower() in CATEGORIAS
        ]

        return AnalysisResult(
            plugin=self.nombre,
            conversacion_id=conversacion.id,
            hallazgos=categorias_detectadas,
        )
