"""
Jarvis-X Index Builder
Version: 2.0.0
"""

import os

from config import (
    INDEX_BATCH_SIZE,
    INDEX_PROGRESS_TEMPLATE,
    SCAN_DRIVES,
    SKIP_FOLDERS,
    SKIP_PATHS,
    IGNORE_FOLDERS,
    IGNORE_EXTENSIONS,
)
from core.database import connect, create_table

# Compatibility aliases for callers that access index settings directly.
DRIVES = SCAN_DRIVES
BATCH_SIZE = INDEX_BATCH_SIZE


def handle_walk_error(error):
    """Ignore folders Windows does not allow Jarvis-X to read."""
    if isinstance(error, OSError):
        return


def flush_batch(cursor, batch):
    """Write one batch of indexed items to SQLite."""
    if not batch:
        return

    cursor.executemany(
        """
        INSERT INTO files(name, path, type, extension)
        VALUES (?, ?, ?, ?)
        """,
        batch,
    )

    batch.clear()


def build_index():
    """
    Scan all configured drives and save the index to SQLite.
    """

    create_table()

    conn = connect()
    cursor = conn.cursor()

    total_files = 0
    total_folders = 0
    batch = []

    print("\nScanning drives...\n")

    try:
        with conn:
            # Clear old index
            cursor.execute("DELETE FROM files")

            for drive in DRIVES:

                try:
                    if not os.path.exists(drive):
                        continue
                except OSError:
                    continue

                print(f"Scanning {drive}")

                for root, dirs, files in os.walk(
                    drive,
                    onerror=handle_walk_error,
                ):

                    # Current directory being scanned
                    current_root = root.lower()

                    # ---------------- DEBUG ----------------
                    # Skip entire directory trees
                    if any(skip in current_root for skip in SKIP_PATHS):
                        dirs[:] = []
                        continue

                    # ---------------- FOLDERS ----------------
                    filtered_dirs = []

                    for folder in dirs:
                        folder_name = folder.lower()

                        if folder_name in SKIP_FOLDERS:
                            continue

                        if folder_name in IGNORE_FOLDERS:
                            continue

                        filtered_dirs.append(folder)

                    dirs[:] = filtered_dirs

                    # Index folders
                    for folder in dirs:
                        batch.append(
                            (
                                folder.lower(),
                                os.path.join(root, folder),
                                "folder",
                                "",
                            )
                        )

                        total_folders += 1

                    # ---------------- FILES ----------------
                    for file in files:

                        extension = os.path.splitext(file)[1].lower()

                        if extension in IGNORE_EXTENSIONS:
                            continue

                        batch.append(
                            (
                                file.lower(),
                                os.path.join(root, file),
                                "file",
                                extension,
                            )
                        )

                        total_files += 1

                    # Flush batch
                    if len(batch) >= BATCH_SIZE:
                        flush_batch(cursor, batch)

                        print(
                            INDEX_PROGRESS_TEMPLATE.format(
                                count=total_files + total_folders
                            ),
                            end="",
                            flush=True,
                        )
    finally:
        conn.close()

    print("\n===================================")
    print("Database index created successfully")
    print("-----------------------------------")
    print(f"Files   : {total_files}")
    print(f"Folders : {total_folders}")
    print(f"Total   : {total_files + total_folders}")
    print("===================================\n")


if __name__ == "__main__":
    build_index()