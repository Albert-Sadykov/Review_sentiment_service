class SentimentAnalyzer:
    POSITIVE_KEYWORDS = ["хорош", "любл", "отличн", "супер", "прекрасн"]
    NEGATIVE_KEYWORDS = ["плох", "ненавиж", "ужасн", "отвратительн", "хейт"]

    @classmethod
    def detect(cls, text: str) -> str:
        text = text.lower()
        if any(word in text for word in cls.NEGATIVE_KEYWORDS):
            return "negative"
        if any(word in text for word in cls.POSITIVE_KEYWORDS):
            return "positive"
        return "neutral"