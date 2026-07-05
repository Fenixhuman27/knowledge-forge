from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from src.canonical.models.knowledge_object import KnowledgeObject


class BaseProcessor(ABC):
    """
    Clase base para todos los procesadores del
    Cognitive Analysis Engine.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Nombre único del procesador."""
        pass

    @abstractmethod
    def process(
        self,
        objects: List[KnowledgeObject],
    ) -> List[KnowledgeObject]:
        """
        Recibe Knowledge Objects y devuelve
        nuevos Knowledge Objects.
        """
        pass