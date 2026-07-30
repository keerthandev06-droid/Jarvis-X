"""
==========================================================
Jarvis-X File Search Engine
Version : 3.0.0
==========================================================
"""

import os

from core.database import connect, create_table
from core.search_engine import search

from modules.ui import (
    success,
    warning,
)

# ==========================================================
# Configuration
# ==========================================================

MAX_RESULTS = 20

# ==========================================================
# Database Search
# ==========================================================

def search_items(query: str, limit: int = MAX_RESULTS):
    """
    Search indexed files and folders.
    """

    query = query.lower().strip()

    if not query:
        return []

    create_table()

    conn = connect()

    try:

        rows = conn.execute(
            """
            SELECT
                name,
                path,
                type
            FROM files
            WHERE lower(name) LIKE ?
            LIMIT 500
            """,
            (
                f"%{query}%",
            ),
        ).fetchall()

    finally:

        conn.close()

    rows = search(query, rows)

    return rows[:limit]


# ==========================================================
# Helpers
# ==========================================================

def open_result(result):
    """
    Open a single search result.
    """

    try:

        os.startfile(result[1])

        success(f"Opened: {result[0]}")

        return True

    except Exception as e:

        warning(str(e))

        return False


def print_results(results):
    """
    Display search results.
    """

    print()

    print("━" * 60)

    print(f"Found {len(results)} match(es)")

    print("━" * 60)

    for index, (name, path, item_type) in enumerate(
        results,
        start=1,
    ):

        icon = "📁" if item_type == "folder" else "📄"

        folder = os.path.basename(
            os.path.dirname(path)
        )

        print(f"[{index}] {icon} {name}")

        if folder:
            print(f"     {folder}")

        print()

    print("━" * 60)

    print("Select a number")

    print("q = cancel")

    print()
    # ==========================================================
# Open Best Match
# ==========================================================

def open_file(name):
    """
    Open the best matching file.
    """

    results = search_items(name, limit=1)

    if not results:
        return False

    return open_result(results[0])


# ==========================================================
# Interactive Search
# ==========================================================

def smart_find(name):
    """
    Search and interactively open files/folders.
    """

    results = search_items(name)

    if not results:

        warning("No matching files or folders found.")

        return

    # ------------------------------------------
    # Only one result
    # ------------------------------------------

    if len(results) == 1:

        print()

        print(f"📄 {results[0][0]}")

        print()

        open_result(results[0])

        return

    # ------------------------------------------
    # Multiple results
    # ------------------------------------------

    print_results(results)

    while True:

        choice = input("> ").strip()

        # --------------------------
        # Cancel
        # --------------------------

        if choice.lower() in (
            "q",
            "quit",
            "exit",
            "cancel",
        ):

            print()

            print("Search cancelled.")

            return

        # --------------------------
        # Invalid
        # --------------------------

        if not choice.isdigit():

            print("Enter a number or q.")

            continue

        index = int(choice)

        if index < 1 or index > len(results):

            print("Invalid selection.")

            continue

        print()

        open_result(results[index - 1])

        return