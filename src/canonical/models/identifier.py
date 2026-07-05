from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(slots=True, frozen=True)
class Identifier:
    """
    Identificador único e inmutable para cualquier objeto del
    Canonical Knowledge Model.
    """

    value: str = field(default_factory=lambda: str(uuid4()))

    def __str__(self) -> str:
        return self.value