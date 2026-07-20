"""
Jarvis-X Resource Manager
Version: 1.1.0
"""

from modules.app_launcher import open_app
from modules.file_search import open_file


def open_resource(name):
    """
    Try opening an application first.
    If that fails, try opening a file/folder.
    """

    try:
        result = open_app(name)

        if result:
            return True

    except Exception:
        pass

    try:
        result = open_file(name)

        if result:
            return True

    except Exception:
        pass

    return False