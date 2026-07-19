"""
Jarvis-X UI Module
Handles all terminal output.
"""

from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)


def banner():
    print(Fore.CYAN + "=" * 55)
    print(Fore.GREEN + "               🤖 JARVIS-X")
    print(Fore.YELLOW + "          Personal AI Assistant")
    print(Fore.CYAN + "=" * 55)
    print(Fore.WHITE + "Version : 0.6")
    print(Fore.WHITE + "Status  : READY")
    print(Fore.CYAN + "=" * 55)


def success(message):
    print(Fore.GREEN + "✅ " + message)


def error(message):
    print(Fore.RED + "❌ " + message)


def warning(message):
    print(Fore.YELLOW + "⚠️ " + message)


def info(message):
    print(Fore.CYAN + "ℹ️ " + message)


# -----------------------------
# Test UI Module
# -----------------------------
if __name__ == "__main__":
    banner()
    print()

    success("Jarvis-X started successfully.")
    info("Searching...")
    warning("No notes found.")
    error("Example error.")

    print()
    print(Fore.MAGENTA + "UI Module Test Completed!")