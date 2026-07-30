"""
Jarvis-X Natural Language Understanding Engine
Version: 8.0.0
"""

import re

from core.command import Command

# ==========================================================
# Stop Words
# ==========================================================

STOP_WORDS = {
    "please",
    "can",
    "could",
    "would",
    "will",
    "you",
    "me",
    "my",
    "the",
    "a",
    "an",
    "to",
    "for",
    "kindly",
    "just",
    "up",
    "of",
    "on",
    "at",
    "this",
    "that",
    "some",
    "computer",
    "pc",
    "system",
}

# ==========================================================
# Open Words
# ==========================================================

OPEN_WORDS = {
    "open",
    "launch",
    "start",
    "run",
    "execute",
    "load",
    "show",
    "bring",
    "fire",
    "boot",
    "use",
    "visit",
    "browse",
    "navigate",
}

# ==========================================================
# Power Words
# ==========================================================

POWER_WORDS = {
    "shutdown",
    "restart",
    "lock",
    "sleep",
    "logoff",
}

# ==========================================================
# Workflow Words
# ==========================================================

WORKFLOW_WORDS = {
    "work_mode",
    "study_mode",
    "movie_mode",
    "gaming_mode",
}

# ==========================================================
# Phrases
# ==========================================================

PHRASES = {

    # ---------- Workflows ----------

    "work mode": "work_mode",
    "study mode": "study_mode",
    "movie mode": "movie_mode",
    "gaming mode": "gaming_mode",

    # ---------- Screenshot ----------

    "take screenshot": "screenshot",
    "take a screenshot": "screenshot",
    "capture screen": "screenshot",
    "screen shot": "screenshot",

    # ---------- Volume ----------

    "volume up": "volume_up",
    "volume down": "volume_down",

    # ---------- Brightness ----------

    "brightness up": "brightness_up",
    "brightness down": "brightness_down",
    "increase brightness": "brightness_up",
    "decrease brightness": "brightness_down",

    # ---------- Close Apps ----------

    "close chrome": "close_process chrome",
    "close edge": "close_process edge",
    "close firefox": "close_process firefox",
    "close vscode": "close_process vscode",

    # ---------- Common ----------

    "cancel shutdown": "cancel_shutdown",

    "i need": "open",
    "i want": "open",
    "i want to": "open",
    "i would like": "open",

    "show me": "open",
    "take me to": "open",
    "go to": "open",
    "navigate to": "open",
    "open up": "open",
}

# ==========================================================
# Local Commands
# ==========================================================

LOCAL_COMMANDS = {

    # Apps

    "open",
    "find",
    "search",

    # Browser

    "google",
    "youtube",

    # Notes

    "note",
    "notes",

    # General

    "help",
    "time",
    "date",
    "clear",

    # Maintenance

    "reindex",
    "rebuild_apps",

    # Power

    "shutdown",
    "restart",
    "lock",
    "sleep",
    "logoff",
    "cancel_shutdown",

    # System

    "screenshot",

    "downloads",
    "desktop",
    "documents",
    "pictures",
    "videos",
    "music",

    "mute",
    "unmute",

    "volume_up",
    "volume_down",
    "set_volume",

    "brightness_up",
    "brightness_down",
    "set_brightness",

    "close_process",
    "kill_process",
    "list_processes",
    "task_manager",

    # Workflows

    "work_mode",
    "study_mode",
    "movie_mode",
    "gaming_mode",
}

# ==========================================================
# AI Keywords
# ==========================================================

AI_WORDS = {

    "what",
    "who",
    "why",
    "when",
    "where",
    "which",
    "how",

    "explain",
    "tell",
    "define",
    "describe",
    "compare",

    "write",
    "create",
    "generate",

    "summarize",
    "translate",

    "solve",
    "calculate",

    "code",
}

# ==========================================================
# Main
# ==========================================================

def preprocess(text: str) -> Command:
    """
    Convert natural language into a Command.
    """

    original = text.strip()

    cleaned = original.lower()

    cleaned = re.sub(
        r"[^\w\s]",
        "",
        cleaned,
    )

    # Replace phrases

    for phrase in sorted(
        PHRASES,
        key=len,
        reverse=True,
    ):

        cleaned = cleaned.replace(
            phrase,
            PHRASES[phrase],
        )

    words = []

    for word in cleaned.split():

        if word in STOP_WORDS:
            continue

        if word in OPEN_WORDS:
            word = "open"

        words.append(word)

    if not words:
        return Command()

    action = words[0]

    target = " ".join(words[1:])

    # ======================================================
    # AI
    # ======================================================

    if action in AI_WORDS:

        return Command(
            action="ask_ai",
            target=original,
            confidence=1.0,
        )

    # ======================================================
    # Workflow
    # ======================================================

    if action in WORKFLOW_WORDS:

        return Command(
            action=action,
            target="",
            confidence=1.0,
        )

    # ======================================================
    # Power
    # ======================================================

    if action in POWER_WORDS:

        return Command(
            action=action,
            target=target,
            confidence=1.0,
        )

    # ======================================================
    # Local Commands
    # ======================================================

    if action in LOCAL_COMMANDS:

        return Command(
            action=action,
            target=target,
            confidence=1.0,
        )

    # ======================================================
    # Single Word
    # ======================================================

    if len(words) == 1:

        return Command(
            action="open",
            target=words[0],
            confidence=1.0,
        )

    # ======================================================
    # Default AI
    # ======================================================

    return Command(
        action="ask_ai",
        target=original,
        confidence=1.0,
    )