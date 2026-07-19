from modules.utils import (
    current_time,
    current_date,
    show_help,
    clear_screen,
)

from modules.browser import google_search, youtube_search
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
    cmd = command.lower()

    if cmd == "help":
        show_help()

    elif cmd == "time":
        current_time()

    elif cmd == "date":
        current_date()

    elif cmd == "clear":
        clear_screen()

    elif cmd == "notepad":
        open_notepad()

    elif cmd == "calculator":
        open_calculator()

    elif cmd == "explorer":
        open_explorer()

    elif cmd == "browser":
        open_browser()

    elif cmd.startswith("google "):
        query = command[7:]
        google_search(query)

    elif cmd.startswith("youtube "):
        query = command[8:]
        youtube_search(query)

    elif cmd.startswith("note "):
        text = command[5:]
        save_note(text)

    elif cmd == "notes":
        show_notes()

    else:
        print("\n❌ Unknown command.")
        print("Type 'help' to see available commands.")