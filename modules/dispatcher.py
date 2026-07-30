"""
==========================================================
Jarvis-X Dispatcher
Version : 1.0.0
==========================================================

Central command dispatcher.

Flow:

User
    ↓
NLU
    ↓
Router
    ↓
Handler
    ↓
CommandResult
"""

from core.nlu import preprocess
from core.parser import normalize
from core.router import route

from core.logger import (
    info,
    warning,
)

from modules.handlers.ai_handler import handle as ai_handler


# ==========================================================
# Handler Registry
# ==========================================================

HANDLERS = {
    "ask_ai": ai_handler,
}


# ==========================================================
# Dispatcher
# ==========================================================

def execute_command(command: str):
    """
    Main dispatcher.
    """

    info(f"User Command : {command}")

    # ------------------------------------------------------
    # NLU
    # ------------------------------------------------------

    cmd = preprocess(command)

    normalized = normalize(
        f"{cmd.action} {cmd.target}".strip()
    )

    info(
        f"Normalized : {normalized}"
    )

    # ------------------------------------------------------
    # Router
    # ------------------------------------------------------

    intent, value = route(cmd)

    info(
        f"Intent : {intent}"
    )

    # ------------------------------------------------------
    # Handler
    # ------------------------------------------------------

    handler = HANDLERS.get(intent)

    if handler is None:

        warning(
            f"No handler for '{intent}'"
        )

        print(
            f"\n⚠ No handler registered for '{intent}'."
        )

        return

    result = handler(
        intent,
        value,
    )

    # ------------------------------------------------------
    # Result
    # ------------------------------------------------------

    if result:

        info(
            result.message
        )

    else:

        warning(
            result.message
        )