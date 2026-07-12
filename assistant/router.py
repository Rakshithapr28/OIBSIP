from assistant.speak import speak


def route(intent_data):
    """
    Route the detected intent to the appropriate module.
    """

    intent = intent_data.get("intent")

    if intent == "greeting":
       print("Greeting route executed")
       speak("Hello Sagar! How can I help you today?")

    elif intent == "weather":
        city = intent_data.get("city")
        speak(f"Getting weather information for {city}")

    elif intent == "reminder":
        minutes = intent_data.get("minutes")
        speak(f"Setting a reminder for {minutes} minutes")

    elif intent == "send_email":
        speak("Email feature is under development.")

    elif intent == "search_web":
        query = intent_data.get("query")
        speak(f"Searching for {query}")

    elif intent == "general_question":
        question = intent_data.get("question")
        speak(f"You asked {question}")

    elif intent == "exit":
        speak("Goodbye! Have a nice day.")

    else:
        speak("Sorry, I don't know how to handle that request.")