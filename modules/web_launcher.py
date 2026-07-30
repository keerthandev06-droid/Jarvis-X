"""
Jarvis-X Website Launcher
Version: 2.0.0
"""

from core.browser_manager import open_url
from core.website_resolver import resolve_website
from modules.ui import success, warning


def open_website(name: str) -> bool:
    """
    Opens a website in the correct browser.
    """

    website = resolve_website(name)

    if not website:
        return False

    if open_url(
        website["url"],
        website["browser"]
    ):
        success(f"Opening {name}...")
        return True

    warning(f"Failed to open {name}")
    return False