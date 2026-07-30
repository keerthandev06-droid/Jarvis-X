"""
Jarvis-X Smart Voice Engine
Version: 3.0.0
"""

import tempfile
import wave

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

# =====================================================
# SETTINGS
# =====================================================

SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_SIZE = 1024

VOICE_THRESHOLD = 700
SILENCE_LIMIT = 25

print("Loading Whisper model (small)...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)

print("Whisper ready!")


# =====================================================
# MICROPHONE
# =====================================================

def get_microphone():
    devices = sd.query_devices()

    print("\nAvailable Input Devices:\n")

    best = None

    for index, device in enumerate(devices):

        if device["max_input_channels"] <= 0:
            continue

        print(f"[{index}] {device['name']}")

        name = device["name"].lower()

        if "noise" in name:
            return index

        if "headset" in name:
            best = index

        elif "microphone" in name and best is None:
            best = index

    return best


# =====================================================
# LISTEN
# =====================================================

def listen():

    device = get_microphone()

    if device is None:
        print("❌ No microphone found.")
        return ""

    print(f"\nUsing microphone: {device}")
    print("\n🎤 Waiting for speech...")

    frames = []

    recording = False
    silence = 0

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        blocksize=CHUNK_SIZE,
        device=device,
    )

    with stream:

        while True:

            data, overflow = stream.read(CHUNK_SIZE)

            volume = np.abs(data).mean()

            if not recording:

                if volume > VOICE_THRESHOLD:

                    print("🎙 Recording...")

                    recording = True

                    frames.append(data.copy())

            else:

                frames.append(data.copy())

                if volume < VOICE_THRESHOLD:

                    silence += 1

                else:

                    silence = 0

                if silence >= SILENCE_LIMIT:
                    break

    if not frames:
        return ""

    audio = np.concatenate(frames)

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as temp:

        filename = temp.name

    with wave.open(filename, "wb") as wav:

        wav.setnchannels(CHANNELS)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(audio.tobytes())

    print("🧠 Transcribing...")

    segments, info = model.transcribe(
        filename,
        language="en",
        beam_size=10,
        vad_filter=True,
        temperature=0.0,
    )

    text = ""

    for segment in segments:
        text += segment.text

    text = text.strip()

    print("\nDetected Language :", info.language)
    print("Recognized Text   :", text)

    return text


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    print("\n===== Jarvis Voice Test =====\n")

    while True:

        result = listen()

        if result:

            print("\n✅ You said:", result)

        else:

            print("\n⚠ Nothing detected.\n")