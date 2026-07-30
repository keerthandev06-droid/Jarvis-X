"""
==========================================================
Jarvis-X AI Manager
Version : 2.0.0
==========================================================

Purpose:
Central AI controller.

Responsibilities:
- Handle normal AI requests
- Handle live web AI requests
- Detect Gemini failures
- Return fallback responses
"""

from core.ai_fallback import fallback_response

from modules.ai_chat import (
    ask_ai,
    ask_ai_with_web,
)


# ==========================================================
# Error Detection
# ==========================================================

ERROR_KEYWORDS = (
    "ai error",
    "429",
    "resource_exhausted",
    "quota",
    "rate limit",
    "timed out",
    "connection",
    "network",
)


def _is_ai_error(response: str) -> bool:
    """
    Returns True if the response looks like an AI failure.
    """

    if not response:
        return True

    response = response.lower()

    return any(
        keyword in response
        for keyword in ERROR_KEYWORDS
    )


# ==========================================================
# Main AI Entry
# ==========================================================

def get_response(
    question: str,
    use_web: bool = False,
    web_results: str = "",
) -> str:
    """
    Main AI controller.
    """

    question = str(question).strip()

    if not question:
        return "Please enter a question."

    try:

        # --------------------------------------
        # AI + Live Web
        # --------------------------------------

        if use_web:

            ai_response = ask_ai_with_web(
                question,
                web_results,
            )

            return fallback_response(
                ai_response,
                web_results,
            )

        # --------------------------------------
        # Normal AI
        # --------------------------------------

        ai_response = ask_ai(question)

        if _is_ai_error(ai_response):

            return (
                "I'm currently unable to contact "
                "the AI service. Please try again "
                "in a few moments."
            )

        return ai_response

    except Exception:

        if use_web:

            return fallback_response(
                "",
                web_results,
            )

        return (
            "I'm currently unable to process "
            "your request."
        )


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    print("Jarvis-X AI Manager")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You : ").strip()

        if question.lower() == "exit":
            break

        print()
        print(get_response(question))
        print()