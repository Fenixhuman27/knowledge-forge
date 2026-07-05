class KeywordMatcher:

    @staticmethod
    def score(text: str, keywords: dict[str, int]) -> int:

        score = 0

        text = text.lower()

        for keyword, weight in keywords.items():

            if keyword.lower() in text:

                score += weight

        return score