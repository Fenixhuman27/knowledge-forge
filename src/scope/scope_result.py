from dataclasses import dataclass, field


@dataclass(slots=True)
class ScopeResult:
    conversation_id: str

    score: int = 0

    matched_keywords: list[str] = field(default_factory=list)

    relevant: bool = False