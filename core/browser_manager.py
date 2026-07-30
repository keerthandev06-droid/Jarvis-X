"""
Jarvis-X Browser Manager
Version: 1.0.0
"""

import subprocess

FIREFOX = r"C:\Program Files\Mozilla Firefox\firefox.exe"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def open_url(url: str, browser: str = "personal") -> bool:
    """
    Opens a URL in the selected browser.
    """

    try:

        if browser == "work":
            subprocess.Popen([CHROME, url])

        else:
            subprocess.Popen([FIREFOX, url])

        return True

    except Exception as e:
        print(e)
        return False