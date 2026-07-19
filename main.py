from modules.memory import get_owner
from modules.greetings import welcome, goodbye
from modules.commands import execute_command
from modules.utils import clear_screen


def main():
    clear_screen()

    owner = get_owner()
    welcome(owner)

    while True:
        command = input(f"\n{owner} > ").strip()

        if command == "":
            continue

        if command.lower() in ["exit", "quit", "bye"]:
            goodbye(owner)
            break

        execute_command(command)


if __name__ == "__main__":
    main()