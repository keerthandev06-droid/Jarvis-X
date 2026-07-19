import os
import shutil
import subprocess


def get_firefox():
    firefox = shutil.which("firefox")

    if firefox:
        return firefox

    possible_paths = [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    return None


def open_notepad():
    try:
        subprocess.Popen("notepad.exe")
        print("✅ Opening Notepad...")
    except Exception as e:
        print(f"❌ {e}")


def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        print("✅ Opening Calculator...")
    except Exception as e:
        print(f"❌ {e}")


def open_explorer():
    try:
        os.startfile("C:\\")
        print("✅ Opening File Explorer...")
    except Exception as e:
        print(f"❌ {e}")


def open_browser():
    firefox = get_firefox()

    if firefox:
        subprocess.Popen([firefox])
        print("🦊 Opening Firefox...")
    else:
        print("❌ Firefox was not found on this PC.")