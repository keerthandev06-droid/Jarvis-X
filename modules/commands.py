"""
==========================================================
Jarvis-X Command Processor
Version : 7.0.0
==========================================================
"""

from core.nlu import preprocess
from core.parser import normalize
from core.router import route
from core.command_registry import COMMANDS
from core.resource_manager import open_resource
from core.resource_resolver import resolve
from core.decision_engine import decide
from core.ai_manager import get_response

from core.logger import (
    info,
    warning as log_warning,
    error as log_error,
)

from modules.ui import warning
from modules.web_launcher import open_website
from modules.web_search import search_web

from modules.speaker import (
    speak,
    opening,
    not_found,
    unknown,
)


# ==========================================================
# Execute Command
# ==========================================================

def execute_command(command):
    """
    Main Jarvis-X Command Dispatcher
    """

    info(f"User Command: {command}")

    # ------------------------------------------------------
    # NLU
    # ------------------------------------------------------

    cmd = preprocess(command)

    normalized = normalize(
        f"{cmd.action} {cmd.target}".strip()
    )

    info(f"Normalized Command: {normalized}")

    # ------------------------------------------------------
    # Intent Detection
    # ------------------------------------------------------

    intent, value = route(cmd)

    # ------------------------------------------------------
    # AI Requests
    # ------------------------------------------------------

    if intent == "ask_ai":

        try:

            decision = decide(command)

            info(
                f"Decision Engine : "
                f"{decision.source}"
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
                    command
                )

            response = get_response(
                question=command,
                use_web=use_web,
                web_results=web_results,
            )

            print("\n🤖 Jarvis-X:\n")
            print(response)

            speak(
                response,
                print_text=False,
            )

            info(
                "AI response generated."
            )

            return response

        except Exception as e:

            warning(str(e))

            log_error(str(e))

            speak(
                "Sorry, I couldn't process your request."
            )

            return

    # ------------------------------------------------------
    # Website
    # ------------------------------------------------------

    if intent == "open_website":

        if open_website(value):

            opening(value)

            info(
                f"Opened Website: {value}"
            )

        else:

            warning(
                f'"{value}" not found.'
            )

            not_found(value)

            log_warning(
                f"Website Not Found: {value}"
            )

        return

    # ------------------------------------------------------
    # Resolve Resource
    # ------------------------------------------------------

    if value:

        value = resolve(value)
            # ------------------------------------------------------
    # Open App / File
    # ------------------------------------------------------

    if intent in ("open_app", "open_file"):

        if open_resource(value):

            opening(value)

            info(
                f"Opened Resource: {value}"
            )

        else:

            warning(
                f'"{value}" not found.'
            )

            not_found(value)

            log_warning(
                f"Resource Not Found: {value}"
            )

        return

    # ------------------------------------------------------
    # Other Commands
    # ------------------------------------------------------

    handler = COMMANDS.get(intent)

    if handler is None:

        unknown()

        warning(
            "Unknown command."
        )

        log_warning(
            f"Unknown Command: {command}"
        )

        return

    # ------------------------------------------------------
    # Execute Handler
    # ------------------------------------------------------

    try:

        if value:

            handler(value)

        else:

            handler()

        info(
            f"Executed Intent: {intent}"
        )

    except TypeError:

        try:

            handler()

            info(
                f"Executed Intent: {intent}"
            )

        except Exception as e:

            warning(str(e))

            log_error(str(e))

            speak(
                "An error occurred while "
                "executing the command."
            )

    except Exception as e:

        warning(str(e))

        log_error(str(e))

        speak(
            "An error occurred while "
            "executing the command."
        )