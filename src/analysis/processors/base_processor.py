from __future__ import annotations

from abc import ABC, abstractmethod

from src.analysis.context.processing_context import ProcessingContext


class BaseProcessor(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def process(
        self,
        context: ProcessingContext,
    ) -> ProcessingContext:
        pass
