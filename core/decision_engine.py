"""
==========================================================
Jarvis-X Decision Engine
Version : 1.0.0
==========================================================

Purpose:
Decides which subsystem should handle a user request.
"""

from dataclasses import dataclass


# ==========================================================
# Decision Object
# ==========================================================

@dataclass
class Decision:
    source: str
    reason: str = ""


# ==========================================================
# Keywords
# ==========================================================

WEB_KEYWORDS = {
    "today",
    "latest",
    "news",
    "current",
    "live",
    "weather",
    "temperature",
    "forecast",
    "score",
    "match",
    "ipl",
    "cricket",
    "football",
    "stock",
    "share",
    "bitcoin",
    "crypto",
    "price",
    "collection",
    "box office",
    "released",
    "release date",
    "breaking",
    "headline",
}

LOCAL_KEYWORDS = {
    "time",
    "date",
    "shutdown",
    "restart",
    "lock",
    "sleep",
    "volume",
    "mute",
    "unmute",
    "brightness",
    "battery",
}

AI_KEYWORDS = {
    "what",
    "why",
    "how",
    "who",
    "explain",
    "describe",
    "compare",
    "write",
    "create",
    "generate",
    "summarize",
    "translate",
    "code",
    "python",
    "java",
    "c++",
}


# ==========================================================
# Decision Logic
# ==========================================================

def decide(command: str) -> Decision:
    """
    Decide which engine should process the request.

    Returns:
        Decision(source="local")
        Decision(source="web")
        Decision(source="ai")
    """

    if not command:
        return Decision("ai", "Empty command")

    text = command.lower().strip()

    # --------------------------------------
    # Local commands
    # --------------------------------------

    for keyword in LOCAL_KEYWORDS:

        if keyword in text:
            return Decision(
                source="local",
                reason=f"Matched local keyword: {keyword}",
            )

    # --------------------------------------
    # Live web information
    # --------------------------------------

    for keyword in WEB_KEYWORDS:

        if keyword in text:
            return Decision(
                source="web",
                reason=f"Matched web keyword: {keyword}",
            )

    # --------------------------------------
    # AI reasoning
    # --------------------------------------

    for keyword in AI_KEYWORDS:

        if keyword in text:
            return Decision(
                source="ai",
                reason=f"Matched AI keyword: {keyword}",
            )

    # --------------------------------------
    # Default
    # --------------------------------------

    return Decision(
        source="ai",
        reason="Default AI handler",
    )


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    tests = [
        "What time is it?",
        "Open Chrome",
        "Today's weather",
        "Latest AI news",
        "Explain Python decorators",
        "Jana Nayagan collection today",
        "Shutdown computer",
    ]

    for item in tests:

        decision = decide(item)

        print(
            f"{item}\n"
            f" -> {decision.source.upper()}"
            f" ({decision.reason})\n"
        )