"""
Jarvis-X Application Manager
"""

from modules.app_database import clear_apps
from modules.app_scanner import scan_apps
from modules.ui import success


def rebuild_apps():
    """
    Rebuild the application database.
    """

    print("Rebuilding application database...\n")

    clear_apps()
    scan_apps()

    success("Application database rebuilt successfully!")