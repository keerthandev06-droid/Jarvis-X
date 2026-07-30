"""
==========================================================
Jarvis-X Main Controller
Version : 1.0.0
==========================================================
"""

from config import EXIT_COMMANDS

from modules.memory import get_owner
from modules.commands import execute_command
from modules.utils import clear_screen
from modules.ui import banner

# Use the new smart voice engine
from modules.voice_v2 import listen

# Speaker
from modules.speaker import (
    startup,
    goodbye,
)


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


def main():

    clear_screen()

    owner = get_owner() or "Boss"

    banner()

    print(f"\n👋 Welcome back, {owner}!")

    startup(owner)

    mode = choose_mode()

    while True:

        try:

            if mode == "1":

                command = input(f"\n{owner} > ").strip()

            else:

                command = listen()

            if not command:
                continue

            command = command.strip()

            if command.lower() in EXIT_COMMANDS:

                goodbye()

                print("\n👋 Goodbye!")

                break

            execute_command(command)

        except KeyboardInterrupt:

            goodbye()

            print("\n\nInterrupted.")

            break

        except Exception as e:

            print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()