"""
Jarvis-X Utility Functions
Version: 3.0.0
"""

import os
from datetime import datetime


def current_time():
    """
    Display current time.
    """
    print(
        f"ℹ️ Current Time : "
        f"{datetime.now().strftime('%I:%M:%S %p')}"
    )


def current_date():
    """
    Display current date.
    """
    print(
        f"ℹ️ Current Date : "
        f"{datetime.now().strftime('%d-%m-%Y')}"
    )


def clear_screen():
    """
    Clear console.
    """
    os.system("cls")


def show_help():
    """
    Display all available commands.
    """

    print()

    print("=" * 55)
    print("              AVAILABLE COMMANDS")
    print("=" * 55)

    print()
    print("GENERAL")
    print("-" * 55)
    print("help                     Show help")
    print("time                     Current time")
    print("date                     Current date")
    print("clear                    Clear screen")

    print()
    print("APPLICATIONS")
    print("-" * 55)
    print("open <app>               Open application")
    print("open <file>              Open file")
    print("find <name>              Search files")

    print()
    print("WEB")
    print("-" * 55)
    print("google <query>           Google Search")
    print("youtube <query>          YouTube Search")

    print()
    print("NOTES")
    print("-" * 55)
    print("note <text>              Save note")
    print("notes                    Show notes")

    print()
    print("POWER")
    print("-" * 55)
    print("shutdown                 Shutdown PC")
    print("restart                  Restart PC")
    print("cancel shutdown          Cancel Shutdown")
    print("lock                     Lock Computer")
    print("sleep                    Sleep Computer")
    print("logoff                   Log Off")

    print()
    print("MAINTENANCE")
    print("-" * 55)
    print("reindex                  Rebuild File Index")
    print("rebuild_apps             Rebuild App Database")

    print()
    print("AI")
    print("-" * 55)
    print("Ask anything naturally")
    print("Example:")
    print("What is Python?")
    print("Latest AI news")
    print("Jana Nayagan collection today")

    print()
    print("=" * 55)