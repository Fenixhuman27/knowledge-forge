from .keyword_matcher import KeywordMatcher
from .profile import ScopeProfile


class ScopeEngine:

    def belongs(
        self,
        conversation_text: str,
        profile: ScopeProfile,
    ) -> bool:

        score = KeywordMatcher.score(
            conversation_text,
            profile.keywords,
        )

        return score >= profile.minimum_score