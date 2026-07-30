"""
==========================================================
Jarvis-X Gemini AI Module
Version : 4.0.0
==========================================================
"""

import os

from dotenv import load_dotenv
from google import genai

from config import GEMINI_MODEL
from modules.conversation_memory import (
    add_message,
    get_messages,
)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=API_KEY)


def _generate(contents):

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=contents,
    )

    if hasattr(response, "text") and response.text:
        return response.text.strip()

    return "Sorry, I couldn't generate a response."


def ask_ai(prompt: str):
    """
    Normal AI conversation.
    """

    if not prompt:
        return "Please enter a question."

    add_message("user", prompt)

    history = []

    for message in get_messages():

        history.append(
            {
                "role": message["role"],
                "parts": [
                    {
                        "text": message["content"]
                    }
                ],
            }
        )

    try:

        reply = _generate(history)

        add_message("model", reply)

        return reply

    except Exception as e:

        return f"AI Error: {e}"


def ask_ai_with_web(question: str, web_results: str):
    """
    AI + Live Web Results
    """

    prompt = f"""
You are Jarvis-X.

Use ONLY the web search results below.

If the answer is present,
answer accurately.

If it is not present,
say the information was not found.

=========================
WEB SEARCH RESULTS
=========================

{web_results}

=========================
USER QUESTION
=========================

{question}

Give a clean natural answer.
"""

    try:

        contents = [
            {
                "role": "user",
                "parts": [
                    {
                        "text": prompt
                    }
                ],
            }
        ]

        return _generate(contents)

    except Exception as e:

        return f"AI Error: {e}"


if __name__ == "__main__":

    while True:

        q = input("You : ")

        if q.lower() == "exit":
            break

        print()

        print(ask_ai(q))

        print()