"""
Knowledge Cognition Engine (KCE)
Pipeline principal.

Este es el corazon del motor. Recibe una conversacion normalizada y la
hace pasar por una cadena de etapas. Los plugins de analisis se
registran aqui y se ejecutan al final de la cadena, todos recibiendo
la misma informacion.

Etapas del pipeline:
  1. Normalizacion       -> ya hecha antes de llegar aqui (normalizers.py)
  2. Analisis semantico   -> (a construir)
  3. Deteccion de entidades -> (a construir)
  4. Deteccion de relaciones -> (a construir)
  5. Actualizacion del Knowledge Graph -> (a construir)
  6. Plugins de analisis  -> cualquier detector especifico (decisiones,
                              contradicciones, etc.) se registra aqui
"""

from src.kce.schema import NormalizedConversation, AnalysisResult


class Plugin:
    """Clase base que debe heredar cualquier plugin de analisis.
    Cada plugin recibe una conversacion normalizada y devuelve un
    AnalysisResult estandarizado."""

    nombre = "plugin_sin_nombre"

    def analizar(self, conversacion: NormalizedConversation) -> AnalysisResult:
        raise NotImplementedError(
            f"El plugin '{self.nombre}' debe implementar el metodo analizar()"
        )


class KCEPipeline:
    """Orquestador principal del Knowledge Cognition Engine."""

    def __init__(self):
        self.plugins: list[Plugin] = []

    def registrar_plugin(self, plugin: Plugin):
        """Agrega un nuevo plugin de analisis al pipeline."""
        self.plugins.append(plugin)

    def procesar(self, conversacion: NormalizedConversation) -> list[AnalysisResult]:
        """Hace pasar una conversacion normalizada por todos los
        plugins registrados y devuelve la lista de resultados."""
        resultados = []

        for plugin in self.plugins:
            resultado = plugin.analizar(conversacion)
            resultados.append(resultado)

        return resultados
