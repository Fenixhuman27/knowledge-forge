"""
Decision Detector (con IA local)

Version del Decision Detector que usa Ollama (IA local, gratuita)
en lugar de reglas de texto, para detectar decisiones reales con
mayor precision y comprension de contexto.
"""

from src.kce.pipeline import Plugin
from src.kce.schema import NormalizedConversation, AnalysisResult
from src.kce.ollama_client import preguntar_a_ollama

LONGITUD_MINIMA = 40

PROMPT_BASE = """Analiza el siguiente mensaje de una persona y responde
UNICAMENTE con "SI" o "NO", sin explicaciones.

Pregunta: ¿Este mensaje expresa que la persona tomo una decision concreta
sobre un proyecto, plan, tarea o aspecto importante de su vida?
No cuenta como decision si es solo una pregunta, un comentario casual,
o una peticion de informacion.

Mensaje: "{mensaje}"

Respuesta (SI o NO):"""


class DecisionDetectorIA(Plugin):
    nombre = "decision_detector_ia"

    def analizar(self, conversacion: NormalizedConversation) -> AnalysisResult:
        hallazgos = []

        for mensaje in conversacion.mensajes:
            if mensaje.autor != "user":
                continue

            if len(mensaje.texto.strip()) < LONGITUD_MINIMA:
                continue

            prompt = PROMPT_BASE.format(mensaje=mensaje.texto[:500])

            try:
                respuesta = preguntar_a_ollama(prompt)
            except Exception:
                continue

            if respuesta.strip().upper().startswith("SI"):
                hallazgos.append(mensaje.texto.strip())

        return AnalysisResult(
            plugin=self.nombre,
            conversacion_id=conversacion.id,
            hallazgos=hallazgos,
        )