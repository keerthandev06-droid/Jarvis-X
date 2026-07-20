"""
Jarvis-X Utility Functions
Version: 1.2.1
"""

import os
from datetime import datetime

from config import (
    DATE_FORMAT,
    HELP_COMMANDS,
    HELP_WIDTH,
    OTHER_CLEAR_COMMAND,
    TIME_FORMAT,
    WINDOWS_CLEAR_COMMAND,
)
from modules.ui import info


# ---------------- CLEAR SCREEN ---------------- #

def clear_screen():
    os.system(WINDOWS_CLEAR_COMMAND if os.name == "nt" else OTHER_CLEAR_COMMAND)


# ---------------- TIME ---------------- #

def current_time():
    current = datetime.now().strftime(TIME_FORMAT)
    info(f"Current Time : {current}")


# ---------------- DATE ---------------- #

def current_date():
    current = datetime.now().strftime(DATE_FORMAT)
    info(f"Current Date : {current}")


# ---------------- HELP ---------------- #

def show_help():
    print("\n============= AVAILABLE COMMANDS =============")

    for command, description in HELP_COMMANDS:
        print(f"{command:<20} - {description}")

    print("=" * HELP_WIDTH)