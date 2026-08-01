import pyttsx3
import threading

# Lock to prevent multiple threads from speaking simultaneously
speech_lock = threading.Lock()

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty("voices")

# Male voice
engine.setProperty("voice", voices[0].id)

# Speed
engine.setProperty("rate", 170)

# Volume
engine.setProperty("volume", 1.0)


def speak(text):
    """
    Convert text to speech safely.
    """

    with speech_lock:
        print(f"Assistant: {text}")

        engine.say(text)
        engine.runAndWait()