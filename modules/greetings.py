from config import ASSISTANT_NAME, VERSION


def welcome(owner):
    print("=" * 50)
    print(f"🤖 Welcome to {ASSISTANT_NAME}")
    print(f"Version: {VERSION}")
    print("=" * 50)

    if owner:
        print(f"\nHello, {owner}!")
    else:
        print("\nHello!")

    print(f"I am {ASSISTANT_NAME}.")
    print("Type 'help' to see available commands.")
    print()


def goodbye(owner):
    print()
    print(f"Goodbye, {owner}!")
    print("Have a wonderful day.")