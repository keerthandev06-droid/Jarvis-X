"""
==========================================================
Jarvis-X Main Controller
Version : 2.0.0
==========================================================
"""

from config import EXIT_COMMANDS

from modules.memory import get_owner
from modules.commands import execute_command
from modules.utils import clear_screen
from modules.ui import banner
from modules.voice_v2 import listen
from modules.speaker import (
    startup,
    goodbye,
)

from core.session_manager import (
    is_active,
    current_type,
)


# ==========================================================
# Input Mode
# ==========================================================

def choose_mode():
    """
    Ask the user which input mode to use.
    """

    print("\nSelect Input Mode")
    print("1. Keyboard")
    print("2. Voice")

    while True:

        mode = input("\nChoose (1/2): ").strip()

        if mode in ("1", "2"):
            return mode

        print("❌ Invalid choice.")


# ==========================================================
# Read Input
# ==========================================================

def read_command(owner: str, mode: str) -> str:
    """
    Read one command from the selected input mode.
    """

    if mode == "1":
        return input(f"\n{owner} > ").strip()

    return listen().strip()


# ==========================================================
# Main Loop
# ==========================================================

def main():

    clear_screen()

    owner = get_owner() or "Boss"

    banner()

    print(f"\n👋 Welcome back, {owner}!")

    startup(owner)

    mode = choose_mode()

    while True:

        try:

            command = read_command(owner, mode)

            if not command:
                continue

            # -------------------------------------
            # Exit
            # -------------------------------------

            if command.lower() in EXIT_COMMANDS:

                goodbye()

                print("\n👋 Goodbye!")

                break

            # -------------------------------------
            # Session Info (Temporary)
            # -------------------------------------

            if is_active():

                print(
                    f"\n[Session Active: {current_type()}]"
                )

            # -------------------------------------
            # Execute
            # -------------------------------------

            execute_command(command)

        except KeyboardInterrupt:

            goodbye()

            print("\n\nInterrupted.")

            break

        except Exception as e:

            print(f"\nUnexpected Error: {e}")


# ==========================================================
# Entry
# ==========================================================

if __name__ == "__main__":
    main()