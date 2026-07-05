from __future__ import annotations

from src.analysis.processors.base_processor import BaseProcessor


class ProcessorRegistry:

    def __init__(self) -> None:
        self._processors: dict[str, BaseProcessor] = {}

    def register(self, processor: BaseProcessor) -> None:
        self._processors[processor.name] = processor

    def unregister(self, name: str) -> None:
        self._processors.pop(name, None)

    def get(self, name: str) -> BaseProcessor | None:
        return self._processors.get(name)

    def all(self) -> list[BaseProcessor]:
        return list(self._processors.values())

    def clear(self) -> None:
        self._processors.clear()
