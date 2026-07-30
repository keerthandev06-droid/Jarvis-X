"""
Jarvis-X Application Database
"""

from core.database import connect
from modules.app_aliases import APP_ALIASES


def save_app(name, path, app_type):
    """
    Save an application if it doesn't already exist.
    """

    name = name.lower().strip()

    # Skip duplicates
    if app_exists(name):
        return

    with connect() as conn:
        conn.execute(
            """
            INSERT INTO applications
            (name, path, type)
            VALUES (?, ?, ?)
            """,
            (
                name,
                path,
                app_type.lower(),
            ),
        )


def get_app(name):
    with connect() as conn:
        return conn.execute(
            """
            SELECT path, type
            FROM applications
            WHERE name = ?
            """,
            (name.lower().strip(),),
        ).fetchone()


def search_app(keyword):
    """
    Search applications using aliases + partial matching.
    """

    keyword = keyword.lower().strip()

    # Convert aliases
    keyword = APP_ALIASES.get(keyword, keyword)

    with connect() as conn:

        return conn.execute(
            """
            SELECT DISTINCT name, path, type
            FROM applications
            WHERE name LIKE ?
            ORDER BY
                CASE
                    WHEN name = ? THEN 0
                    WHEN name LIKE ? THEN 1
                    ELSE 2
                END,
                LENGTH(name)
            LIMIT 10
            """,
            (
                f"%{keyword}%",
                keyword,
                f"{keyword}%",
            ),
        ).fetchall()


def get_all_apps():
    with connect() as conn:
        return conn.execute(
            """
            SELECT id, name, path, type
            FROM applications
            ORDER BY name
            """
        ).fetchall()


def clear_apps():
    with connect() as conn:
        conn.execute("DELETE FROM applications")


def app_exists(name):
    with connect() as conn:
        row = conn.execute(
            """
            SELECT 1
            FROM applications
            WHERE name = ?
            LIMIT 1
            """,
            (name.lower().strip(),),
        ).fetchone()

    return row is not None