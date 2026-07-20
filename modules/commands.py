"""
Jarvis-X Command Processor
Version: 1.2.0
"""

from core.parser import normalize
from core.intents import detect_intent
from core.command_registry import COMMANDS
from core.resource_manager import open_resource
from core.logger import info, warning as log_warning, error as log_error

from modules.ui import warning


def execute_command(command):
    """
    Main Command Dispatcher
    """

    # Log user command
    info(f"User Command: {command}")

    normalized = normalize(command)

    intent, value = detect_intent(normalized)

    # ---------- OPEN RESOURCE ----------

    if intent in ("open_app", "open_file"):

        if open_resource(value):
            info(f"Opened Resource: {value}")
        else:
            warning(f'"{value}" not found.')
            log_warning(f'Resource Not Found: {value}')

        return

    # ---------- OTHER COMMANDS ----------

    handler = COMMANDS.get(intent)

    if handler is None:
        warning("Unknown command.")
        log_warning(f"Unknown Command: {command}")
        return

    try:
        if value:
            handler(value)
        else:
            handler()

        info(f"Executed Intent: {intent}")

    except TypeError:

        try:
            handler()
            info(f"Executed Intent: {intent}")
        except Exception as e:
            warning(str(e))
            log_error(str(e))

    except Exception as e:
        warning(str(e))
        log_error(str(e))