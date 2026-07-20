"""
Jarvis-X Natural Language Parser
"""

import re

from config import ACTION_WORDS, FILLER_WORDS


def normalize(command):
    """
    Converts natural language into a standard Jarvis-X command.
    """

    text = command.lower().strip()

    # Keep dots so filenames like test.txt remain unchanged
    text = re.sub(r"[^\w\s.]", "", text)

    words = text.split()

    cleaned = [word for word in words if word not in FILLER_WORDS]

    if not cleaned:
        return ""

    for action, aliases in ACTION_WORDS.items():
        for alias in aliases:
            if alias in cleaned:
                index = cleaned.index(alias)
                target = " ".join(cleaned[index + 1:])

                if target:
                    return f"{action} {target}"

    return " ".join(cleaned)