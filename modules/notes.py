"""
Jarvis-X Notes Module
"""

import os

from config import NOTES_FILE, NOTES_WIDTH, TEXT_ENCODING
from modules.ui import error, success, warning


def save_note(text):
    """Save a note to notes.txt"""

    try:
        with open(NOTES_FILE, "a", encoding=TEXT_ENCODING) as file:
            file.write(text + "\n")

        success("Note saved successfully.")

    except Exception as e:
        error(str(e))


def show_notes():
    """Display all saved notes"""

    if not os.path.exists(NOTES_FILE):
        warning("No notes found.")
        return

    with open(NOTES_FILE, "r", encoding=TEXT_ENCODING) as file:
        notes = file.readlines()

    if not notes:
        warning("No notes available.")
        return

    print()
    print("=" * NOTES_WIDTH)
    print("               YOUR NOTES")
    print("=" * NOTES_WIDTH)

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")

    print("=" * NOTES_WIDTH)