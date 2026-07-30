"""
==========================================================
Jarvis-X Speaker
Version : 3.0.0
==========================================================
"""

import pyttsx3

from config import (
    ASSISTANT_NAME,
    VOICE_RATE,
    VOICE_VOLUME,
)

# ==========================================================
# Initialize Engine
# ==========================================================

engine = pyttsx3.init()

engine.setProperty("rate", VOICE_RATE)
engine.setProperty("volume", VOICE_VOLUME)

# ==========================================================
# Select Best Voice
# ==========================================================

voices = engine.getProperty("voices")

if voices:

    selected_voice = voices[0].id

    for voice in voices:

        name = voice.name.lower()

        if "zira" in name:
            selected_voice = voice.id
            break

        if "david" in name:
            selected_voice = voice.id

    engine.setProperty("voice", selected_voice)

# ==========================================================
# Core Speak
# ==========================================================


def speak(text: str, print_text: bool = True):
    """
    Speak text.
    """

    if not text:
        return

    text = str(text).strip()

    if not text:
        return

    if print_text:
        print(f"\n🤖 {ASSISTANT_NAME}:\n{text}")

    try:

        engine.stop()

        engine.say(text)

        engine.runAndWait()

    except Exception as e:

        print(f"TTS Error: {e}")


# ==========================================================
# Helper Messages
# ==========================================================


def startup(owner: str):

    speak(f"Welcome back, {owner}.", print_text=False)


def listening():

    print("\n🎤 Listening...")


def thinking():

    speak("Please wait. Let me think.")


def opening(name):

    speak(f"Opening {name}.")


def completed():

    speak("Done.")


def not_found(name):

    speak(f"Sorry, I couldn't find {name}.")


def unknown():

    speak("Sorry, I didn't understand that command.")


def goodbye():

    speak("Goodbye. Have a nice day.")


def error():

    speak("Sorry. Something went wrong.")