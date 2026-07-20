"""
Jarvis-X Search Engine
Version : 0.7

Responsible for:
- Database search
- Ranking results
- Filtering unwanted paths

This module DOES NOT:
- Print anything
- Ask for user input
- Open files
"""

import sqlite3
import os

from config import DATABASE_PATH


# Folders that should be pushed to the bottom of results
LOW_PRIORITY_PATHS = (
    ".vscode",
    ".codex",
    "__pycache__",
    "node_modules",
    "AppData\\Local\\Packages",
)


def _score_result(name, path, item_type, query):
    """
    Assign a score to each search result.
    Higher score = Higher position.
    """

    score = 0

    name_lower = name.lower()
    path_lower = path.lower()
    query_lower = query.lower()

    # Exact filename
    if name_lower == query_lower:
        score += 100

    # Starts with search text
    if name_lower.startswith(query_lower):
        score += 80

    # Contains search text
    if query_lower in name_lower:
        score += 40

    # Executables are important
    if name_lower.endswith(".exe"):
        score += 60

    # Folders are useful
    if item_type == "folder":
        score += 25

    # Useful document types
    if name_lower.endswith((".pdf", ".docx", ".xlsx", ".pptx", ".txt")):
        score += 20

    # Penalize developer/system folders
    for folder in LOW_PRIORITY_PATHS:
        if folder.lower() in path_lower:
            score -= 80

    return score


def search(query, limit=20):
    """
    Returns a ranked list of search results.

    Output:
    [
        {
            "name": "...",
            "path": "...",
            "type": "file",
            "score": 220
        }
    ]
    """

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, path, type
        FROM file_index
        WHERE name LIKE ?
        """,
        (f"%{query}%",)
    )

    rows = cursor.fetchall()
    conn.close()

    results = []

    for name, path, item_type in rows:

        score = _score_result(
            name=name,
            path=path,
            item_type=item_type,
            query=query
        )

        results.append({
            "name": name,
            "path": path,
            "type": item_type,
            "score": score
        })

    # Highest score first
    results.sort(
        key=lambda x: (-x["score"], x["name"].lower())
    )

    return results[:limit]