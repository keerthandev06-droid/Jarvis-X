"""
Jarvis-X UI Module
Handles all terminal output.
"""

from colorama import Fore, init

from config import BANNER_STATUS, BANNER_SUBTITLE, BANNER_TITLE, BANNER_WIDTH, VERSION

# Initialize Colorama
init(autoreset=True)


def banner():
    print(Fore.CYAN + "=" * BANNER_WIDTH)
    print(Fore.GREEN + BANNER_TITLE)
    print(Fore.YELLOW + BANNER_SUBTITLE)
    print(Fore.CYAN + "=" * BANNER_WIDTH)
    print(Fore.WHITE + f"Version : {VERSION}")
    print(Fore.WHITE + f"Status  : {BANNER_STATUS}")
    print(Fore.CYAN + "=" * BANNER_WIDTH)


def success(message):
    print(Fore.GREEN + "✅ " + message)


def error(message):
    print(Fore.RED + "❌ " + message)


def warning(message):
    print(Fore.YELLOW + "⚠️ " + message)


def info(message):
    print(Fore.CYAN + "ℹ️ " + message)


if __name__ == "__main__":
    banner()
    print()

    success("Jarvis-X started successfully.")
    info("Searching...")
    warning("No notes found.")
    error("Example error.")

    print()
    print(Fore.MAGENTA + "UI Module Test Completed!")