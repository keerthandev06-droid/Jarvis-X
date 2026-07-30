"""
==========================================================
Jarvis-X Search Session
Version : 1.0.0
==========================================================

Purpose:
Stores the latest search results so the user can
open them later without repeating the search.
"""

LAST_QUERY = ""
LAST_RESULTS = []


def save_results(query: str, results: list):
    """
    Save the latest search results.
    """

    global LAST_QUERY
    global LAST_RESULTS

    LAST_QUERY = query
    LAST_RESULTS = results


def get_results():
    """
    Return the latest search results.
    """

    return LAST_RESULTS


def get_query():
    """
    Return the latest search query.
    """

    return LAST_QUERY


def clear():
    """
    Clear search session.
    """

    global LAST_QUERY
    global LAST_RESULTS

    LAST_QUERY = ""
    LAST_RESULTS = []


def has_results() -> bool:
    """
    Check whether search results exist.
    """

    return len(LAST_RESULTS) > 0


def get_result(index: int):
    """
    Return a result by index.

    Index is zero-based.
    """

    if index < 0:
        return None

    if index >= len(LAST_RESULTS):
        return None

    return LAST_RESULTS[index]


if __name__ == "__main__":

    sample = [
        ("Chrome", "C:\\Chrome.exe", "file"),
        ("VS Code", "C:\\Code.exe", "file"),
    ]

    save_results("chrome", sample)

    print(get_query())
    print(get_results())
    print(get_result(0))