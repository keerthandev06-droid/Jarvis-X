"""
Jarvis-X Action Engine
Version: 1.0.0
"""


def detect_action(command: str) -> dict:
    """
    Detect the user's action.
    """

    command = command.lower().strip()

    # -------------------------
    # Open
    # -------------------------

    if command.startswith("open "):
        return {
            "action": "open",
            "target": command.replace("open ", "", 1)
        }

    # -------------------------
    # Google Search
    # -------------------------

    if command.startswith("search google for "):
        return {
            "action": "search_google",
            "target": command.replace("search google for ", "", 1)
        }

    # -------------------------
    # YouTube Search
    # -------------------------

    if command.startswith("search youtube for "):
        return {
            "action": "search_youtube",
            "target": command.replace("search youtube for ", "", 1)
        }

    # -------------------------
    # Play
    # -------------------------

    if command.startswith("play "):
        return {
            "action": "play",
            "target": command.replace("play ", "", 1)
        }

    return {
        "action": "unknown",
        "target": command
    }