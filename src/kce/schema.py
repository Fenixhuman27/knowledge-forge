"""
Knowledge Cognition Engine (KCE)
Esquema de datos estandar.

Toda conversacion, sin importar su origen (ChatGPT, Claude, Gemini, etc.),
se convierte a esta forma antes de ser analizada. Todos los plugins del
motor reciben y devuelven estas mismas estructuras.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NormalizedMessage:
    """Un mensaje individual, ya limpio y estandarizado."""
    autor: str              # "user" o "assistant"
    texto: str
    timestamp: Optional[float] = None


@dataclass
class NormalizedConversation:
    """Una conversacion completa, en formato universal, lista para el motor."""
    id: str
    titulo: str
    fecha: Optional[str]
    origen: str              # "chatgpt", "claude", "gemini", etc.
    mensajes: list[NormalizedMessage] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


@dataclass
class Entity:
    """Algo que un plugin detecto dentro de una conversacion:
    una persona, un proyecto, un lugar, una fecha clave, etc."""
    tipo: str                # ej: "persona", "proyecto", "lugar"
    valor: str                # ej: "Banda de rock", "Mario"
    conversacion_id: str
    contexto: Optional[str] = None


@dataclass
class Relationship:
    """Una conexion detectada entre dos elementos (dos conversaciones,
    dos entidades, etc.)."""
    origen_id: str
    destino_id: str
    tipo: str                 # ej: "mismo_proyecto", "contradice", "continua"
    peso: float = 1.0
    descripcion: Optional[str] = None


@dataclass
class AnalysisResult:
    """Resultado estandarizado que devuelve cualquier plugin del motor."""
    plugin: str                # nombre del plugin que genero el resultado
    conversacion_id: str
    hallazgos: list = field(default_factory=list)
    entidades: list[Entity] = field(default_factory=list)
    relaciones: list[Relationship] = field(default_factory=list)
