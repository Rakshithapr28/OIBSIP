from assistant.speak import speak
from assistant.weather import get_weather


def route(intent_data):
    """
    Route the detected intent to the appropriate module.
    """

    intent = intent_data.get("intent")

    # -------------------------------
    # Conversation
    # -------------------------------
    if intent == "conversation":
        response = intent_data.get("response")
        speak(response)

    # -------------------------------
    # Weather
    # -------------------------------
    elif intent == "weather":
        city = intent_data.get("city")

        if city:
            weather_report = get_weather(city)
            speak(weather_report)
        else:
            speak("Please tell me the city name.")

    # -------------------------------
    # Reminder
    # -------------------------------
    elif intent == "reminder":
        minutes = intent_data.get("minutes")
        speak(f"Setting a reminder for {minutes} minutes.")

    # -------------------------------
    # Send Email
    # -------------------------------
    elif intent == "send_email":
        recipient = intent_data.get("recipient")
        message = intent_data.get("message")

        speak(f"Preparing to send an email to {recipient}.")

        # We'll implement email_service.py later.

    # -------------------------------
    # Web Search
    # -------------------------------
    elif intent == "search_web":
        query = intent_data.get("query")
        speak(f"Searching the web for {query}")

        # We'll implement search.py later.

    # -------------------------------
    # Exit
    # -------------------------------
    elif intent == "exit":
        speak("Goodbye Sagar! Have a great day.")

    # -------------------------------
    # Unknown Intent
    # -------------------------------
    else:
        speak("Sorry Sagar, I couldn't understand your request.")