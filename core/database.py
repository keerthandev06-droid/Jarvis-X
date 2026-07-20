import sqlite3

from config import DATABASE_PATH

# Compatibility alias for callers that access the database path directly.
DB_PATH = DATABASE_PATH


def connect():
    """
    Create and return a database connection.
    """
    DB_PATH.parent.mkdir(exist_ok=True)

    return sqlite3.connect(DB_PATH)


def create_table():
    """
    Create the files table and search indexes if they don't exist.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            path TEXT NOT NULL,
            type TEXT NOT NULL,
            extension TEXT
        )
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_files_name_type
        ON files(name, type)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_files_type_name
        ON files(type, name)
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("Database initialized successfully.")