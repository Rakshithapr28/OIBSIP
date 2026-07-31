from assistant.speak import speak
from assistant.weather import get_weather
from assistant.time_service import get_current_time, get_current_date
from assistant.website import open_website


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
    # Time
    # -------------------------------
    elif intent == "time":
        current_time = get_current_time()
        speak(current_time)

    # -------------------------------
    # Date
    # -------------------------------
    elif intent == "date":
        current_date = get_current_date()
        speak(current_date)

    # -------------------------------
    # Open Website
    # -------------------------------
    elif intent == "open_website":
        website = intent_data.get("website")

        if website:
            response = open_website(website)
            speak(response)
        else:
            speak("Please tell me which website you want to open.")

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