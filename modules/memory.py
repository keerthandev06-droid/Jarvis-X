import json
import os
from config import MEMORY_FILE


def load_memory():
    """Load memory from JSON file."""
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_memory(data):
    """Save memory to JSON file."""
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def get_owner():
    memory = load_memory()
    return memory.get("owner", None)


def set_owner(name):
    memory = load_memory()
    memory["owner"] = name.upper()
    save_memory(memory)