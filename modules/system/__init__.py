"""
==========================================================
Jarvis-X System Module
Version : 2.0.0
==========================================================
"""

# ---------------- Power ----------------

from .power import (
    shutdown,
    restart,
    cancel_shutdown,
    lock,
    sleep,
    logoff,
)

# ---------------- Screenshot ----------------

from .screenshot import take_screenshot

# ---------------- Folders ----------------

from .folders import (
    open_downloads,
    open_desktop,
    open_documents,
    open_pictures,
    open_videos,
    open_music,
)

# ---------------- Process ----------------

from .process import (
    close_process,
    kill_process,
    list_processes,
    task_manager,
)

# ---------------- Volume ----------------

from .volume import (
    mute,
    unmute,
    volume_up,
    volume_down,
    set_volume,
)

# ---------------- Brightness ----------------

from .brightness import (
    get_brightness,
    set_brightness,
    increase as brightness_up,
    decrease as brightness_down,
)

SYSTEM_COMMANDS = {

    # Power
    "shutdown": shutdown,
    "restart": restart,
    "cancel_shutdown": cancel_shutdown,
    "lock": lock,
    "sleep": sleep,
    "logoff": logoff,

    # Screenshot
    "screenshot": take_screenshot,

    # Folders
    "downloads": open_downloads,
    "desktop": open_desktop,
    "documents": open_documents,
    "pictures": open_pictures,
    "videos": open_videos,
    "music": open_music,

    # Process
    "close_process": close_process,
    "kill_process": kill_process,
    "list_processes": list_processes,
    "task_manager": task_manager,

    # Volume
    "mute": mute,
    "unmute": unmute,
    "volume_up": volume_up,
    "volume_down": volume_down,
    "set_volume": set_volume,

    # Brightness
    "get_brightness": get_brightness,
    "set_brightness": set_brightness,
    "brightness_up": brightness_up,
    "brightness_down": brightness_down,
}