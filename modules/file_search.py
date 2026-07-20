"""
Jarvis-X File Search Engine
Version: 2.1.0
"""

import os

from core.database import connect, create_table
from modules.ui import success, warning

LOW_PRIORITY = (
    ".vscode",
    ".codex",
    "appdata",
    "__pycache__",
    "node_modules",
)

EXT_SCORES = {
    ".exe": 60,
    ".lnk": 40,
    ".bat": 35,
    ".cmd": 35,
}


def _score(name, path, item_type, query):
    n = name.lower()
    p = path.lower()
    score = 0

    if n == query:
        score += 100
    elif n.startswith(query):
        score += 80
    elif query in n:
        score += 40

    if item_type == "folder":
        score += 15
    else:
        score += EXT_SCORES.get(os.path.splitext(n)[1], 0)

    for bad in LOW_PRIORITY:
        if bad in p:
            score -= 80

    if "program files" in p or p.startswith(r"c:\python"):
        score += 25

    return score


def search_items(name, limit=20):
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

    rows = sorted(
        rows,
        key=lambda r: (-_score(r[0], r[1], r[2], query), r[0].lower()),
    )

    return rows[:limit]


def open_file(name):
    results = search_items(name, 1)

    if not results:
        return False

    try:
        os.startfile(results[0][1])
        success(f"Opened: {results[0][0]}")
        return True
    except Exception:
        return False


def smart_find(name):
    results = search_items(name)

    if not results:
        warning("No matching files or folders found.")
        return

    print()
    print("=" * 60)
    print(f"Search Results ({len(results)})")
    print("=" * 60)

    for i, (filename, path, item_type) in enumerate(results, 1):
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

        idx = int(choice)

        if not 1 <= idx <= len(results):
            print("Invalid selection.")
            continue

        try:
            os.startfile(results[idx - 1][1])
            success(f"Opened: {results[idx - 1][0]}")
            return
        except Exception:
            warning("Unable to open the selected item.")
            return
