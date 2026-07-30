"""
==========================================================
Jarvis-X AI Handler
Version : 1.0.0
==========================================================

Handles all AI-related requests.
"""

from core.decision_engine import decide
from core.ai_manager import get_response
from core.models.result import CommandResult

from core.logger import (
    info,
    error,
)

from modules.web_search import search_web
from modules.speaker import speak


# ==========================================================
# AI Handler
# ==========================================================

def handle(intent: str, value: str) -> CommandResult:
    """
    Handle AI requests.

    Returns:
        CommandResult
    """

    if intent != "ask_ai":

        return CommandResult.fail(
            "Unsupported AI intent."
        )

    try:

        decision = decide(value)

        info(
            f"AI Source : {decision.source}"
        )

        use_web = (
            decision.source == "web"
        )

        web_results = ""

        if use_web:

            info(
                "Searching live web..."
            )

            web_results = search_web(
                value
            )

        response = get_response(
            question=value,
            use_web=use_web,
            web_results=web_results,
        )

        print()

        print("🤖 Jarvis-X\n")

        print(response)

        speak(
            response,
            print_text=False,
        )

        return CommandResult.ok(
            message=response,
            data=response,
        )

    except Exception as e:

        error(str(e))

        return CommandResult.fail(
            message=str(e)
        )