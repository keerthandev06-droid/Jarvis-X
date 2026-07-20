import shutil
import subprocess

from config import (
    BROWSER_EXECUTABLE,
    BROWSER_NAME,
    BROWSER_PATHS,
    GOOGLE_HOMEPAGE_URL,
    GOOGLE_URL,
    SEARCH_SPACE_REPLACEMENT,
    YOUTUBE_URL,
)


def get_firefox():
    """Find the configured browser automatically."""
    firefox = shutil.which(BROWSER_EXECUTABLE)

    if firefox:
        return firefox

    for path in BROWSER_PATHS:
        try:
            with open(path):
                pass
            return path
        except Exception:
            continue

    return None


def open_url(url):
    firefox = get_firefox()

    if firefox:
        subprocess.Popen([firefox, url])
    else:
        print(f"❌ {BROWSER_NAME} was not found on this PC.")


def google_search(query):
    if not query.strip():
        print("❌ Please enter a search.")
        return

    open_url(f"{GOOGLE_URL}{query.replace(' ', SEARCH_SPACE_REPLACEMENT)}")
    print(f"🔍 Searching Google for: {query}")


def youtube_search(query):
    if not query.strip():
        print("❌ Please enter a search.")
        return

    open_url(f"{YOUTUBE_URL}{query.replace(' ', SEARCH_SPACE_REPLACEMENT)}")
    print(f"▶️ Searching YouTube for: {query}")


def open_homepage():
    open_url(GOOGLE_HOMEPAGE_URL)
    print(f"🦊 Opening {BROWSER_NAME}...")