import os
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def current_time():
    return datetime.now().strftime("%I:%M:%S %p")


def current_date():
    return datetime.now().strftime("%d-%m-%Y")


def show_help():
    print("\n========== AVAILABLE COMMANDS ==========")
    print("hello              - Greet Jarvis-X")
    print("help               - Show commands")
    print("time               - Show current time")
    print("date               - Show current date")
    print("clear              - Clear screen")
    print("exit               - Exit Jarvis-X")
    print("========================================\n")