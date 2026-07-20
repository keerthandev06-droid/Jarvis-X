import os
import shutil
import subprocess

from config import (
    APPLICATIONS,
    BROWSER_EXECUTABLE,
    BROWSER_NAME,
    BROWSER_PATHS,
    FILE_EXPLORER_PATH,
)


def get_firefox():
    firefox = shutil.which(BROWSER_EXECUTABLE)

    if firefox:
        return firefox

    for path in BROWSER_PATHS:
        if os.path.exists(path):
            return path

    return None


def open_notepad():
    try:
        subprocess.Popen(APPLICATIONS["notepad"])
        print("✅ Opening Notepad...")
    except Exception as e:
        print(f"❌ {e}")


def open_calculator():
    try:
        subprocess.Popen(APPLICATIONS["calculator"])
        print("✅ Opening Calculator...")
    except Exception as e:
        print(f"❌ {e}")


def open_explorer():
    try:
        os.startfile(FILE_EXPLORER_PATH)
        print("✅ Opening File Explorer...")
    except Exception as e:
        print(f"❌ {e}")


def open_browser():
    firefox = get_firefox()

    if firefox:
        subprocess.Popen([firefox])
        print(f"🦊 Opening {BROWSER_NAME}...")
    else:
        print(f"❌ {BROWSER_NAME} was not found on this PC.")