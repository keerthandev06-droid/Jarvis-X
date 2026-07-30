"""
==========================================================
Jarvis-X Search Session
Version : 2.0.0
==========================================================

Purpose:
Maintains the active search session.
Stores the latest search results and tracks whether
Jarvis is currently waiting for a search selection.
"""

from typing import List, Optional, Tuple

# ==========================================================
# Session State
# ==========================================================

_ACTIVE = False

_QUERY = ""

_RESULTS: List[Tuple[str, str, str]] = []


# ==========================================================
# Session Management
# ==========================================================

def start(query: str, results: list):
    """
    Start a new search session.
    """

    global _ACTIVE
    global _QUERY
    global _RESULTS

    _ACTIVE = True
    _QUERY = query.strip()
    _RESULTS = list(results)


def clear():
    """
    Clear the current search session.
    """

    global _ACTIVE
    global _QUERY
    global _RESULTS

    _ACTIVE = False
    _QUERY = ""
    _RESULTS = []


# ==========================================================
# Status
# ==========================================================

def is_active() -> bool:
    """
    Returns True if a search session is active.
    """

    return _ACTIVE


def has_results() -> bool:
    """
    Returns True if results exist.
    """

    return len(_RESULTS) > 0


def result_count() -> int:
    """
    Returns number of search results.
    """

    return len(_RESULTS)


# ==========================================================
# Query
# ==========================================================

def get_query() -> str:
    """
    Returns the current search query.
    """

    return _QUERY


# ==========================================================
# Results
# ==========================================================

def get_results() -> list:
    """
    Returns all stored search results.
    """

    return _RESULTS.copy()


def get_result(index: int) -> Optional[Tuple[str, str, str]]:
    """
    Returns a single search result.
    Index is zero-based.
    """

    if index < 0:
        return None

    if index >= len(_RESULTS):
        return None

    return _RESULTS[index]


# ==========================================================
# Selection
# ==========================================================

def select(selection: str):
    """
    Process a user selection.

    Returns:

        ("cancel", None)

        ("selected", result)

        ("invalid", None)
    """

    value = selection.strip().lower()

    if value in (
        "q",
        "quit",
        "exit",
        "cancel",
    ):

        clear()

        return (
            "cancel",
            None,
        )

    if not value.isdigit():

        return (
            "invalid",
            None,
        )

    index = int(value) - 1

    result = get_result(index)

    if result is None:

        return (
            "invalid",
            None,
        )

    clear()

    return (
        "selected",
        result,
    )


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    sample = [
        ("Chrome", r"C:\Chrome.exe", "exe"),
        ("VS Code", r"C:\Code.exe", "exe"),
    ]

    start("chrome", sample)

    print(is_active())
    print(result_count())
    print(get_results())
    print(select("2"))