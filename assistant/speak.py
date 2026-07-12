import pyttsx3


# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty("voices")

# Set male voice (usually the first voice on Windows)
engine.setProperty("voice", voices[0].id)

# Set speaking speed
engine.setProperty("rate", 170)

# Set volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)


def speak(text):
    """
    Convert text to speech.
    """
    engine.say(text)
    engine.runAndWait()