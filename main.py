from assistant.speech import listen
from assistant.speak import speak
from assistant.ai_service import detect_intent
from assistant.router import route
from assistant.local_handler import handle_local_command


def main():

    speak("Hello Rakshitha. I am your AI Voice Assistant.")

    while True:

        # Listen to the user
        user_input = listen()

        if not user_input:
            continue

        # ---------------------------------------
        # Step 1: Handle local commands first
        # ---------------------------------------
        intent_data = handle_local_command(user_input)

        # ---------------------------------------
        # Step 2: If not a local command, use Gemini
        # ---------------------------------------
        if intent_data is None:
            intent_data = detect_intent(user_input)

        print("\nIntent Data:")
        print(intent_data)

        # ---------------------------------------
        # Step 3: Route the request
        # ---------------------------------------
        route(intent_data)

        # ---------------------------------------
        # Step 4: Exit
        # ---------------------------------------
        if intent_data.get("intent") == "exit":
            break


if __name__ == "__main__":
    main()