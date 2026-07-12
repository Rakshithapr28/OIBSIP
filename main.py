from assistant.speech import listen
from assistant.ai_service import detect_intent
from assistant.router import route
from assistant.speak import speak


def main():

    speak("Hello Sagar. I am your AI Voice Assistant.")

    while True:

        user_input = listen()

        if not user_input:
            continue

        intent_data = detect_intent(user_input)

        print("\nIntent Data:")
        print(intent_data)

        route(intent_data)

        if intent_data.get("intent") == "exit":
            break


if __name__ == "__main__":
    main()