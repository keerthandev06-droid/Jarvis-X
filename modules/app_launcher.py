"""
Jarvis-X Application Launcher
Supports:
- .lnk
- .exe
- Windows Store (UWP/MSIX) apps
"""

import os
import subprocess

from modules.app_database import search_app
from modules.ui import success, warning


def open_app(app_name):
    """
    Open an application by name.
    """

    results = search_app(app_name)

    if not results:
        warning(f"Application '{app_name}' not found.")
        return False

    name, path, app_type = results[0]

    try:

        if app_type in ("lnk", "exe"):
            os.startfile(path)
            success(f"Opening {name}...")
            return True

        elif app_type == "store":
            subprocess.Popen(
                [
                    "explorer.exe",
                    f"shell:AppsFolder\\{path}",
                ]
            )

            success(f"Opening {name}...")
            return True

        else:
            warning(f"Unsupported application type: {app_type}")
            return False

    except Exception as e:
        warning(f"Failed to open {name}")
        print(e)
        return False