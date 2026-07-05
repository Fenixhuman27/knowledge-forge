from __future__ import annotations

from typing import List

from src.analysis.processors.base_processor import BaseProcessor
from src.canonical.models.knowledge_object import KnowledgeObject


class Pipeline:
    """
    Define una secuencia ordenada de procesadores.
    """

    def __init__(self) -> None:
        self._processors: List[BaseProcessor] = []

    def add(self, processor: BaseProcessor) -> None:
        self._processors.append(processor)

    def execute(
        self,
        objects: List[KnowledgeObject],
    ) -> List[KnowledgeObject]:

        result = objects

        for processor in self._processors:
            result = processor.process(result)

        return result

    @property
    def processors(self) -> List[BaseProcessor]:
        return self._processors.copy()