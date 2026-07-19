from modules.memory import get_owner
from modules.commands import execute_command
from modules.utils import clear_screen
from modules.ui import banner


def main():
    clear_screen()

    owner = get_owner()

    banner()

    print(f"\n👋 Welcome back, {owner}!")

    while True:
        command = input(f"\n{owner} > ").strip()

        if command == "":
            continue

        if command.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Goodbye!")
            break

        execute_command(command)


if __name__ == "__main__":
    main()