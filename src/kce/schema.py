"""
Este archivo define la estructura de datos estandar que viaja
a traves de todo el Knowledge Cognition Engine (KCE).

Ningun plugin debe conocer el formato original (ChatGPT, Claude, Gemini).
Todos los plugins trabajan unicamente sobre esta estructura normalizada.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Mensaje:
    autor: str          # "user" o "assistant"
    texto: str
    fecha: Optional[str] = None


@dataclass
class ConversacionNormalizada:
    id: str
    titulo: str
    fecha: str
    origen: str                    # "chatgpt", "claude", "gemini", etc.
    mensajes: List[Mensaje] = field(default_factory=list)
    temas: List[str] = field(default_factory=list)
    metadatos: dict = field(default_factory=dict)
