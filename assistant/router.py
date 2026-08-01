from assistant.speak import speak
from assistant.weather import get_weather
from assistant.time_service import get_current_time, get_current_date
from assistant.website import open_website
from assistant.web_search import search_web
from assistant.application import open_application
from assistant.reminder import set_reminder
from assistant.email_service import send_email


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
    # Open Application
    # -------------------------------
    elif intent == "open_application":
        application = intent_data.get("application")

        if application:
            response = open_application(application)
            speak(response)
        else:
            speak("Please tell me which application you want to open.")

    # -------------------------------
    # Web Search
    # -------------------------------
    elif intent == "search_web":
        query = intent_data.get("query")

        if query:
            response = search_web(query)
            speak(response)
        else:
            speak("Please tell me what you want to search.")

    # -------------------------------
    # Reminder
    # -------------------------------
    elif intent == "reminder":
        minutes = intent_data.get("minutes")

        if minutes:
            response = set_reminder(minutes)
            speak(response)
        else:
            speak("Please tell me after how many minutes to remind you.")

    # -------------------------------
    # Send Email
    # -------------------------------
    elif intent == "send_email":

        recipient_email = intent_data.get("recipient_email")
        subject = intent_data.get("subject")
        message = intent_data.get("message")

        if recipient_email and subject and message:

            response = send_email(
                recipient_email,
                subject,
                message
            )

            speak(response)

        else:
            speak("Please provide the recipient email, subject, and message.")

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