"""
Jarvis-X Search Engine
Version: 3.1.0

Core search engine used by:
- File Search
- App Launcher
- Voice Commands (future)
- AI Assistant (future)
"""

import os

# -----------------------------
# Configuration
# -----------------------------

DEBUG_SEARCH = False

# Completely hide these folders
HIDDEN_FOLDERS = (
    ".vscode",
    ".codex",
    "__pycache__",
    "node_modules",
    "appiconcache",
    "chromecodeverifyextension",
    "resources\\app\\extensions",
)

# Keep searchable, but lower their score
LOW_PRIORITY = (
    ".git",
    ".github",
    "temp",
    "cache",
    "logs",
    "build",
    "dist",
    "venv",
    "env",
)

JUNK_EXTENSIONS = (
    ".dll",
    ".pak",
    ".md5",
    ".tmp",
    ".log",
    ".cache",
)

APP_EXTENSIONS = (
    ".exe",
    ".lnk",
    ".bat",
    ".cmd",
)

HELPER_KEYWORDS = (
    "proxy",
    "launcher",
    "helper",
    "updater",
    "installer",
    "visualelements",
    "crash",
    "service",
    "broker",
    "elevation",
)

# -----------------------------
# Public API
# -----------------------------

def search(query, rows):
    rows = filter_results(rows)
    rows = sort_results(rows, query)
    rows = remove_duplicates(rows)
    return rows


# -----------------------------
# Internal Helpers
# -----------------------------

def filter_results(results):
    """
    Remove junk files and hidden folders.
    """

    filtered = []

    for result in results:
        name, path, item_type = result

        path = path.lower()
        extension = os.path.splitext(name)[1].lower()

        if extension in JUNK_EXTENSIONS:
            continue

        if any(folder in path for folder in HIDDEN_FOLDERS):
            continue

        filtered.append(result)

    return filtered

def remove_duplicates(results):
    """
    Remove duplicate paths.
    """

    seen = set()
    unique = []

    for result in results:
        _, path, _ = result

        path = path.lower()

        if path in seen:
            continue

        seen.add(path)
        unique.append(result)

    return unique


def classify_result(result):
    """
    Classify search result.
    """

    name, path, item_type = result

    name = name.lower()
    path = path.lower()

    extension = os.path.splitext(name)[1]

    if any(keyword in name for keyword in HELPER_KEYWORDS):
        return "helper"

    if extension == ".lnk":
        if "desktop" in path:
            return "application"

        if "start menu" in path:
            return "application"

        return "shortcut"

    if extension == ".exe":
        if "program files" in path:
            return "application"

        if "windowsapps" in path:
            return "application"

        return "executable"

    if item_type == "folder":
        return "folder"

    return "file"


def score_result(result, query):
    """
    Smart ranking algorithm.
    """

    name, path, item_type = result

    name = name.lower()
    path = path.lower()
    query = query.lower()

    score = 0

    # -------------------------
    # Name Matching
    # -------------------------

    filename = os.path.splitext(name)[0]

    if filename == query:
        score += 150
    elif filename.startswith(query):
        score += 100
    elif query in filename:
        score += 60

    # -------------------------
    # Category
    # -------------------------

    category = classify_result(result)

    if category == "application":
        score += 300

    elif category == "shortcut":
        score += 220

    elif category == "executable":
        score += 180

    elif category == "folder":
        score += 40

    elif category == "helper":
        score -= 150

    # -------------------------
    # Location Bonuses
    # -------------------------

    if "desktop" in path:
        score += 120

    if "start menu" in path:
        score += 100

    if "documents" in path:
        score += 40

    if "downloads" in path:
        score += 30

    if "pictures" in path:
        score += 20

    if "videos" in path:
        score += 20

    # -------------------------
    # Penalties
    # -------------------------

    if any(folder in path for folder in LOW_PRIORITY):
        score -= 80

    if "appdata\\local\\temp" in path:
        score -= 100

    if "cache" in path:
        score -= 80

    if "logs" in path:
        score -= 60

    return score


def sort_results(results, query):
    """
    Sort results by score.
    """

    sorted_results = sorted(
        results,
        key=lambda result: score_result(result, query),
        reverse=True,
    )

    if DEBUG_SEARCH:
        print("\n========== Search Debug ==========")

        for result in sorted_results[:10]:
            print(
                score_result(result, query),
                result[0],
                result[1]
            )

        print("==================================\n")

    return sorted_results