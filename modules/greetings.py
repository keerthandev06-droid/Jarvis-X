from config import ASSISTANT_NAME, GREETING_WIDTH, VERSION


def welcome(owner):
    print("=" * GREETING_WIDTH)
    print(f"🤖 Welcome to {ASSISTANT_NAME}")
    print(f"Version: {VERSION}")
    print("=" * GREETING_WIDTH)

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