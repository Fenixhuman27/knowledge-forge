"""
Decision Detector

Plugin del Knowledge Cognition Engine (KCE).
Detecta frases dentro de una conversacion que probablemente indican
que el usuario tomo una decision concreta.

Version 2: reglas mejoradas con lista negra de frases irrelevantes
y filtro de sustancia minima, para reducir falsos positivos.
"""

from src.kce.pipeline import Plugin
from src.kce.schema import NormalizedConversation, AnalysisResult

FRASES_DECISION = [
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
]

FRASES_IRRELEVANTES = [
    "voy a hacerte una pregunta",
    "voy a hacer una pregunta",
    "voy a explicarte",
    "voy a contarte",
    "voy a mostrarte",
    "voy a intentar explicar",
]

PALABRAS_DE_SUSTANCIA = [
    "proyecto", "banda", "cancion", "disco", "estrategia", "plan",
    "nombre", "trabajo", "casa", "mudanza", "viaje", "empresa",
    "contrato", "dinero", "estudio", "carrera", "relacion",
]

LONGITUD_MINIMA = 40


class DecisionDetector(Plugin):
    nombre = "decision_detector"

    def _es_falso_positivo(self, texto_normalizado: str) -> bool:
        return any(frase in texto_normalizado for frase in FRASES_IRRELEVANTES)

    def _tiene_sustancia(self, texto_normalizado: str) -> bool:
        return any(palabra in texto_normalizado for palabra in PALABRAS_DE_SUSTANCIA)

    def analizar(self, conversacion: NormalizedConversation) -> AnalysisResult:
        hallazgos = []

        for mensaje in conversacion.mensajes:
            if mensaje.autor != "user":
                continue

            texto_normalizado = mensaje.texto.lower()

            if len(mensaje.texto.strip()) < LONGITUD_MINIMA:
                continue

            if self._es_falso_positivo(texto_normalizado):
                continue

            contiene_frase_decision = any(
                frase in texto_normalizado for frase in FRASES_DECISION
            )

            if contiene_frase_decision and self._tiene_sustancia(texto_normalizado):
                hallazgos.append(mensaje.texto.strip())

        return AnalysisResult(
            plugin=self.nombre,
            conversacion_id=conversacion.id,
            hallazgos=hallazgos,
        )
