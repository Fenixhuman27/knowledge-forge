"""
Base comun para todos los plugins del Knowledge Cognition Engine (KCE).

Todo plugin (Decision Detector, Contradiction Detector, Task Detector, etc.)
debe heredar de PluginBase e implementar el metodo analizar().

Esto garantiza que el motor pueda ejecutar cualquier plugin de la misma forma,
sin conocer detalles internos de cada uno.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


@dataclass
class ResultadoPlugin:
    """Resultado estandar que devuelve cualquier plugin."""
    plugin: str                    # nombre del plugin, ej: "decision_detector"
    conversacion_id: str
    hallazgos: List[dict] = field(default_factory=list)


class PluginBase(ABC):
    """Clase base que todo plugin del KCE debe heredar."""

    nombre = "plugin_base"

    @abstractmethod
    def analizar(self, conversacion_normalizada) -> ResultadoPlugin:
        """
        Recibe una ConversacionNormalizada y devuelve un ResultadoPlugin.
        Cada plugin implementa su propia logica aqui.
        """
        pass
