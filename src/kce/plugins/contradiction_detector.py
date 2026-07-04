"""
Contradiction Detector

Plugin del Knowledge Cognition Engine (KCE).
Detecta frases donde el usuario expresa un cambio de opinion o
postura respecto a algo dicho anteriormente en la misma conversacion.

Version inicial: basada en reglas (frases que indican cambio de idea).
"""

from src.kce.pipeline import Plugin
from src.kce.schema import NormalizedConversation, AnalysisResult

FRASES_CAMBIO_DE_OPINION = [
    "cambie de idea",
    "cambie de opinion",
    "en realidad no",
    "ya no quiero",
    "ya no creo",
    "me equivoque",
    "pense mal",
    "al final decidi lo contrario",
    "contradigo lo que dije",
    "olvida lo que dije",
    "mejor no",
    "pensandolo bien no",
]

LONGITUD_MINIMA = 20


class ContradictionDetector(Plugin):
    nombre = "contradiction_detector"

    def analizar(self, conversacion: NormalizedConversation) -> AnalysisResult:
        hallazgos = []

        for mensaje in conversacion.mensajes:
            if mensaje.autor != "user":
                continue

            texto_normalizado = mensaje.texto.lower()

            if len(mensaje.texto.strip()) < LONGITUD_MINIMA:
                continue

            if any(frase in texto_normalizado for frase in FRASES_CAMBIO_DE_OPINION):
                hallazgos.append(mensaje.texto.strip())

        return AnalysisResult(
            plugin=self.nombre,
            conversacion_id=conversacion.id,
            hallazgos=hallazgos,
        )
