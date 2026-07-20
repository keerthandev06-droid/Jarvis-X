"""
Central configuration for Jarvis-X.
Cleaned version - v0.7 Compatible
"""

import os
from pathlib import Path

# ==========================================================
# Project
# ==========================================================

PROJECT_NAME = "Jarvis-X"
ASSISTANT_NAME = "Jarvis-X"
OWNER_NAME = "BOSS"
VERSION = "0.7"

# ==========================================================
# Paths
# ==========================================================

DATA_FOLDER = Path("data")
LOG_FOLDER = Path("logs")

DATABASE_PATH = DATA_FOLDER / "file_index.db"
NOTES_FILE = DATA_FOLDER / "notes.txt"
MEMORY_FILE = DATA_FOLDER / "memory.json"
LOG_FILE = LOG_FOLDER / "jarvis.log"

TEXT_ENCODING = "utf-8"
JSON_INDENT = 4

# ==========================================================
# Browser
# ==========================================================

BROWSER_NAME = "Firefox"
BROWSER_EXECUTABLE = "firefox"

BROWSER_PATHS = (
    r"C:\Program Files\Mozilla Firefox\firefox.exe",
    r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
)

GOOGLE_HOMEPAGE_URL = "https://www.google.com"
GOOGLE_URL = "https://www.google.com/search?q="
YOUTUBE_URL = "https://www.youtube.com/results?search_query="
SEARCH_SPACE_REPLACEMENT = "+"

# ==========================================================
# Applications
# ==========================================================

APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "explorer": "explorer.exe",
    "firefox": [BROWSER_EXECUTABLE, *BROWSER_PATHS],
    "vscode": [
        "Code.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"),
        r"C:\Program Files\Microsoft VS Code\Code.exe",
    ],
}

FILE_EXPLORER_PATH = "C:\\"

# ==========================================================
# Indexing
# ==========================================================

SCAN_DRIVES = ("C:\\","D:\\","E:\\","F:\\")

SKIP_FOLDERS = {
    "windows",
    "program files",
    "program files (x86)",
    "programdata",
    "$recycle.bin",
    "system volume information",
}

INDEX_BATCH_SIZE = 1000
INDEX_ITEM_TYPES = ("file","folder")
INDEX_PROGRESS_TEMPLATE = "\rIndexed {count} items..."

# ==========================================================
# Smart Search
# ==========================================================

SEARCH_RESULT_LIMIT = 10

IGNORE_FOLDERS = {
    "__pycache__",
    ".git",
    ".venv",
    "node_modules",
}

IGNORE_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".tmp",
    ".log",
}

PRIORITY_EXTENSIONS = (
    ".exe",".lnk",".pdf",".docx",".xlsx",".pptx",".txt",
)

# ==========================================================
# Parser
# ==========================================================

ACTION_WORDS = {
    "open": ("open","launch","start","run"),
}

FILLER_WORDS = {
    "please","can","could","would","you","me","for",
    "the","a","an","to","my","i","want","need","kindly",
}

FILE_EXTENSIONS = (
    ".txt",".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",
    ".jpg",".jpeg",".png",".gif",".bmp",".webp",
    ".mp3",".wav",".mp4",".mkv",
    ".zip",".rar",".7z",".py",
)

EXIT_COMMANDS = ("exit","quit","bye")

TIME_FORMAT = "%I:%M:%S %p"
DATE_FORMAT = "%d-%m-%Y"

WINDOWS_CLEAR_COMMAND = "cls"
OTHER_CLEAR_COMMAND = "clear"

# ==========================================================
# Logging
# ==========================================================

LOG_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

# ==========================================================
# UI
# ==========================================================

BANNER_WIDTH = 55
BANNER_TITLE = "               🤖 JARVIS-X"
BANNER_SUBTITLE = "          Personal AI Assistant"
BANNER_STATUS = "READY"

GREETING_WIDTH = 50
HELP_WIDTH = 45
NOTES_WIDTH = 45

HELP_COMMANDS = (
    ("help","Show available commands"),
    ("time","Show current time"),
    ("date","Show current date"),
    ("clear","Clear screen"),
    ("open <app/file>","Open application or file"),
    ("find <name>","Search indexed files"),
    ("google <query>","Search Google"),
    ("youtube <query>","Search YouTube"),
    ("note <text>","Save note"),
    ("notes","Show notes"),
    ("reindex","Rebuild file index"),
    ("exit","Exit Jarvis-X"),
)
