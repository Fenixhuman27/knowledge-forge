from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from src.canonical.models.knowledge_object import KnowledgeObject


@dataclass(slots=True)
class ProcessingContext:
    """
    Estado compartido durante toda la ejecución
    del Cognitive Analysis Engine.
    """

    knowledge_objects: list[KnowledgeObject] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    cache: dict[str, Any] = field(default_factory=dict)

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)
