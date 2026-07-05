from __future__ import annotations

from src.analysis.context.processing_context import ProcessingContext
from src.analysis.processors.base_processor import BaseProcessor


class CognitiveAnalysisEngine:

    def __init__(self) -> None:
        self._processors: list[BaseProcessor] = []

    def register(self, processor: BaseProcessor) -> None:
        self._processors.append(processor)

    def run(
        self,
        context: ProcessingContext,
    ) -> ProcessingContext:

        for processor in self._processors:
            context = processor.process(context)

        return context

    @property
    def processors(self) -> list[BaseProcessor]:
        return self._processors.copy()
