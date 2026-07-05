from dataclasses import dataclass, field
from typing import Any

from .identifier import Identifier
from ..types.knowledge_type import KnowledgeType


@dataclass(slots=True)
class KnowledgeObject:
    """
    Objeto base del Canonical Knowledge Model.
    """

    id: Identifier = field(default_factory=Identifier)

    type: KnowledgeType = KnowledgeType.CONCEPT

    title: str = ""

    summary: str = ""

    confidence: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)