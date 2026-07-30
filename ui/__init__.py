"""
Jarvis-X Voice Engine
Version: 1.0

Speech Recognition using:
- sounddevice
- soundfile
- SpeechRecognition
"""

import os
import tempfile

import sounddevice as sd
import soundfile as sf
import speech_recognition as sr


SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5


def listen():
    """
    Record voice from microphone
    and convert it to text.
    """

    print("\n🎤 Listening...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as temp_audio:

        temp_path = temp_audio.name

    sf.write(
        temp_path,
        recording,
        SAMPLE_RATE
    )

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile(temp_path) as source:

            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        print(f"\n🗣 You said: {text}")

        return text.lower()

    except sr.UnknownValueError:

        print("❌ Couldn't understand.")

        return ""

    except sr.RequestError as e:

        print(f"❌ Speech service error: {e}")

        return ""

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)