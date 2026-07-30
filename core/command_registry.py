"""
Jarvis-X Command Registry
Version: 4.0.0
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
from modules.file_search import (
    open_file,
    smart_find,
)

from modules.indexer import build_index
from modules.app_manager import rebuild_apps

# ==========================================
# Power
# ==========================================

from modules.system.power import (
    shutdown,
    restart,
    cancel_shutdown,
    lock,
    sleep,
    logoff,
)

# ==========================================
# System
# ==========================================

from modules.system import (
    take_screenshot,
    open_downloads,
    open_desktop,
    open_documents,
    open_pictures,
    open_videos,
    open_music,
    mute,
    unmute,
    volume_up,
    volume_down,
    set_volume,
    brightness_up,
    brightness_down,
    set_brightness,
    close_process,
    kill_process,
    list_processes,
    task_manager,
)

# ==========================================
# Workflows
# ==========================================

from features import WORKFLOWS


COMMANDS = {

    # ======================================
    # General
    # ======================================

    "help": show_help,
    "time": current_time,
    "date": current_date,
    "clear": clear_screen,

    # ======================================
    # Apps / Files
    # ======================================

    "open_app": open_app,
    "open_file": open_file,
    "find": smart_find,

    # ======================================
    # Browser
    # ======================================

    "google": google_search,
    "youtube": youtube_search,

    # ======================================
    # Notes
    # ======================================

    "save_note": save_note,
    "show_notes": show_notes,

    # ======================================
    # Power
    # ======================================

    "shutdown": shutdown,
    "restart": restart,
    "cancel_shutdown": cancel_shutdown,
    "lock": lock,
    "sleep": sleep,
    "logoff": logoff,

    # ======================================
    # Screenshot
    # ======================================

    "screenshot": take_screenshot,

    # ======================================
    # Folders
    # ======================================

    "downloads": open_downloads,
    "desktop": open_desktop,
    "documents": open_documents,
    "pictures": open_pictures,
    "videos": open_videos,
    "music": open_music,

    # ======================================
    # Volume
    # ======================================

    "mute": mute,
    "unmute": unmute,
    "volume_up": volume_up,
    "volume_down": volume_down,
    "set_volume": set_volume,

    # ======================================
    # Brightness
    # ======================================

    "brightness_up": brightness_up,
    "brightness_down": brightness_down,
    "set_brightness": set_brightness,

    # ======================================
    # Process
    # ======================================

    "close_process": close_process,
    "kill_process": kill_process,
    "list_processes": list_processes,
    "task_manager": task_manager,

    # ======================================
    # Workflows
    # ======================================

    "work_mode": WORKFLOWS["work mode"],
    "study_mode": WORKFLOWS["study mode"],
    "movie_mode": WORKFLOWS["movie mode"],
    "gaming_mode": WORKFLOWS["gaming mode"],

    # ======================================
    # Maintenance
    # ======================================

    "reindex": build_index,
    "rebuild_apps": rebuild_apps,
}