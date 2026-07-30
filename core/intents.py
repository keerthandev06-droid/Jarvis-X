"""
Jarvis-X Intent Detection Engine
Version: 2.1.0
"""

from config import FILE_EXTENSIONS


def detect_intent(command):
    """
    Detects the user's intent.

    Returns:
        (intent, value)
    """

    text = command.lower().strip()

    # ---------- REINDEX ----------

    if text == "reindex":
        return ("reindex", "")

    # ---------- REBUILD APPS ----------

    if text in (
        "rebuild apps",
        "scan apps",
        "refresh apps",
    ):
        return ("rebuild_apps", "")

    # ---------- FIND ----------

    if text.startswith("find "):
        return ("find", text[5:].strip())

    if text.startswith("search "):

        query = text[7:].strip()

        # Preserve existing Google and YouTube commands
        if query.startswith("google "):
            return ("google", query[7:].strip())

        if query.startswith("youtube "):
            return ("youtube", query[8:].strip())

        return ("find", query)

    if text.startswith("locate "):
        return ("find", text[7:].strip())

    if text.startswith("where is "):
        return ("find", text[9:].strip())

    # ---------- OPEN ----------

    if text.startswith("open "):
        value = text[5:].strip()

        if value.endswith(FILE_EXTENSIONS):
            return ("open_file", value)

        return ("open_app", value)

    # ---------- GOOGLE ----------

    if text.startswith("google "):
        return ("google", text[7:].strip())

    # ---------- YOUTUBE ----------

    if text.startswith("youtube "):
        return ("youtube", text[8:].strip())

    # ---------- NOTES ----------

    if text.startswith("note "):
        return ("save_note", text[5:].strip())

    if text.startswith("save note "):
        return ("save_note", text[10:].strip())

    if text == "notes":
        return ("show_notes", "")

    # ---------- TIME ----------

    if text == "time":
        return ("time", "")

    # ---------- DATE ----------

    if text == "date":
        return ("date", "")

    # ---------- HELP ----------

    if text == "help":
        return ("help", "")

    # ---------- CLEAR ----------

    if text == "clear":
        return ("clear", "")

    return ("unknown", text)