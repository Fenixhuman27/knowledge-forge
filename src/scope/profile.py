from dataclasses import dataclass, field


@dataclass(slots=True)
class ScopeProfile:
    """
    Define un universo de conocimiento.
    """

    name: str

    keywords: dict[str, int] = field(default_factory=dict)

    minimum_score: int = 10