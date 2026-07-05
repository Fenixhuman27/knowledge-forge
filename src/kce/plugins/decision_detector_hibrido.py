"""
Decision Detector (Hibrido: reglas + IA local)

Combina lo mejor de los dos enfoques:
1. Reglas rapidas (palabras clave amplias) para encontrar mensajes
   candidatos a contener una decision, sin gastar tiempo de IA en
   miles de mensajes irrelevantes.
2. IA local (Ollama) para confirmar o descartar cada candidato,
   con mayor precision que las reglas solas.
"""

from src.kce.pipeline import Plugin
from src.kce.schema import NormalizedConversation, AnalysisResult
from src.kce.ollama_client import preguntar_a_ollama

FRASES_CANDIDATAS = [
    "decidi",
    "voy a hacer",
    "vamos a hacer",
    "vamos a usar",
    "la opcion final",
    "me quedo con",
    "elijo",
    "he decidido",
    "vamos con",
    "la decision es",
    "opto por",
    "definitivamente voy a",
    "voy a elegir",
    "creo que voy a",
    "finalmente voy a",
]

LONGITUD_MINIMA = 30

PROMPT_BASE = """Analiza el siguiente mensaje de una persona y responde
UNICAMENTE con "SI" o "NO", sin explicaciones.

Pregunta: Este mensaje expresa que la persona tomo una decision concreta
sobre un proyecto, plan, tarea o aspecto importante de su vida?
No cuenta como decision si es solo una pregunta, un comentario casual,
o una peticion de informacion.

Mensaje: "{mensaje}"

Respuesta (SI o NO):"""


class DecisionDetectorHibrido(Plugin):
    nombre = "decision_detector_hibrido"

    def _es_candidato(self, texto_normalizado: str) -> bool:
        return any(frase in texto_normalizado for frase in FRASES_CANDIDATAS)

    def analizar(self, conversacion: NormalizedConversation) -> AnalysisResult:
        hallazgos = []

        for mensaje in conversacion.mensajes:
            if mensaje.autor != "user":
                continue

            if len(mensaje.texto.strip()) < LONGITUD_MINIMA:
                continue

            texto_normalizado = mensaje.texto.lower()

            if not self._es_candidato(texto_normalizado):
                continue

            prompt = PROMPT_BASE.format(mensaje=mensaje.texto[:500])

            try:
                respuesta = preguntar_a_ollama(prompt)
            except Exception as e:
                print(f"ERROR en un mensaje: {e}")
                continue

            if respuesta.strip().upper().startswith("SI"):
                hallazgos.append(mensaje.texto.strip())

        return AnalysisResult(
            plugin=self.nombre,
            conversacion_id=conversacion.id,
            hallazgos=hallazgos,
        )
