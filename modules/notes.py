import os
from config import NOTES_FILE


def save_note(text):
    """Save a note to notes.txt"""
    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(text + "\n")

        print("✅ Note saved successfully.")

    except Exception as e:
        print(f"❌ Error: {e}")


def show_notes():
    """Display all saved notes"""

    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()

    if not notes:
        print("No notes available.")
        return

    print("\n========== YOUR NOTES ==========\n")

    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")

    print("\n===============================\n")