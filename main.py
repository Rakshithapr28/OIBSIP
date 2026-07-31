from assistant.speech import listen
from assistant.speak import speak
from assistant.ai_service import detect_intent
from assistant.router import route


def main():

    speak("Hello Sagar. I am your AI Voice Assistant.")

    while True:

        # Listen to the user
        user_input = listen()

        if not user_input:
            continue

        # Ask Gemini to understand the request
        intent_data = detect_intent(user_input)

        print("\nIntent Data:")
        print(intent_data)

        # Route the request
        route(intent_data)

        # Exit assistant
        if intent_data.get("intent") == "exit":
            break


if __name__ == "__main__":
    main()