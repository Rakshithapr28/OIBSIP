import speech_recognition as sr

from assistant.speak import speak


# Create recognizer object
recognizer = sr.Recognizer()


def listen():
    """
    Listen to the user's voice and convert it into text.
    """

    with sr.Microphone() as source:
        print("🎤 Listening...")

        # Reduce background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Capture audio
        audio = recognizer.listen(source)

    try:
        print("🔄 Recognizing...")

        command = recognizer.recognize_google(audio)

        print(f"You said: {command}")

        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Please repeat.")
        return None

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None