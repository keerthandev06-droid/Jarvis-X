"""
Jarvis-X File Search Engine
Version: 2.2.0
"""

import os

from core.database import connect, create_table
from core.search_engine import search
from modules.ui import success, warning

LOW_PRIORITY = (
    ".vscode",
    ".codex",
    "appdata",
    "__pycache__",
    "node_modules",
    ".git",
    "temp",
    "cache",
    "logs",
    "build",
    "dist",
    "venv",
    "env",
)

EXT_SCORES = {
    ".exe": 80,
    ".lnk": 60,
    ".bat": 40,
    ".cmd": 40,
    ".url": 30,
}


def _score(name, path, item_type, query):
    """
    Calculate ranking score for a search result.
    Higher score = higher in results.
    """
    n = name.lower()
    p = path.lower()

    score = 0

    # ---------- Name Matching ----------

    if n == query:
        score += 120
    elif n.startswith(query):
        score += 90
    elif query in n:
        score += 50

    # ---------- File Type ----------

    if item_type == "folder":
        score += 10
    else:
        extension = os.path.splitext(n)[1]
        score += EXT_SCORES.get(extension, 0)

    # ---------- Preferred Locations ----------

    if "start menu" in p:
        score += 80

    if "windowsapps" in p:
        score += 40

    if "desktop" in p:
        score += 30

    if "program files" in p:
        score += 30

    if p.startswith(r"c:\python"):
        score += 30

    # ---------- Low Priority ----------

    for bad in LOW_PRIORITY:
        if bad in p:
            score -= 100

    return score


def search_items(name, limit=20):
    """
    Search indexed files/folders and return
    ranked results.
    """
    query = name.lower().strip()

    create_table()

    conn = connect()

    try:
        rows = conn.cursor().execute(
            """
            SELECT name, path, type
            FROM files
            WHERE lower(name) LIKE ?
            LIMIT 500
            """,
            (f"%{query}%",),
        ).fetchall()

    finally:
        conn.close()

        # ---------- Smart Search Engine ----------

    rows = search(query, rows)

    return rows[:limit]


def open_file(name):
    """
    Open the highest-ranked matching file.
    """
    results = search_items(name, limit=1)

    if not results:
        return False

    try:
        os.startfile(results[0][1])
        success(f"Opened: {results[0][0]}")
        return True
    except Exception:
        return False


def smart_find(name):
    """
    Search and interactively open indexed files/folders.
    """
    results = search_items(name)

    if not results:
        warning("No matching files or folders found.")
        return

    print()
    print("=" * 60)
    print(f"Search Results ({len(results)})")
    print("=" * 60)

    for i, (filename, path, item_type) in enumerate(results, start=1):
        label = "📁 Folder" if item_type == "folder" else "📄 File"

        print(f"{i}. {filename}")
        print(f"   {label}")
        print(f"   {path}")
        print()

    while True:
        choice = input(f"Select 1-{len(results)} or 0 to cancel: ").strip()

        if choice == "0":
            print("Cancelled.")
            return

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        index = int(choice)

        if not 1 <= index <= len(results):
            print("Invalid selection.")
            continue

        try:
            os.startfile(results[index - 1][1])
            success(f"Opened: {results[index - 1][0]}")
            return
        except Exception as e:
            warning(f"Unable to open the selected item: {e}")
            return