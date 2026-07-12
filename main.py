from assistant.speak import speak
from assistant.speech import listen


def main():
    speak("Hello Sagar, I am your AI Voice Assistant.")

    while True:
        command = listen()

        if command:
            speak(f"You said {command}")

            if "exit" in command or "bye" in command:
                speak("Goodbye! Have a nice day.")
                break


if __name__ == "__main__":
    main()