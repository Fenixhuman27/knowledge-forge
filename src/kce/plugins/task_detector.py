"""
Task Detector

Plugin del Knowledge Cognition Engine (KCE).
Detecta frases que indican una tarea pendiente, algo que el usuario
dijo que necesita hacer, comprar, escribir, terminar, etc.

Version inicial: basada en reglas.
"""

from src.kce.pipeline import Plugin
from src.kce.schema import NormalizedConversation, AnalysisResult

FRASES_TAREA = [
    "tengo que",
    "necesito hacer",
    "me falta",
    "todavia debo",
    "hay que",
    "pendiente de",
    "recordar que",
    "no me olvide de",
    "no me olvidar de",
    "queda pendiente",
]

FRASES_IRRELEVANTES = [
    "tengo que decirte",
    "tengo que preguntarte",
    "tengo que confesar",
]

LONGITUD_MINIMA = 25


class TaskDetector(Plugin):
    nombre = "task_detector"

    def analizar(self, conversacion: NormalizedConversation) -> AnalysisResult:
        hallazgos = []

        for mensaje in conversacion.mensajes:
            if mensaje.autor != "user":
                continue

            texto_normalizado = mensaje.texto.lower()

            if len(mensaje.texto.strip()) < LONGITUD_MINIMA:
                continue

            if any(frase in texto_normalizado for frase in FRASES_IRRELEVANTES):
                continue

            if any(frase in texto_normalizado for frase in FRASES_TAREA):
                hallazgos.append(mensaje.texto.strip())

        return AnalysisResult(
            plugin=self.nombre,
            conversacion_id=conversacion.id,
            hallazgos=hallazgos,
        )
