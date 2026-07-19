"""
Jarvis-X Notes Module
"""

import os
from config import NOTES_FILE
from modules.ui import success, warning, error


def save_note(text):
    """Save a note to notes.txt"""

    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(text + "\n")

        success("Note saved successfully.")

    except Exception as e:
        error(str(e))


def show_notes():
    """Display all saved notes"""

    if not os.path.exists(NOTES_FILE):
        warning("No notes found.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()

    if not notes:
        warning("No notes available.")
        return

    print()
    print("=" * 45)
    print("               YOUR NOTES")
    print("=" * 45)

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")

    print("=" * 45)