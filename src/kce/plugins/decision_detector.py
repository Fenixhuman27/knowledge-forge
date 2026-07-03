from src.kce.plugin_base import PluginBase, ResultadoPlugin

FRASES_DECISION = [
    "decidi", "decidí", "voy a", "he decidido", "opto por",
    "elegi", "elegí", "me quedo con", "vamos a hacer",
    "la decision es", "la decisión es", "resolvi", "resolví",
]


class DecisionDetector(PluginBase):
    nombre = "decision_detector"

    def analizar(self, conversacion_normalizada) -> ResultadoPlugin:
        hallazgos = []

        for mensaje in conversacion_normalizada.mensajes:
            if mensaje.autor != "user":
                continue

            texto_normalizado = mensaje.texto.lower()

            for frase in FRASES_DECISION:
                if frase in texto_normalizado:
                    hallazgos.append({
                        "frase_detectada": frase,
                        "fragmento": mensaje.texto[:200],
                    })
                    break

        return ResultadoPlugin(
            plugin=self.nombre,
            conversacion_id=conversacion_normalizada.id,
            hallazgos=hallazgos,
        )
