"""
==========================================================
Jarvis-X Workflow Engine
Version : 1.0.0
==========================================================
"""

from modules.app_launcher import open_app
from modules.system.folders import (
    open_downloads,
    open_documents,
)
from modules.browser import google_search


def work_mode():

    open_app("chrome")
    open_app("vscode")
    open_documents()

    return True


def study_mode():

    open_app("chrome")
    google_search("Python documentation")
    open_documents()

    return True


def movie_mode():

    open_app("vlc")

    return True


def gaming_mode():

    open_app("steam")

    return True


WORKFLOWS = {
    "work mode": work_mode,
    "study mode": study_mode,
    "movie mode": movie_mode,
    "gaming mode": gaming_mode,
}