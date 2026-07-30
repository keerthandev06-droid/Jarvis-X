"""
==========================================================
Jarvis-X Folder Manager
Version : 2.0.0
==========================================================
"""

import os


HOME = os.path.expanduser("~")

FOLDERS = {
    "desktop": os.path.join(HOME, "Desktop"),
    "downloads": os.path.join(HOME, "Downloads"),
    "documents": os.path.join(HOME, "Documents"),
    "pictures": os.path.join(HOME, "Pictures"),
    "videos": os.path.join(HOME, "Videos"),
    "music": os.path.join(HOME, "Music"),
}


def open_folder(name: str):

    name = name.lower().strip()

    path = FOLDERS.get(name)

    if not path:
        return False

    if not os.path.exists(path):
        print(f"❌ Folder not found:\n{path}")
        return False

    os.startfile(path)

    print(f"✅ Opened {name}")

    return True


def open_desktop():
    return open_folder("desktop")


def open_downloads():
    return open_folder("downloads")


def open_documents():
    return open_folder("documents")


def open_pictures():
    return open_folder("pictures")


def open_videos():
    return open_folder("videos")


def open_music():
    return open_folder("music")


FOLDER_COMMANDS = {
    "desktop": open_desktop,
    "downloads": open_downloads,
    "documents": open_documents,
    "pictures": open_pictures,
    "videos": open_videos,
    "music": open_music,
}


if __name__ == "__main__":

    for folder in FOLDER_COMMANDS:
        print(folder)