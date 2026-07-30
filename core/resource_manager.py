"""
Jarvis-X Resource Manager
Version: 1.3.0
"""

import re

from modules.app_launcher import open_app
from modules.file_search import open_file


def open_resource(name):
    """
    Open one or multiple applications/files.

    Supports:

    open chrome
    open chrome and vscode
    open chrome, wa and tg
    open chrome,wa,calc
    """

    # Split on commas or the word "and"
    resources = [
        item.strip()
        for item in re.split(
            r"\s*(?:,|\band\b)\s*",
            name,
            flags=re.IGNORECASE,
        )
        if item.strip()
    ]

    opened = False

    for resource in resources:

        # Try opening as application
        try:
            if open_app(resource):
                opened = True
                continue
        except Exception:
            pass

        # Try opening as file/folder
        try:
            if open_file(resource):
                opened = True
                continue
        except Exception:
            pass

    return opened