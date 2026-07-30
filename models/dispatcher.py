"""
Jarvis-X Command Model
Version: 1.0.0
"""


class Command:
    """
    Represents a parsed user command.
    """

    def __init__(
        self,
        action: str = "",
        target: str = "",
        context: str | None = None,
        query: str | None = None,
        confidence: float = 1.0
    ):
        self.action = action
        self.target = target
        self.context = context
        self.query = query
        self.confidence = confidence

    def to_dict(self):
        return {
            "action": self.action,
            "target": self.target,
            "context": self.context,
            "query": self.query,
            "confidence": self.confidence
        }

    def __str__(self):
        return (
            f"Command("
            f"action='{self.action}', "
            f"target='{self.target}', "
            f"context='{self.context}', "
            f"query='{self.query}', "
            f"confidence={self.confidence})"
        )