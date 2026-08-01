import speech_recognition as sr

from assistant.speak import speak


# Create recognizer object
recognizer = sr.Recognizer()

# Better microphone settings
recognizer.pause_threshold = 1
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True


def listen():
    """
    Listen to the user's voice and convert it into text.
    """

    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")

            # Reduce background noise
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # Capture audio
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("🔄 Recognizing...")

        command = recognizer.recognize_google(audio)

        print(f"You said: {command}")

        return command.lower()

    except sr.WaitTimeoutError:
        # No speech detected within timeout
        return None

    except sr.UnknownValueError:
        # Speech detected but not understood
        return None

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None

    except Exception as e:
        print(f"Speech Error: {e}")
        return None