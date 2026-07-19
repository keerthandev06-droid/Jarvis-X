import shutil
import subprocess


def get_firefox():
    """Find Firefox automatically."""
    firefox = shutil.which("firefox")

    if firefox:
        return firefox

    possible_paths = [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
    ]

    for path in possible_paths:
        try:
            with open(path):
                pass
            return path
        except:
            continue

    return None


def open_url(url):
    firefox = get_firefox()

    if firefox:
        subprocess.Popen([firefox, url])
    else:
        print("❌ Firefox was not found on this PC.")


def google_search(query):
    if not query.strip():
        print("❌ Please enter a search.")
        return

    open_url(f"https://www.google.com/search?q={query.replace(' ', '+')}")
    print(f"🔍 Searching Google for: {query}")


def youtube_search(query):
    if not query.strip():
        print("❌ Please enter a search.")
        return

    open_url(f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}")
    print(f"▶️ Searching YouTube for: {query}")


def open_homepage():
    open_url("https://www.google.com")
    print("🦊 Opening Firefox...")