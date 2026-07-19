from modules.utils import (
    current_time,
    current_date,
    show_help,
    clear_screen,
)

from modules.browser import (
    google_search,
    youtube_search,
)

from modules.apps import (
    open_notepad,
    open_calculator,
    open_explorer,
    open_browser,
)

from modules.notes import (
    save_note,
    show_notes,
)


def execute_command(command):

    text = command.lower().strip()

    # ---------------- HELP ----------------

    if text == "help":
        show_help()
        return

    # ---------------- TIME ----------------

    if "time" in text:
        current_time()
        return

    # ---------------- DATE ----------------

    if "date" in text:
        current_date()
        return

    # ---------------- CLEAR ----------------

    if text == "clear":
        clear_screen()
        return

    # ---------------- OPEN APPS ----------------

    if "notepad" in text:
        open_notepad()
        return

    if "calculator" in text or "calc" in text:
        open_calculator()
        return

    if "explorer" in text or "file explorer" in text:
        open_explorer()
        return

    if "browser" in text or "firefox" in text:
        open_browser()
        return

    # ---------------- GOOGLE ----------------

    if text.startswith("google "):
        google_search(command[7:])
        return

    if text.startswith("search google "):
        google_search(command[14:])
        return

    # ---------------- YOUTUBE ----------------

    if text.startswith("youtube "):
        youtube_search(command[8:])
        return

    if text.startswith("search youtube "):
        youtube_search(command[15:])
        return

    # ---------------- NOTES ----------------

    if text.startswith("note "):
        save_note(command[5:])
        return

    if text.startswith("save note "):
        save_note(command[10:])
        return

    if text == "notes":
        show_notes()
        return

    # ---------------- UNKNOWN ----------------

    print("\n❌ I don't understand that command.")
    print("Type 'help' to see available commands.")