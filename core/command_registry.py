"""
Jarvis-X Command Registry
Version: 1.2.0
"""

from modules.utils import (
    current_time,
    current_date,
    show_help,
    clear_screen,
)

from modules.browser import (
    google_search,
    youtube_search,
)

from modules.notes import (
    save_note,
    show_notes,
)

from modules.app_launcher import open_app
from modules.file_search import open_file, smart_find
from modules.indexer import build_index


COMMANDS = {
    "help": show_help,
    "time": current_time,
    "date": current_date,
    "clear": clear_screen,

    "open_app": open_app,
    "open_file": open_file,

    # Smart Find
    "find": smart_find,

    "google": google_search,
    "youtube": youtube_search,

    "save_note": save_note,
    "show_notes": show_notes,

    "reindex": build_index,
}