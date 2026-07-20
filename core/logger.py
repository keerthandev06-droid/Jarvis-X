"""
Jarvis-X Logger
Version: 1.2.0
"""

from datetime import datetime

from config import LOG_FILE, LOG_FOLDER, LOG_TIMESTAMP_FORMAT, TEXT_ENCODING

LOG_FOLDER.mkdir(exist_ok=True)


def log(level, message):
    timestamp = datetime.now().strftime(LOG_TIMESTAMP_FORMAT)

    with open(LOG_FILE, "a", encoding=TEXT_ENCODING) as file:
        file.write(f"[{timestamp}] [{level}] {message}\n")


def info(message):
    log("INFO", message)


def warning(message):
    log("WARNING", message)


def error(message):
    log("ERROR", message)