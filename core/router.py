"""
Jarvis-X Command Router
Version: 8.0.0
"""

from config import FILE_EXTENSIONS
from core.website_resolver import resolve_website


POWER_COMMANDS = {
    "shutdown",
    "restart",
    "lock",
    "sleep",
    "logoff",
    "cancel_shutdown",
}

SYSTEM_COMMANDS = {
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
}

WORKFLOW_COMMANDS = {
    "work_mode",
    "study_mode",
    "movie_mode",
    "gaming_mode",
}


def route(command):
    """
    Returns:
        (intent, value)
    """

    action = command.action.lower().strip()
    target = command.target.strip()

    # ----------------------------------------
    # AI
    # ----------------------------------------

    if action == "ask_ai":
        return ("ask_ai", target)

    # ----------------------------------------
    # Power
    # ----------------------------------------

    if action in POWER_COMMANDS:
        return (action, target)

    # ----------------------------------------
    # Workflows
    # ----------------------------------------

    if action in WORKFLOW_COMMANDS:
        return (action, "")

    # ----------------------------------------
    # Desktop Automation
    # ----------------------------------------

    if action in SYSTEM_COMMANDS:
        return (action, target)

    # ----------------------------------------
    # Open
    # ----------------------------------------

    if action == "open":

        if target.endswith(FILE_EXTENSIONS):
            return ("open_file", target)

        if resolve_website(target):
            return ("open_website", target)

        return ("open_app", target)

    # ----------------------------------------
    # Search
    # ----------------------------------------

    if action == "find":
        return ("find", target)

    if action == "search":

        if target.startswith("google "):
            return ("google", target[7:].strip())

        if target.startswith("youtube "):
            return ("youtube", target[8:].strip())

        return ("find", target)

    if action == "google":
        return ("google", target)

    if action == "youtube":
        return ("youtube", target)

    # ----------------------------------------
    # Notes
    # ----------------------------------------

    if action == "note":
        return ("save_note", target)

    if action == "notes":
        return ("show_notes", "")

    # ----------------------------------------
    # System
    # ----------------------------------------

    if action == "time":
        return ("time", "")

    if action == "date":
        return ("date", "")

    if action == "help":
        return ("help", "")

    if action == "clear":
        return ("clear", "")

    if action == "reindex":
        return ("reindex", "")

    if action == "rebuild_apps":
        return ("rebuild_apps", "")

    return ("unknown", target)