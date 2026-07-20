"""
Jarvis-X Universal App Launcher
Version: 1.1.0
"""

import os
import shutil
import subprocess

from config import APPLICATIONS
from modules.ui import success


def find_executable(app_entry):
    if isinstance(app_entry, str):
        path = shutil.which(app_entry)

        if path:
            return path

        if os.path.exists(app_entry):
            return app_entry

        return None

    if isinstance(app_entry, list):

        for item in app_entry:

            path = shutil.which(item)

            if path:
                return path

            if os.path.exists(item):
                return item

    return None


def open_app(app_name):
    """
    Returns:
        True  -> App opened
        False -> App not found
    """

    app_name = app_name.lower().strip()

    if app_name not in APPLICATIONS:
        return False

    executable = find_executable(APPLICATIONS[app_name])

    if executable is None:
        return False

    try:
        subprocess.Popen([executable])
        success(f"Opening {app_name.title()}...")
        return True

    except Exception:
        return False